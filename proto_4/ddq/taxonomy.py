import uuid
from uuid import UUID
from typing import Union, List, Tuple, Any
import logging
import pprint
from tabulate import tabulate
import tinydb
import sys

from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter


from .print_tree import print_tuple_tree

FuzzyBoxType = Union[str, UUID]


class World:
    def __init__(self, json_file: str = None):
        self._db = tinydb.TinyDB(json_file, sort_keys=True, indent=4)

    def _boxes(self):
        return self._db.table("Boxes")
    
    def _relations(self):
        return self._db.table("Relations")

    def boxes(self) -> List[Any]:
        return self._boxes().all()
    
    def relations(self) -> List[Any]:
        return self._relations().all()

    def add_box(self, name: str):
        self._boxes().insert({"name": name})
        
    def add_relation(self, 
                     relation: FuzzyBoxType, 
                     a: FuzzyBoxType, 
                     b: FuzzyBoxType):
        # TODO: do not duplicate
        self._relations().insert({"relation": relation, "a": a, "b": b})
        
    def find_box_ids_by_name(self, name: str) -> List[int]:
        exact_boxes = [x.doc_id for x in self._boxes() if x["name"] == name]
        if len(exact_boxes) > 0:
            return exact_boxes
        fuzzy_boxes = [x.doc_id for x in self._boxes() if name in x["name"]]
        if len(fuzzy_boxes) > 0:
            return fuzzy_boxes
        very_fuzzy_boxes = [x.doc_id for x in self._boxes()
                            if name.lower() in x["name"].lower()]
        if len(very_fuzzy_boxes) > 0:
            return very_fuzzy_boxes
        return []

    def find_box_id(self, box: FuzzyBoxType) -> int:
        if isinstance(box, int):
            return self.get_box(box).doc_id
        else:
            box_ids = self.find_box_ids_by_name(box)
            if len(box_ids) == 1:
                return box_ids[0]
        return None
    
    def soft_find_box_id(self, box: FuzzyBoxType) -> Union[int, str]:
        box_id = self.find_box_id(box)
        return box_id if box_id is not None else box

    def get_box(self, id: int) -> Any:
        return self._boxes().get(doc_id = id)
    
    def get_box_name(self, id: int) -> str:
        return self.get_box(id)["name"]

    def find_box(self, box: FuzzyBoxType) -> Any:
        return self.get_box(self.find_box_id(box))

    def relate(self, 
               a: FuzzyBoxType,
               relation: FuzzyBoxType,
               b: FuzzyBoxType):
        self.add_relation(
            self.soft_find_box_id(relation),
            self.soft_find_box_id(a),
            self.soft_find_box_id(b)
        )
        
    '''
    def add_input(self, 
                  box: FuzzyBoxType,
                  type_djnf: FuzzyBoxType = None,
                  name: str = None):
        self._relations().insert({"relation": relation, "a": a, "b": b})
    '''


    def build_relation_matrix(self, 
                            box: FuzzyBoxType, 
                            relation: FuzzyBoxType = None):
        def find_related_box_ids(all_relations, box_id):
            relatex_box_ids = set()
            for rel in all_relations:
                if rel["a"] == box_id:
                    relatex_box_ids.add(rel["b"])
                elif rel["b"] == box_id:
                    relatex_box_ids.add(rel["a"])
            return relatex_box_ids
        
        def make_relation_matrix(all_relations, box_id_set):
            box_id_index = {}
            box_index_id = {}
            matrix = []
            for i, box_id in enumerate(box_id_set):
                box_id_index[box_id] = i
                box_index_id[i] = box_id
            for _r in range(len(box_id_set)):
                cols = []
                for _c in range(len(box_id_set)):
                    cols.append([])
                matrix.append(cols)
            for rel in all_relations:
                if rel["a"] in box_id_set and rel["b"] in box_id_set:
                    row = box_id_index[rel["a"]]
                    col = box_id_index[rel["b"]]
                    matrix[row][col].append(rel["relation"])
            box_ids = [box_index_id[i] for i in range(len(box_id_set))]
            return box_ids, matrix

        if self.find_box_id(box) is None:
            return []
        if relation is not None and self.find_box_id(relation) is None:
            return []
        filter_relation_id = (self.find_box_id(relation) 
                              if relation is not None else None)
        all_relations = [rel for rel in self.relations()
                         if (filter_relation_id is None 
                             or filter_relation_id == rel["relation"])]
        box_id_set = set()
        new_box_ids = set([self.find_box_id(box)])
        while len(new_box_ids) > 0:
            box_id_set = box_id_set.union(new_box_ids)
            next_box_ids = set()
            for box_id in new_box_ids:
                rel_ids = find_related_box_ids(all_relations, 
                                               box_id)
                next_box_ids = next_box_ids.union(
                                    set([x for x in rel_ids 
                                        if x not in box_id_set]))
            new_box_ids =  next_box_ids
        return make_relation_matrix(all_relations, box_id_set)


def make_sep(count = 1):
    return "".join(["  "] * count)


def prompt_box(world: World, text: str):
    name_completer = FuzzyWordCompleter([x["name"] for x in world.boxes()])
    choice = prompt(text, 
                    completer=name_completer, 
                    complete_while_typing=True)
    return choice if len(choice.strip()) > 0 else None


def cmd_box(world: World):
    name = prompt(make_sep() + "name\n" + make_sep(2))
    world.add_box(name)


def cmd_relate(world: World):
    a = prompt_box(world, make_sep() + "box\n" + make_sep(2))
    relation = prompt_box(world, make_sep() + "relation\n" + make_sep(2))
    b = prompt_box(world, make_sep() + "to\n" + make_sep(2))
    world.relate(a, relation, b)


def cmd_graph(world: World):
    def try_print_as_tree(box_ids, matrix):
        def recurse_get_children(node_i, 
                                 matrix, 
                                 transpose, 
                                 loop_guard_set=set()):
            if node_i in loop_guard_set:
                return ("LOOP", [])
            else:
                loop_guard_set.add(node_i)
            n = len(matrix)
            if transpose:
                children_indices = [ri for ri in range(n)
                                    if len(matrix[ri][node_i]) > 0]
            else:
                children_indices = [ci for ci in range(n)
                                    if len(matrix[node_i][ci]) > 0]
            children = [recurse_get_children(x, 
                                             matrix, 
                                             transpose, 
                                             loop_guard_set) 
                        for x in children_indices]
            return (node_i, children)

        n = len(box_ids)
        transpose = False
        
        roots = []
        for ci in range(n):
            if all([len(matrix[ri][ci]) == 0 for ri in range(n)]):
                roots.append(ci)
        
        if len(roots) != 1:
            transpose = True
            roots = []
            for ri in range(n):
                if all([len(matrix[ri][ci]) == 0 for ci in range(n)]):
                    roots.append(ri)
        
        if len(roots) != 1:
            return False

        tree = recurse_get_children(roots[0], matrix, transpose)
        print_tuple_tree(tree, 
                         namer_func=lambda i: world.get_box_name(box_ids[i]))
        return True

    a = prompt_box(world, make_sep() + "box\n" + make_sep(2))
    relation = prompt_box(world, make_sep() + "relation\n" + make_sep(2))
    box_ids, matrix = world.build_relation_matrix(a, relation)
    print("")
    if not try_print_as_tree(box_ids, matrix):
        print(tabulate(matrix, headers=box_ids))


def cmd_list(world: World):
    boxes = sorted(world.boxes(), key= lambda box: box["name"])
    print(tabulate(boxes))


command_handlers = {
    "box": cmd_box,
    "relate": cmd_relate,
    "ls": cmd_list,
    "graph": cmd_graph,
}


world = World('test.json' if len(sys.argv) == 1 else sys.argv[1])
while (True):
    try:
        command = input("> ")
        if command == "help":
            print("\n".join([make_sep(2) + x for x in command_handlers.keys()]))
        else:
            handle_command = command_handlers[command]
            handle_command(world)
    except KeyboardInterrupt:
        break
    except Exception as ex:
         logging.exception("")
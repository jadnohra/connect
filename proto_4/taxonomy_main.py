import uuid
from uuid import UUID
from typing import Union, List, Tuple, Any
import logging
import pprint
from tabulate import tabulate
import tinydb

from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter


FuzzyBoxType = Union[str, UUID]


class Box:
    def __init__(self, name: str = None):
        self._id = uuid.uuid4()
        self._name = name
        self._relations = []

    def relate(self, relation: FuzzyBoxType, b: FuzzyBoxType):
        self._relations.append((relation, b))

    def id(self) -> UUID:
        return self._id
    
    def name(self) -> str:
        return self._name
    
    def relations(self) -> List[Tuple[FuzzyBoxType, FuzzyBoxType]]:
        return self._relations

class World:
    def __init__(self):
        self._boxes = {}

    def boxes(self) -> List[Box]:
        return self._boxes.values()

    def add_box(self, name: str):
        box = Box(name)
        self._boxes[box.id()] = box

    def find_boxes_by_name(self, name: str) -> List[Box]:
        exact_boxes = [x for x in self._boxes.values() if x.name() == name]
        if len(exact_boxes) > 0:
            return exact_boxes
        fuzzy_boxes = [x for x in self._boxes.values() if name in x.name()]
        if len(fuzzy_boxes) > 0:
            return fuzzy_boxes
        very_fuzzy_boxes = [x for x in self._boxes.values() 
                            if name.lower() in x.name().lower()]
        if len(very_fuzzy_boxes) > 0:
            return very_fuzzy_boxes
        return []

    def find_box(self, box: FuzzyBoxType) -> Box:
        if isinstance(box, UUID):
            return self._boxes[box]
        else:
            boxes = self.find_boxes_by_name(box)
            if len(boxes) == 1:
                return boxes[0]
        return None

    def relate(self, 
                     a: FuzzyBoxType, 
                     relation: FuzzyBoxType, 
                     b: FuzzyBoxType):
        abox = self.find_box(a)
        abox.relate(relation, b)

class WorldDb:
    def __init__(self, json_file: str = None):
        self._db = tinydb.TinyDB(json_file)

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

    def find_box(self, box: FuzzyBoxType) -> Any:
        return self.get_box(self.find_box_id(box))

    def relate(self, 
               a: FuzzyBoxType,
               relation: FuzzyBoxType,
               b: FuzzyBoxType):
        self.add_relation(
            self.soft_find_box_id(a),
            self.soft_find_box_id(relation),
            self.soft_find_box_id(b)
        )


    def build_relation_tree(self, 
                            box: FuzzyBoxType, 
                            relation: FuzzyBoxType = None):
        def find_related_box_ids(all_relations, box_id, relation_id):
            relatex_box_ids = set()
            for rel in all_relations:
                if relation_id is None or relation_id == rel["relation"]:
                    if rel["a"] == box_id:
                        relatex_box_ids.add(rel["b"])
                    elif rel["b"] == box_id:
                        relatex_box_ids.add(rel["a"])
            return relatex_box_ids
        
        if self.find_box_id(box) is None:
            return []
        if relation is not None and self.find_box_id(relation) is None:
            return []
        relation_id = (self.find_box_id(relation) 
                       if relation is not None else None)
        all_relations = self.relations()
        relations = {}
        related_box_ids = set()
        new_box_ids = set([self.find_box_id(box)])
        while len(new_box_ids) > 0:
            related_box_ids = related_box_ids.union(new_box_ids)
            next_box_ids = set()
            for box_id in new_box_ids:
                rel_ids = find_related_box_ids(all_relations, 
                                               box_id, 
                                               relation_id)
                next_box_ids = next_box_ids.union(
                                    set([x for x in rel_ids 
                                        if x not in related_box_ids]))
            new_box_ids =  next_box_ids
        # something like this? https://github.com/Nelarius/imnodes
        return related_box_ids


def make_sep(count = 1):
    return "".join(["  "] * count)


def prompt_box(world: World, text: str):
    name_completer = FuzzyWordCompleter([x["name"] for x in world.boxes()])
    return prompt(
        text, 
        completer=name_completer, 
        complete_while_typing=True)


def cmd_box(world: World):
    name = prompt(make_sep() + "name\n" + make_sep(2))
    world.add_box(name)


def cmd_relate(world: World):
    a = prompt_box(world, make_sep() + "box\n" + make_sep(2))
    relation = prompt_box(world, make_sep() + "relation\n" + make_sep(2))
    b = prompt_box(world, make_sep() + "to\n" + make_sep(2))
    world.relate(a, relation, b)


def cmd_tree(world: World):
    a = prompt_box(world, make_sep() + "box\n" + make_sep(2))
    print(world.build_relation_tree(a))


def cmd_list(world: World):
    boxes = sorted(world.boxes(), key= lambda box: box["name"])
    print(tabulate(boxes))


command_handlers = {
    "box": cmd_box,
    "relate": cmd_relate,
    "ls": cmd_list,
    "tree": cmd_tree,
}


world = WorldDb('test.json')
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
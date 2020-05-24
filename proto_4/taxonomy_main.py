import uuid
from uuid import UUID
from typing import Union, List, Tuple, Any
import logging
import pprint
from tabulate import tabulate
import tinydb


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

    def boxes(self) -> List[Box]:
        return self._boxes().all()

    def add_box(self, name: str):
        self._boxes().insert({"name": name, "relations": []})
        
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
        a_box = self.find_box(a)
        relation_box = self.soft_find_box_id(relation)
        b_box = self.soft_find_box_id(b)
        new_relations = a_box["relations"] + [
            [relation_box, b_box]
        ]
        self._boxes().update(
            {"relations": new_relations},
            doc_ids = [a_box.doc_id]
        )

def make_sep(count = 1):
    return "".join(["  "] * count)

def cmd_box(world: World):
    name = input(make_sep() + "name\n" + make_sep(2))
    world.add_box(name)

def cmd_relate(world: World):
    a = input(make_sep() + "box\n" + make_sep(2))
    relation = input(make_sep() + "relation\n" + make_sep(2))
    b = input(make_sep() + "to\n" + make_sep(2))
    world.relate(a, relation, b)

def cmd_list(world: World):
    boxes = sorted(world.boxes(), key= lambda box: box["name"])
    print(tabulate(boxes))


command_handlers = {
    "box": cmd_box,
    "relate": cmd_relate,
    "ls": cmd_list,
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
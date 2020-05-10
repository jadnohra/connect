from typing import List, Any


def find_instances_of(items: List, item_class: type) -> List:
    return [x for x in items if isinstance(x, item_class)]


def find_instance_of(items: List, item_class: type) -> Any:
    candidates = find_instances_of(items, item_class)
    assert len(candidates) == 1
    return candidates[0]
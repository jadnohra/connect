from typing import Any


def check_type(object: Any, check_type: type, allow_type_object: bool = True):
    if isinstance(object, check_type):
        return True
    if (allow_type_object 
         and isinstance(object, type) 
         and issubclass(object, check_type)):
        return True
    return False

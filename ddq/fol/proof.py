from typing import List, Dict, Tuple
from .lang import Wff

class Variable:

    def is_arbitrary(self) -> bool:
        pass

class Line:

    def get_number(self) -> int:
        pass

    def get_wff(self) -> Wff:
        pass 

    def premisses(self) -> List["Line"]:
        pass

    def variables(self) -> Dict[str, Variable]:
        pass

    def inference(self) -> "Inference":
        pass

    def application(self) -> "Application":
        pass


class Application:
    def __init__(self):
        pass

class Inference:
    def possible_conclusions(self, line: Line) -> List[Tuple[Line, Application]]:
        pass


class Proof:
    def lines(self) -> List[Line]:
        pass

    def declare(self, premisses: List[Wff], conclusion: Wff) -> None:
        pass

    def extend(self, line: Line, inference: Inference, application: Application) -> "Proof":
        pass


from typing import List
from .fol import Wff


class Inference:
    def short_name(self):
        pass

    def possible_inferences(self, permisses: List[Wff]) -> List[Wff]:
        pass

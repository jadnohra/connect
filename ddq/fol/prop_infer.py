'''
References:
 - Symbolic Logic, Copi, p.33, 396
'''
from typing import List, Tuple, Callable
from .lang import (
    PropositionalVariable,
    Wff, PropVarWff, ImplWff, ConjWff, DisjWff, NegWff)
from .proof import Inference, Application, Line


def find_proposional_patterns(premises: List[Wff], 
                              form_constrains: List[Callable],
                              final_constraint: Callable) -> List:
    compat_premise_ilists = []
    for form_constraint in form_constrains:
        compat_premises_ilist = [i for i in range(len(premises))
                                 if form_constraint(premises[i])]
        compat_premise_ilists.append(compat_premises_ilist)

    out_list = []

    def recurse_form(form_index, inference_premise_ilist=[]):
        if form_index == len(form_constrains):
            inference_wffs = [premises[i] for i in inference_premise_ilist]
            if final_constraint(inference_wffs):
                out_list.append(inference_premise_ilist)
        else:
            compat_premises_ilist = compat_premise_ilists[form_index]
            for prem_i in compat_premises_ilist:
                recurse_form(form_index+1, inference_premise_ilist + [prem_i])
    
    recurse_form(0)
    return out_list
            


            


class ModusPonens(Inference):
    def __init__(self):
        self.form_constrains = [
            lambda wff: True,
            lambda wff: isinstance(wff, ImplWff)
            lambda wffs: wffs[1].left().equals(wffs[0]) # equals: takes care of bound vars with different names, TODO implement this next!
        ]

    def name(self):
        return 'Modus Ponens'

    def short_name(self):
        return 'MP'

    def _apply(self, wffs) -> Tuple[Line, Application]:
        # We need to provide lines and not wffs due to 'rules'
        # such as assumption and discharge
        return wffs[1]

    def possible_conclusions(self, line: Line) -> List[Tuple[Line, Application]]:
        matching_patterns = find_proposional_patterns([
            [line.get_wff() for line in line.premises(),
            lambda wff: True,

            ]    
        ])
        return [self._apply(x) for x in matching_patterns]
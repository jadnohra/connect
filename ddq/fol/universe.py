from abc import ABC, abstractmethod
from .individual import Individual
from .predicate import Predicate
from .function import Function


class Universe:
    def __init__(self):
        self._indiv_id_counter = 0
        self._pred_id_counter = 0
        self._func_id_counter = 0

    def add_individual(self, individual: Individual):
        individual.set_id(self._indiv_id_counter)
        self._indiv_id_counter = self._indiv_id_counter + 1

    def add_predicate(self, predicate: Predicate):
        predicate.set_id(self._pred_id_counter)
        self._pred_id_counter = self._pred_id_counter + 1

    def add_function(self, function: Function):
        function.set_id(self._func_id_counter)
        self._func_id_counter = self._func_id_counter + 1

from abc import ABC, abstractmethod


class Individual:
    def __init__(self, id: str):
        self._id = id

    def id(self) -> str:
        return self._id


class SpecificIndividual(Individual):
    pass


class UniqueIndividual(SpecificIndividual):
    pass


class AssumptionIndividual(Individual):
    pass


class ArbitraryIndividual(Individual):
    pass


class Universe:
    def __init__(self):
        self._id_counter = 0

    def new_individual(self, individual_class: Individual):
        yield individual_class("id_{}".format(self._id_counter))
        self._id_counter = self._id_counter + 1

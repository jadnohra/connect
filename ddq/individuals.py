"""
Semantic individuals, used a additional properties of syntactic variables
"""
from .classproperty import classproperty


class Individual:
    @classproperty
    def typename(cls) -> str:
        return "individual"


class ConstantIndividual(Individual):
    @classproperty
    def typename(cls) -> str:
        return "constant individual"


class ExistentialIndividual(Individual):
    @classproperty
    def typename(cls) -> str:
        return "existential individual"


class UniqueExistentialIndividual(ExistentialIndividual):
    @classproperty
    def typename(cls) -> str:
        return "unique existential individual"


class AssumedIndividual(Individual):
    @classproperty
    def typename(cls) -> str:
        return "assumed individual"

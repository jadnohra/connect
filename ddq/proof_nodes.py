from .node import NamedLeafNode, classproperty


class VariableContext:
    def makeFreshVariable():
        pass


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

class ProofNode(NamedLeafNode):
    @classproperty
    def typename(cls) -> str:
        return "proof"


class InferenceNode(NamedLeafNode):
    @classproperty
    def typename(cls) -> str:
        return "inference"


class AssumptionNode(ProofNode):
    @classproperty
    def typename(cls) -> str:
        return "assumption"
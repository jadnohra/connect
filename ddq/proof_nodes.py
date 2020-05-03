from .node import NamedLeafNode, classproperty


class VariableContext:
    def makeFreshVariable():
        pass

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
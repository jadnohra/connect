from ddq.topics.logics.logic import MetaOperator, Formula


class FunctionDefinitionMetaOperator(MetaOperator):
    def symbol(self) -> str:
        return "≜"
    
    def __call__(self, *parameters) -> Formula:
        pass

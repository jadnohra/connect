from ddq.topics.logics.logic import Meta


class FunctionDefinitionMetaOperator(Meta):
    def symbol(self) -> str:
        return "N/A"
    
    def info(self) -> str:
        return "≜"
 
    def __call__(self, *parameters):
        pass

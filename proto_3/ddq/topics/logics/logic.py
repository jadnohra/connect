from ddq.taxonomy.thing import Thing, List
from ddq.topics.topic import Topic


class Logic(Topic):
    pass


class Formula(Thing):
    pass


class Formulator(Thing):
    def symbol(self) -> str:
        pass
    
    def __call__(self, *parameters) -> Formula:
        pass


class MetaFormulator(Formulator):
    pass


class MetaOperator(MetaFormulator):
    pass
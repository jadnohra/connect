from typing import List
from ddq.taxonomy.reference import Reference
from ddq.topics.topic import Topic


class Logic(Topic):
    def references(self) -> List[Reference]:
        return [
            Reference("Classical and Nonclassical Logics", 
                      [("Eric", "Schechter")])
        ]
        
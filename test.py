import unittest
from core.connect2 import *

class TestSave(unittest.TestCase):

    @staticmethod
    def build_small_graph():
        g = Graph()
        n = g.node('test')
        n2 = g.node('test2')
        g.edge(n, n2)
        return g

    def test_dumps(self):
        g = self.build_small_graph()
        dump_string = g.dumps()
        print(dump_string)
        
    def test_dumps_loads(self):
        g = self.build_small_graph()
        dump_string = g.dumps()
        g2 = Graph()
        g2.loads(dump_string)
    #    print(g.__dict__)
    #    print(g2.__dict__)
    #    print(g2.__dict__ == g.__dict__)
        

if __name__ == '__main__':
    unittest.main()
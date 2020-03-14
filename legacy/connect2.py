import collections
import json
from .serialize import JSONEncoder
# TODO: https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable
# TODO: https://docs.python.org/3/library/json.html#json.JSONEncoder.default

#print json.dumps(graph(), default=dumper)

class Graph:
    
    Node = collections.namedtuple('Node', 'id name')
    Edge = collections.namedtuple('Edge', 'id name left right')


    def __init__(self):
        self.node_id_counter = 0
        self.edge_id_counter = 0
        self.node_id_map = {}
        self.edge_id_map = {}
                
        
    def dumps(self):
        def dumper(obj):
            if isinstance(obj, set):
                return list(obj)
            meta_dict = {'__type': type(obj)}
            print(obj)
            print(meta_dict)
            print(type(obj.__dict__))
            #return dict(obj.__dict__, **meta_dict)
            return dict(obj.__dict__, **meta_dict)
        json_string = json.dumps(self, cls=JSONEncoder)
        return json_string
        
    def loads(self, str):
        load_dict = json.loads(str)
        #self.__dict__ = load_dict
        
    def node(self, name):
        node = self.Node(self.gen_node_id(), name)
        self.node_id_map[node.id] = node
        return node
        
    def edge(self, left, right, name=None):
        edge = self.Edge(self.gen_edge_id(), name, left.id, right.id)
        self.edge_id_map[edge.id] = edge
        return edge
                
    def gen_node_id(self):
        self.node_id_counter = self.node_id_counter + 1
        return self.node_id_counter - 1
    
    def gen_edge_id(self):
        self.edge_id_counter = self.edge_id_counter + 1
        return self.edge_id_counter - 1
    

# TODO: https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable
# TODO: https://docs.python.org/3/library/json.html#json.JSONEncoder.default

def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__
#print json.dumps(graph(), default=dumper)

class Singleton:
    def __init__(self, decorated):
        self._decorated = decorated

    def instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)

@Singleton
class Graph:
    
    def __init__(self):
        self._id_map = {}
        self._name_map = {}
        self._id_counter = 0
        
    def default(self, o):
        return o.__dict__

    def add(self, object):
        self._id_map[object._id] = object
        if object.name not in self._name_map:
            self._name_map[object.name] = set()
        self._name_map[object.name].add(object)

    def gen_id(self):
        self._id_counter = self._id_counter + 1
        return self._id_counter - 1
        
    def find(self, name):
        return self._name_map.get(name, None)
        
    def find_one(self, name):
        objects = self.find(name)
        return objects.pop() if objects is not None else None

def graph():
    return Graph.instance()

class Edge:
    def __init__(self, name='', left=None, right=None):
        self._id = graph().gen_id()
        self.name = name
        self.left = left
        if self.left:
            self.left.edges.add(self)
        self.right = right
        if self.right:
            self.right.edges.add(self)
        graph().add(self)
        
    def other(self, one):
        return self.right if one == self.left else \
            (self.left if one == self.right else None)

class Node:
    def __init__(self, name):
        self._id = graph().gen_id()
        self.name = name
        self.edges = set()
        graph().add(self)
        
    def link(self, node, name=''):
        Edge(name=name, left=self, right=node)
    
    def list(self):
        print(' |')
        for e in self.edges:
            other = e.other(self)
            if other is not None:
                print(' - {}'.format(other.name))
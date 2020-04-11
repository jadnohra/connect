import ddq.fol.lang as lang


def print_tree(root, children_func=iter, name_func=str):
    """Pretty print a tree, in the style of gnu tree"""
    
    # Inspired by https://stackoverflow.com/questions/9727673
    
    # prefix components:
    space =  '    '
    branch = '│   '
    # pointers:
    tee =    '├── '
    last =   '└── '
    
    def tree(dir_path, children_func, name_func, prefix: str=''):
        """A recursive generator, given a tree
        will yield a visual tree structure line by line
        with each line prefixed by the same characters
        """    
        contents = children_func(dir_path)
        # contents each get pointers that are ├── with a final └── :
        pointers = [tee] * (len(contents) - 1) + [last]
        for pointer, path in zip(pointers, contents):
            yield prefix + str(pointer) + name_func(path)
            if len(children_func(path)): # extend the prefix and recurse:
                extension = branch if pointer == tee else space 
                # i.e. space because last, └── , above so no more |
                yield from tree(path, children_func, name_func, prefix=prefix+extension)

    print(name_func(root))
    for line in tree(root, children_func, name_func):
        print(line)

def print_class_hierarchy(root_class):
    """Print a class hierarchy"""
    print_tree(root_class, 
               lambda cls: cls.__subclasses__(), 
               lambda cls: cls.__name__)

def main():
    print("\nddq FOL language demo")
    print('\nSyntax Taxonomy\n')
    print_class_hierarchy(lang.Node)

if __name__ == "__main__":
    # execute only if run as a script
    main()
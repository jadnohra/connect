
def print_tree(root, children_func=list, name_func=str):
    """Pretty print a tree, in the style of gnu tree"""

    # prefix components:
    space =  '    '
    branch = '│   '
    # pointers:
    tee =    '├── '
    last =   '└── '

    # Inspired by https://stackoverflow.com/questions/9727673
    def tree(node, children_func, name_func, prefix: str = ''):
        """A recursive generator, given a tree
        will yield a visual tree structure line by line
        with each line prefixed by the same characters
        """
        contents = children_func(node)
        # contents each get pointers that are ├── with a final └── :
        pointers = [tee] * (len(contents) - 1) + [last]
        for pointer, path in zip(pointers, contents):
            yield prefix + str(pointer) + name_func(path)
            if len(children_func(path)):  # extend the prefix and recurse:
                extension = branch if pointer == tee else space
                # i.e. space because last, └── , above so no more |
                yield from tree(path, children_func, name_func,
                                prefix=prefix + extension)

    # Print the resulting tree
    print(name_func(root))
    for line in tree(root, children_func, name_func):
        print(line)

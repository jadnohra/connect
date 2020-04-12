import inspect
import ddq.fol.lang as lang
from ddq.util.print_tree import (
    print_class_hierarchy, print_node_hierarchy)


def main():
    print("\nddq FOL language demo")
    print('\n# Syntax Taxonomy\n')
    print_class_hierarchy(lang.Node)
    print('\n# Canonical Instances')
    all_classes = [obj for (name, obj) in inspect.getmembers(lang) if inspect.isclass(obj)]
    all_symbols = [cls for cls in all_classes if issubclass(cls, lang.Symbol)]
    print('\n## Symbols\n')
    for symbol in all_symbols:
        print("{}: {}".format(symbol.__name__, symbol.canonical_instance().name()))
    print('\n## Terms\n')
    all_terms = [cls for cls in all_classes if issubclass(cls, lang.Term)]
    for term in all_terms:
        print()
        print_node_hierarchy(term.canonical_instance())
    print('\n## Wffs\n')
    all_wffs = [cls for cls in all_classes if issubclass(cls, lang.Wff)]
    for wff in all_wffs:
        print()
        print_node_hierarchy(wff.canonical_instance())


if __name__ == "__main__":
    # execute only if run as a script
    main()
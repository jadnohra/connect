import inspect
from ddq.individuals import Individual
from ddq.wff_nodes import Wff
from ddq.util.print_tree import print_class_hierarchy


def main():
    print("\n# ddq type hierarchies demo")
    print('\n## Semantic individuals\n')
    print_class_hierarchy(Individual)
    print('\n## Wff nodes\n')
    print_class_hierarchy(Wff)
    print()


if __name__ == "__main__":
    # execute only if run as a script
    main()

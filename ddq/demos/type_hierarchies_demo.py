import inspect
from ddq.individuals import Individual
from ddq.util.print_tree import print_class_hierarchy


def main():
    print("\nddq type hierarchies demo")
    print('\n# Semantic individuals\n')
    print_class_hierarchy(Individual)


if __name__ == "__main__":
    # execute only if run as a script
    main()
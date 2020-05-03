import inspect
import ddq.fol.inference as inf
import ddq.fol.prop_inf as prop_inf
from ddq.util.print_tree import (
    print_class_hierarchy, print_node_hierarchy)


def main():
    print("\nddq FOL inferences demo")
    print('\n# Inference Taxonomy\n')
    print_class_hierarchy(inf.Inference)
   

if __name__ == "__main__":
    # execute only if run as a script
    main()
from types import SimpleNamespace
from ddq.fol.topic import FOL
from .empty_set import EmptySetConstantNode, EmptySetAxiom
from .membership import Membership
from .non_membership import NonMembership, NonMembeshipDefinition
from .pairing import PairingAxiom
from .preliminary_union import PreliminaryUnionAxiom
from .subset import Subset, SubsetDefinition


def build_topic(FOL: SimpleNamespace = FOL) -> SimpleNamespace:
    st = SimpleNamespace()
    st.references = [
        ("Elements of Set Theory", "Enderton")
    ]
    st.Empty = EmptySetConstantNode()
    st.In = Membership()
    st.Nin = NonMembership()
    st.NinDefinition = NonMembeshipDefinition(FOL, st).get_formula()
    st.EmptySetAxiom = EmptySetAxiom(FOL, st).get_formula()
    st.PairingAxiom = PairingAxiom(FOL, st).get_formula()
    st.PreliminaryUnionAxiom = PreliminaryUnionAxiom(FOL, st).get_formula()
    st.Subset = Subset()
    st.SubsetDefinition = SubsetDefinition(FOL, st).get_formula()
    return st


ST = build_topic()

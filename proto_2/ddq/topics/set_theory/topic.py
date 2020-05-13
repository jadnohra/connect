from types import SimpleNamespace
from ddq.fol.topic import FOL
from .empty_set import EmptySetConstantNode, EmptySetAxiom
from .membership import Membership
from .non_membership import NonMembership, NonMembeshipDefinition
from .pairing import PairingAxiom
from .preliminary_union import PreliminaryUnionAxiom
from .subset import Subset, SubsetDefinition
from .powerset import Powerset, PowersetDefinition
from .inductive_formation import (
    InductiveFormationInductor,
    InductiveFormationDefinitionInductor)


def build_topic(FOL: SimpleNamespace = FOL) -> SimpleNamespace:
    st = SimpleNamespace()
    st.references = [
        ("Elements of Set Theory", "Enderton")
    ]
    st.Empty = EmptySetConstantNode()
    st.In = Membership()
    st.Nin = NonMembership()
    st.NinDefinition = NonMembeshipDefinition(FOL, st)
    st.EmptySetAxiom = EmptySetAxiom(FOL, st)
    st.PairingAxiom = PairingAxiom(FOL, st)
    st.PreliminaryUnionAxiom = PreliminaryUnionAxiom(FOL, st)
    st.Subset = Subset()
    st.SubsetDefinition = SubsetDefinition(FOL, st)
    st.Powerset = Powerset()
    st.PowersetDefinition = PowersetDefinition(FOL, st)
    st.InductiveFormation = InductiveFormationInductor()
    st.InductiveFormationDefinition = \
        InductiveFormationDefinitionInductor(FOL, st)
    return st


ST = build_topic()

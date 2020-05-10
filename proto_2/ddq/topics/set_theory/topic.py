from types import SimpleNamespace
from ddq.fol.topic import FOL
from .membership import Membership
from .non_membership import NonMembership, NonMembeshipDefinition


def build_topic(FOL: SimpleNamespace = FOL) -> SimpleNamespace:
    st = SimpleNamespace()
    st.references = [
        ("Elements of Set Theory", "Enderton")
    ]
    st.In = Membership()
    st.Nin = NonMembership()
    st.NinDef = NonMembeshipDefinition(FOL, st).get_formula()
    return st


ST = build_topic()

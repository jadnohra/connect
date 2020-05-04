class NamedInstance:
    def __init__(self, name: str = None):
        self._name = name

    def set_name(self, name: str):
        assert self._name is None, "Named instance should not be renamed"
        self._name = name

    def name(self) -> str:
        return self._name


class NameContext:
    def __init__(self, prefix: str = None):
        self._prefix = prefix
        self._name_counter = 0

    def add_instance(self, instance: NamedInstance):
        if self._prefix:
            instance.set_name(str(self._name_counter))
        else:
            instance.set_name(
                    "{}_{}".format(self._prefix, 
                                   self._name_counter))
        self._name_counter = self._name_counter + 1
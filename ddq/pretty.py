from .classproperty import classproperty


class PrettyClass:
    @classproperty
    def typename(cls) -> str:
        pass
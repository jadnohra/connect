from .topic import Topic


class Universe:
    def __init__(self):
        self._topics = {}

    def add_topic(self, topic: Topic, override_name: str = None):
        name = override_name if override_name is not None else topic.get_name()
        assert name not in self._topics, "Topics cannot be overwritten"
        self._topics[name] = topic

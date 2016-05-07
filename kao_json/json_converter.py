from .builders import ListBuilder, ObjectBuilder
from collections.abc import Mapping, Iterable

class JsonConverter:
    """ Represents a converter for a value """
    
    def __init__(self, value, config):
        """ Initialize the Json Converter """
        self.value = value
        self.config = config
        
    def toJson(self, context):
        """ Convert the object to JSON """
        config = self.config.find(type(self.value))
        if config:
            data = config(self.value, context)
            return self.config.newConverter(data).toJson(context)
        elif isinstance(self.value, Mapping):
            return ObjectBuilder(self.value).build(context)
        elif isinstance(self.value, Iterable) and not isinstance(self.value, str):
            return ListBuilder(self.value).build(context)
        else:
            return self.value
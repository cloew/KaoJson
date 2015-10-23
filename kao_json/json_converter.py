from .builders import ListBuilder, ObjectBuilder

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
            return config.convert(self.value, context)
        elif type(self.value) is dict:
            return ObjectBuilder(self.value).build(context)
        elif hasattr(self.value, '__iter__') and type(self.value) not in [dict, str]:
            return ListBuilder(self.value).build(context)
        else:
            return self.value
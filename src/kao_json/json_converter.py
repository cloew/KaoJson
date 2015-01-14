
class JsonConverter:
    """ Represents a converter for an object """
    
    def __init__(self, object, config):
        """ Initialize the Json Converter """
        self.object = object
        self.config = config
        
    def toJson(self, *args, **kwargs):
        """ Convert the object to JSON """
        json = self.object
        if self.object.__class__ in self.config:
            json = {}
            attrs = self.config[self.object.__class__]
            for attr in attrs:
                json[attr.name] = attr.value(self.object, *args, **kwargs)
        return json
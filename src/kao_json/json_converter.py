
class JsonConverter:
    """ Represents a converter for an object """
    
    def __init__(self, object, config):
        """ Initialize the Json Converter """
        self.object = object
        self.config = config
        
    def toJson(self, **kwargs):
        """ Convert the object to JSON """
        return self.converterMethod(**kwargs)
        
    @property
    def converterMethod(self):
        """ Return the proper converter method """
        if type(self.object) == list:
            return self.convertList
        elif self.object.__class__ in self.config:
            return self.convertObject
        else:
            return self.convertPrimitive
        
    def newConverter(self, object):
        """ Return a new converter object """
        return JsonConverter(object, self.config)
        
    def convertList(self, **kwargs):
        """ Convert a list to JSON """
        return [self.newConverter(e).toJson(**kwargs) for e in self.object]
        
    def convertObject(self, **kwargs):
        """ Convert an object to JSON """
        json = {}
        attrs = self.config[self.object.__class__]
        for attr in attrs:
            args = [kwargs[arg] for arg in attr.args]
            value = attr.value(self.object, *args)
            json[attr.name] = self.newConverter(value).toJson(**kwargs)
        return json
        
    def convertPrimitive(self, **kwargs):
        """ Convert a primitive to JSON """
        return self.object
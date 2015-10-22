import inspect

class JsonConverter:
    """ Represents a converter for an object """
    
    def __init__(self, object, config):
        """ Initialize the Json Converter """
        self.object = object
        self.config = config
        self.objectConfig = None
        
    def toJson(self, **kwargs):
        """ Convert the object to JSON """
        return self.converterMethod(**kwargs)
        
    @property
    def converterMethod(self):
        """ Return the proper converter method """
        if self.findConfig(self.object.__class__):
            return self.convertObject
        elif type(self.object) is dict:
            return self.convertDictionary
        elif hasattr(self.object, '__iter__') and type(self.object) not in [dict, str]:
            return self.convertList
        else:
            return self.convertPrimitive
            
    def findConfig(self, cls):
        """ Find the config by searching if the object class or any of its parents have been registered """
        for currentClass in [cls] + list(inspect.getmro(cls)):
            if currentClass in self.config:
                self.objectConfig = self.config[currentClass]
                break
        return self.objectConfig is not None
        
    def newConverter(self, object):
        """ Return a new converter object """
        return JsonConverter(object, self.config)
        
    def convertList(self, **kwargs):
        """ Convert a list to JSON """
        return [self.newConverter(e).toJson(**kwargs) for e in self.object]
        
    def convertDictionary(self, **kwargs):
        """ Convert a dictionary to JSON """
        return {key:self.newConverter(value).toJson(**kwargs) for key, value in self.object.items()}
        
    def convertObject(self, **kwargs):
        """ Convert an object to JSON """
        json = {}
        kwargs = self.objectConfig.getKwargs(kwargs)
        for attr in self.objectConfig.getAttrs(self.object, kwargs, self.config): # self.objectConfig set during findConfig
            args = [kwargs[arg] for arg in attr.args]
            value = attr.value(self.object, *args)
            newKwargs = self.getKwargsForNextConverter(attr, kwargs)
            json[attr.name] = self.newConverter(value).toJson(**newKwargs)
        return json
        
    def convertPrimitive(self, **kwargs):
        """ Convert a primitive to JSON """
        return self.object
        
    def getKwargsForNextConverter(self, attr, kwargs):
        """ Return the Keyword arguments to use in the next Json Converter """
        newKwargs = kwargs
        if attr.extraArgsProvider:
            newKwargs = dict(kwargs)
            newKwargs.update(attr.extraArgsProvider(self.object, kwargs))
        return newKwargs
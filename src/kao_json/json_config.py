
class JsonConfig:
    """ Represents an object's configuration for transforming to JSON """
    
    def __init__(self, objectClass, attrs, optionalKwargs=None):
        """ Initialize the Json Config """
        self.objectClasses = objectClass
        if type(objectClass) != list:
            self.objectClasses = [objectClass]
        
        self.attrs = attrs
        self.inheritFromClass = None
        self.optionalKwargs = optionalKwargs
        
    def addConfig(self, classToConfig):
        """ Add this config to the class to Config dictionary used by the Json Factory """
        for cls in self.objectClasses:
            classToConfig[cls] = self
            
    def inheritFrom(self, cls, ignore=[]):
        """ Tell this configuration to use the same attrs from the given class' configuration """
        self.inheritFromClass = cls
        self.ignoreInheritedAttrs = set(ignore)
        return self
        
    def getAttrs(self, object, kwargs, classToConfig):
        """ Return the attributes used for this object's config """
        attrs = []
        if self.inheritFromClass:
            attrs = [attr for attr in classToConfig[self.inheritFromClass].getAttrs(object, classToConfig) if attr.name not in self.ignoreInheritedAttrs]
        return attrs + self.attrs
        
    def getKwargs(self, kwargs):
        """ Return the attributes used for this object's config """
        newKwargs = kwargs
        if self.optionalKwargs:
            newKwargs = dict(kwargs)
            for key in self.optionalKwargs:
                if key not in kwargs:
                    newKwargs[key] = self.optionalKwargs[key]
        return newKwargs
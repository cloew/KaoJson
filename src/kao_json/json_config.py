
class JsonConfig:
    """ Represents an object's configuration for transforming to JSON """
    
    def __init__(self, objectClass, attrs):
        """ Initialize the Json Config """
        self.objectClasses = objectClass
        if type(objectClass) != list:
            self.objectClasses = [objectClass]
        
        self.attrs = attrs
        self.inheritFromClass = None
        
    def addConfig(self, classToConfig):
        """ Add this config to the class to Config dictionary used by the Json Factory """
        for cls in self.objectClasses:
            classToConfig[cls] = self
            
    def inheritFrom(self, cls):
        """ Tell this configuration to use the same attrs from the given class' configuration """
        self.inheritFromClass = cls
        return self
        
    def getAttrs(self, classToConfig):
        """ Return the attributes used for this object's config """
        attrs = []
        if self.inheritFromClass:
            attrs = classToConfig[self.inheritFromClass]
        return attrs + self.attrs
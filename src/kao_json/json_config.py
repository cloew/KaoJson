
class JsonConfig:
    """ Represents an object's configuration for transforming to JSON """
    
    def __init__(self, objectClass, attrs):
        """ Initialize the Json Config """
        self.objectClasses = objectClass
        if type(objectClass) != list:
            self.objectClasses = [objectClass]
        self.attrs = attrs
        
    def addConfig(self, classToConfig):
        """ Add this config to the class to Config dictionary used by the Json Factory """
        for cls in self.objectClasses:
            classToConfig[cls] = self
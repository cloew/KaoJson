
class JsonAttribute:
    """ Represents a Json field attribute """
    
    def __init__(self, name, resultMethod):
        """ Initialize the JSON Attribute with its name and field to access """
        self.name = name
        self.resultMethod = resultMethod
        
    def value(self, object, *args, **kwargs):
        """ Return the value of this attribute """
        return self.resultMethod(object, *args, **kwargs)
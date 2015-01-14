
class JsonAttr:
    """ Represents a Json field attribute """
    
    def __init__(self, name, resultMethod, args=[]):
        """ Initialize the JSON Attribute with its name and field to access """
        self.name = name
        self.resultMethod = resultMethod
        self.args = args
        
    def value(self, object, *args):
        """ Return the value of this attribute """
        return self.resultMethod(object, *args)
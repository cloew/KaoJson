
class JsonAttr:
    """ Represents a Json field attribute """
    
    def __init__(self, name, resultMethod, args=[], extraArgsProvider=None):
        """ Initialize the JSON Attribute with its name and field to access """
        self.name = name
        self.resultMethod = resultMethod
        self.args = args
        self.extraArgsProvider = extraArgsProvider
        
    def value(self, object, *args):
        """ Return the value of this attribute """
        return self.resultMethod(object, *args)
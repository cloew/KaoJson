from .json_attr import JsonAttr

class StaticAttr(JsonAttr):
    """ Represents a static attribute for a Json Object """
    
    def __init__(self, name, value):
        """ Initialize the Static Attribute """
        JsonAttr.__init__(self, name, self._getValue)
        self._value = value
        
    def _getValue(self, object, *args):
        """ Return the value of this attribute """
        return self._value
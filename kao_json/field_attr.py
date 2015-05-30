from json_attr import JsonAttr
from operator import attrgetter

class FieldAttr(JsonAttr):
    """ Represents a attribute that is a field on the requested object """
    
    def __init__(self, name, field=None, extraArgsProvider=None):
        """ Initialize the field attribute """
        if field is None:
            field = name
        self.field = field
        JsonAttr.__init__(self, name, self.getFieldValue, extraArgsProvider=extraArgsProvider)
        
    def getFieldValue(self, object):
        """ Return the field attribute for the given object """
        value = object
        for fieldName in self.field.split('.'):
            value = getattr(value, fieldName)
        return value
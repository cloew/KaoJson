from json_attr import JsonAttr
from operator import attrgetter

class FieldAttr(JsonAttr):
    """ Represents a attribute that is a field on the requested object """
    
    def __init__(self, name, field=None, extraArgsProvider=None):
        """ Initialize the field attribute """
        if field is None:
            field = name
        JsonAttr.__init__(self, name, attrgetter(field), extraArgsProvider=extraArgsProvider)
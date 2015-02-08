from json_converter import JsonConverter
from json_attr import JsonAttr

class JsonFactory:
    """ Represents factory to convert objects to JSON """
    
    def __init__(self, config):
        """ Initialize the Json Factory """
        self.classToConfig = {}
        for key, value in config:
            if type(key) == list:
                for newKey in key:
                    self.classToConfig[newKey] = value
            else:
                self.classToConfig[key] = value
        
    def converterFor(self, object):
        """ Convert the provided object """
        return JsonConverter(object, self.classToConfig)
        
    def toJson(self, object, **kwargs):
        return self.converterFor(object).toJson(**kwargs)
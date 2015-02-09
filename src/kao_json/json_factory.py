from json_config import JsonConfig
from json_converter import JsonConverter
from json_attr import JsonAttr

class JsonFactory:
    """ Represents factory to convert objects to JSON """
    
    def __init__(self, configs):
        """ Initialize the Json Factory """
        self.classToConfig = {}
        for config in configs:
            if not config.__class__ is JsonConfig:
                config = JsonConfig(config[0], config[1])
            config.addConfig(self.classToConfig)
        
    def converterFor(self, object):
        """ Convert the provided object """
        return JsonConverter(object, self.classToConfig)
        
    def toJson(self, object, **kwargs):
        return self.converterFor(object).toJson(**kwargs)
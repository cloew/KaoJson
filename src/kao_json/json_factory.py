from json_converter import JsonConverter
from json_attr import JsonAttr

class JsonFactory:
    """ Represents factory to convert objects to JSON """
    
    def __init__(self, config):
        """ Initialize the Json Factory """
        # if type(list) not in config:
            # config[type(list)] = JsonAttr()
        self.classToConfig = config
        
    def converterFor(self, object):
        """ Convert the provided object """
        return JsonConverter(object, self.classToConfig)
from json_converter import JsonConverter

class JsonFactory:
    """ Represents factory to convert objects to JSON """
    
    def __init__(self, config):
        """ Initialize the Json Factory """
        self.classToConfig = config
        
    def converterFor(self, object):
        """ Convert the provided object """
        return JsonConverter(object, self.classToConfig)
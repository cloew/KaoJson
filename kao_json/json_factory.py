from .conversion_config import ConversionConfig
from .conversion_context import ConversionContext

class JsonFactory:
    """ Represents factory to convert objects to JSON """
    
    def __init__(self, *configs):
        """ Initialize the Json Factory """
        self.config = ConversionConfig(configs)
        
    def toJson(self, object, **kwargs):
        context = ConversionContext(self.config, **kwargs)
        return context.newConverter(object).toJson(context)
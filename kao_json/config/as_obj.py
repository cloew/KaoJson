from ..builders import ObjectBuilder

class AsObj:
    """ Represents an object's configuration for transforming to a JSON Object """
    
    def __init__(self, **providers):
        """ Initialize with the providers """
        self.providers = providers
        
    def convert(self, value, context):
        """ Convert the Object Config in the given context """
        values = {key:provider(value) for key, provider in self.providers.items()}
        return ObjectBuilder(values).build(context)
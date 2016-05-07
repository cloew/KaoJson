from ..builders import ObjectBuilder

class AsObj:
    """ Represents an object's configuration for transforming to a JSON Object """
    
    def __init__(self, **providers):
        """ Initialize with the providers """
        self.providers = providers
        
    def __call__(self, value, context):
        """ Convert the Object Config in the given context """
        return {key:provider(context.providerContext(key, value)) for key, provider in self.providers.items()}
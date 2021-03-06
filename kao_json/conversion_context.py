from .providers import ProviderContext
from kao_decorators import proxy_for

@proxy_for('config', ['newConverter'])
class ConversionContext:
    """ Represents the Configuration and Keyword Arguments provided to a Converter """
    
    def __init__(self, config, **kwargs):
        """ Initialize with the config and keyword arguments """
        self.config = config
        self.kwargs = kwargs
        
    def providerContext(self, name, obj):
        """ Return a Provider Context """
        return ProviderContext(name, obj, self.kwargs)
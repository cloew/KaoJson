from .json_converter import JsonConverter

from kao_decorators import proxy_for
import inspect

@proxy_for('configs', ['__contains__', '__iter__', '__len__'])
class ConversionConfig:
    """ Represents the Conversion Configuration for a Json Factory """
    
    def __init__(self, configs):
        """ Initialize with the configs to wrap """
        self.config = {cls:config for config in configs for cls in config.objectClasses}
        
    def find(self, cls):
        """ Return the config for the given class """
        for currentClass in self._classesToCheck(cls):
            if currentClass in self.config:
                return self.config[currentClass]
        else:
            return None
        
    def _classesToCheck(self, cls):
        """ Generator to return the classes to check """
        yield cls
        yield from inspect.getmro(cls)
        
    def newConverter(self, value):
        """ Return a new Converter for the given value """
        return JsonConverter(value, self)
from .iter_wrapper import IterWrapper
from .json_converter import JsonConverter

from kao_decorators import proxy_for
import inspect

@proxy_for('config', ['__contains__', '__iter__', '__len__'])
class ConversionConfig:
    """ Represents the Conversion Configuration for a Json Factory """
    
    def __init__(self, configGroups):
        """ Initialize with the configs to wrap """
        self.config = {cls:configGroup[classes] for configGroup in configGroups for classes in configGroup for cls in IterWrapper(classes)}
        
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
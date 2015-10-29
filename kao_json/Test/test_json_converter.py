from .class_hierarchy import A, AChild, AGrandchild

from ..conversion_config import ConversionConfig
from ..conversion_context import ConversionContext
from ..json_converter import JsonConverter
from ..config import AsObj
from ..providers import ViaAttr

from operator import attrgetter
import unittest

class toJson(unittest.TestCase):
    """ Test cases of toJson """
        
    def test_dict(self):
        """ Test that a dictionary value is returned properly """
        values = {'one':A(1),'two':AChild(2),'three':AGrandchild(3)}
        expected = {key:{'value':a.value} for key, a in values.items()}
        
        config = ConversionConfig([{A:AsObj(value=attrgetter('value'))}])
        context = ConversionContext(config)
        converter = JsonConverter(expected, config)
        
        actual = converter.toJson(context)
        
        self.assertEqual(expected, actual)
        
    def test_iterable(self):
        """ Test that an iterable value is returned properly """
        value = (A(1), A(2), A(3))
        expected = [{'value':a.value} for a in value]
        
        config = ConversionConfig([{A:AsObj(value=ViaAttr())}])
        context = ConversionContext(config)
        converter = JsonConverter(value, config)
        
        actual = converter.toJson(context)
        
        self.assertEqual(expected, actual)
        
    def test_primitive(self):
        """ Test that a primitive value is returned properly """
        expected = 1
        config = ConversionConfig([])
        context = ConversionContext(config)
        converter = JsonConverter(expected, config)
        
        actual = converter.toJson(context)
        
        self.assertEqual(expected, actual)
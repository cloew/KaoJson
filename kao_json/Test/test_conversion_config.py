from .class_hierarchy import A, AChild, AGrandchild
from ..conversion_config import ConversionConfig
import unittest


class find(unittest.TestCase):
    """ Test cases of find """
        
    def test_matchingClassFound(self):
        """ Test that a matching class is found properly """
        expected = "Dummy Config..."
        config = ConversionConfig([{A:expected}])
        
        actual = config.find(A)
        self.assertEqual(expected, actual)
        
    def test_descendantClassFound(self):
        """ Test that a matching descendant class is found properly """
        expected = "Dummy Config..."
        config = ConversionConfig([{A:expected}])
        
        actual = config.find(AGrandchild)
        self.assertEqual(expected, actual)
        
    def test_noMatchFound(self):
        """ Test that when no match is found, None is returned """
        config = ConversionConfig([])
        self.assertIsNone(config.find(A))

class newConverter(unittest.TestCase):
    """ Test cases of newConverter """
        
    def test_converterBuilt(self):
        """ Test that the Converter was built properly """
        value = "Dummy Value..."
        config = ConversionConfig([])
        converter = config.newConverter(value)
        
        self.assertEqual(converter.value, value)
        self.assertEqual(converter.config, config)
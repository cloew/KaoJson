from ..conversion_config import ConversionConfig
from ..json_config import JsonConfig
import unittest

class A:
    pass
class AChild(A):
    pass
class AGrandchild(AChild):
    pass

class find(unittest.TestCase):
    """ Test cases of find """
        
    def test_matchingClassFound(self):
        """ Test that a matching class is found properly """
        expected = JsonConfig([A], [])
        config = ConversionConfig([expected])
        
        actual = config.find(A)
        self.assertEqual(expected, actual)
        
    def test_descendantClassFound(self):
        """ Test that a matching descendant class is found properly """
        expected = JsonConfig([A], [])
        config = ConversionConfig([expected])
        
        actual = config.find(AGrandchild)
        self.assertEqual(expected, actual)
        
    def test_noMatchFound(self):
        """ Test that when no match is found, None is returned """
        config = ConversionConfig([])
        self.assertIsNone(config.find(A))
from ..provider_context import ProviderContext
from ..via_attr import ViaAttr
import unittest

class A:
    def __init__(self, value):
        self.value = value

class call(unittest.TestCase):
    """ Test cases of call """
        
    def test_attr(self):
        """ Test that the attribute is retrieved """
        expected = 12
        a = A(expected)
        context = ProviderContext('value', a, {})
        provider = ViaAttr()
        
        actual = provider(context)
        self.assertEqual(expected, actual)
        
    def test_differentName(self):
        """ Test that the attribute is retrieved when the destination attr is different """
        expected = 12
        a = A(expected)
        context = ProviderContext('not value', a, {})
        provider = ViaAttr('value')
        
        actual = provider(context)
        self.assertEqual(expected, actual)
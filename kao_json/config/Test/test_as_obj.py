from ..as_obj import AsObj
import unittest
from unittest.mock import Mock, patch

class call(unittest.TestCase):
    """ Test cases of call """
        
    def test_providersUsed(self):
        """ Test that the Providers are used """
        d = {}
        expectedValues = {}
        for i in range(5):
            key = 'test{0}'.format(i)
            value = Mock(return_value=i)
            d[key] = value
            expectedValues[key] = i
            
        value = "Dummy Value..."
        context = Mock()
        
        config = AsObj(**d)
        actual = config(value, context)
        
        for key, provider in d.items():
            context.providerContext.assert_any_call_with(key, value)
            provider.assert_called_once_with(context.providerContext.return_value)
        self.assertEqual(expectedValues, actual)
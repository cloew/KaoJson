from ..as_obj import AsObj
import unittest
from unittest.mock import Mock, patch

class convert(unittest.TestCase):
    """ Test cases of convert """
        
    @patch('kao_json.config.as_obj.ObjectBuilder')
    def test_providersUsed(self, ObjectBuilderMock):
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
        expected = ObjectBuilderMock.return_value.build.return_value
            
        config = AsObj(**d)
        
        
        actual = config.convert(value, context)
        
        for key, provider in d.items():
            context.providerContext.assert_any_call_with(key, value)
            provider.assert_called_once_with(context.providerContext.return_value)
            
        ObjectBuilderMock.assert_called_once_with(expectedValues)
        ObjectBuilderMock.return_value.build.assert_called_once_with(context)
        self.assertEqual(expected, actual)
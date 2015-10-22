from ..list_builder import ListBuilder
import unittest
from unittest.mock import Mock

class build(unittest.TestCase):
    """ Test cases of build """
        
    def test_valuesConverted(self):
        """ Test that the values are converted using the context """
        values = [1, 2, 3, 4]
        expected = [5,6,7,8]
        context = Mock()
        context.newConverter.return_value.toJson = Mock(side_effect=expected)
        
        builder = ListBuilder(values)
        results = builder.build(context)
        
        for i, value in enumerate(values):
            context.newConverter.assert_any_call_with(value)
            context.newConverter.return_value.toJson.assert_any_call_with(context)
            
            self.assertEqual(expected[i], results[i])
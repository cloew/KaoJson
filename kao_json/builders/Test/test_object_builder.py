from ..object_builder import ObjectBuilder
import unittest
from unittest.mock import Mock

class build(unittest.TestCase):
    """ Test cases of build """
        
    def test_valuesConverted(self):
        """ Test that the values are converted using the context """
        context = Mock()
        values = {1:1, 2:2, 3:3, 4:4}
        
        builder = ObjectBuilder(values)
        results = builder.build(context)
        
        for key, value in values.items():
            context.newConverter.assert_any_call_with(value)
            context.newConverter.return_value.toJson.assert_any_call_with(context)
            
            self.assertIn(key, results)
            self.assertEqual(context.newConverter.return_value.toJson.return_value, results[key])
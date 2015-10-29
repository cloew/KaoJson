from ..provider_context import ProviderContext
from ..via_fn import ViaFn

import unittest
from unittest.mock import Mock

class call(unittest.TestCase):
    """ Test cases of call """
        
    def test_fnCalled(self):
        """ Test that the function was called """
        expected = "Expected Result"
        obj = Mock()
        fn = Mock(return_value=expected)
        context = ProviderContext('', obj, {})
        provider = ViaFn(fn)
        
        actual = provider(context)
        
        fn.assert_called_once_with(obj)
        self.assertEqual(expected, actual)
        
    def test_argsRequired(self):
        """ Test that the function was called """
        expected = "Expected Result"
        obj = Mock()
        argNames = ['key1', 'key2', 'key3']
        args = {}
        
        for i, name in enumerate(argNames):
            args[name] = i+1
        
        fn = Mock(return_value=expected)
        context = ProviderContext('', obj, args)
        provider = ViaFn(fn, requires=argNames)
        
        actual = provider(context)
        
        fn.assert_called_once_with(obj, *[args[name] for name in argNames])
        self.assertEqual(expected, actual)
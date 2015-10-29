from ..iter_wrapper import IterWrapper
import unittest

class IterValueTest(unittest.TestCase):
    """ Test cases of IterValue """
        
    def test_iterable(self):
        """ Test that an iterable is returned properly """
        expected = [1,2,3]
        actual = IterWrapper(expected)
        
        self.assertEqual(expected, actual)
        
    def test_nonIterable(self):
        """ Test that a non-iterable is returned properly """
        expected = 1
        actual = IterWrapper(expected)
        
        self.assertEqual(len(actual), 1)
        self.assertIn(expected, actual)
import unittest
import doctest

from primes import is_prime

#Any function beginning w/ test will be called
class SndTestClass(unittest.TestCase):
    # Each class method needs to pass in self
    def test_basic(self):
        a = input('1st value: ')
        b = input('2nd value: ')
        self.assertEqual(a,b,"NAH BRUH")

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        pass
        self.assertTrue(is_prime(5))
        '''
        try:
            self.assertTrue(is_prime(5))
        except Exception as err:
            print ("Exception is :", str(err))
        '''
    def test_equals(self):
        #self.assertEqual("b", "a")
        raise RuntimeError('TIME TO RUN!')

    # test edge cases
    def test_edge_cases(self,a,b):
        # Use doctest
        return a*b

    def my_function(a, b):
        """
        >>> my_function(2, 3)
        6
        >>> my_function('a', 3)
        'aaa'
        """
        return a * b

if __name__ == '__main__':
    # unittest main finds all functions prefixed w/ test
    #unittest.main()
    doctest.main()
    pass

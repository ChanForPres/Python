import unittest
import re
import doctest

 # regex,unitest,doctest,multi-inheritance, webscraping

class Object_to_use():
        def __init__(self, result):
            self.result = result

class Reg_tests(unittest.TestCase):

    def __init__(self, result):
        self.result = result

    def test_txt_matcher(self):
        """Returns a dictionary grouping words into sets by length.
        >>> txt_matcher('hunny',"got some bunnies hunny")
        from 17 to 22
        """
        pattern = 'hunny'
        text = "got some bunnies hunny"
        match = re.search(pattern,text)
        s = match.start() # print start index
        e = match.end() # print end index
        #print('from {} to {}'.format (s, e))
        ret_str = 'from {} to {}'.format (s, e)
        print(ret_str)
        #result = 'from 17 to 22'
        self.assertMultiLineEqual(ret_str,self.result )


def main():

    pattern = 'hunny'
    text = "got some bunnies hunny"
    cmp_str = test_txt_matcher(pattern,text)
    result = 'from 17 to 22'
    reg_obj = Reg_tests('from 17 to 22')

    reg_obj.test_txt_matcher()
#    unittest.TestCase.assertEqual(txt_matcher(pattern,text),result)
#    unittest.TestCase.assertMultiLineEqual(cmp_str,result )

if __name__ == '__main__':
    unittest.main()

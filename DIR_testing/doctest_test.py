import doctest
import collections

class ObjTest():
    pass
'''
# ID's change because loaded into different part of memory
def newVal(val):
    """
    >>> newVal(ObjTest()) #doctest: +ELLIPSIS
    [<doctest_test.ObjTest object at 0x...>]
    """
    return [val]
'''
def group_by_length(words):
    """Returns a dictionary grouping words into sets by length.

    >>> grouped = group_by_length([ 'python', 'module', 'of',
    ... 'the', 'week' ])
    >>> grouped == { 2:set(['of']),
    ...              3:set(['the']),
    ...              4:set(['week']),
    ...              6:set(['python', 'module']),
    ...              }
    True

    """
    d = collections.defaultdict(set)
    for word in words:
        d[len(word)].add(word)
    return d

def main():
    print(multiply(1,2))
    print('IN MAIN')

if __name__ == '__main__':
    main()

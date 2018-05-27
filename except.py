
import os
import sys


def dum_add(x,y):

    try:
        # add string and num
        x + y

    except TypeError:
        # catch error
        print('Can\'t add diff types')

    except:
        print('')

def main():
    dum_add('',1)

if __name__ == '__main__':
    main()

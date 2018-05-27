#! /usr/local/bin/python3

import sys #to pass cmd line args
import pexpect
from pexpect import pxssh
import time
import getpass # retrieves password w/o being informed
import logging

logger = logging.getLogger()  #logger object
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')


def adder(x,y):
    logging.debug('Start Adder: ')

    logging.debug(x+y) #launch debug

def mult(x,y):
    logging.debug('Start Mult: ')

    logging.debug(x*y)

def main():
    # log prints error to another file
    logging.debug("Start of program: ")
    open('myLog.log', 'w').close()
    file_handler = logging.FileHandler('myLog.log')
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)


    x = int(input("Enter X value: "))
    assert x >= 0, "ILLEGAL x is less than 0"  #ILLEGAL x<0

    y = int(input("Enter Y value: "))
    assert y >= 0, "ILLEGAL:Y<0" #ILLEGAL y<0


    adder(x,y) #test func
    mult(x,y)



if __name__ == "__main__":
    main()


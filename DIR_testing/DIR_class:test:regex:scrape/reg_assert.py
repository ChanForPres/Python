# assert webpage matches "www.*.com"
import re
import sys
import os
import unittest
import doctest
import inherit

def multimatch(site_ex):
    pattern = 'w'
    text = site_ex.site



def site_regex(site_ex):
    pattern = 'www'
    text = site_ex.site
    match = re.search(pattern,text)
    s = match.start() # print start index
    e = match.end() # print end index
    #print('from {} to {}'.format (s, e))
    ret_str = 'from {} to {}'.format (s, e)

    #unittest.TestCase.assertMultiLineEqual()

    print(site_ex.site)
    print(ret_str)

lst_choice = [str(i) for i in range(1,3,1)] # site options

try:
    choice = input("1) SOCIAL 2) SPORTS\n")
except Exception as err:
    print("ERROR: " + str(err))

assert choice in lst_choice, str(choice) +' IS NOT AN OPTION'
print("INPUT GOOD")

if choice == 1:
    #SOCIAL
    obj_social = inherit.Social()
    site_regex(obj_social)

elif choice == 2:
    #SPORTS
    obj_sport = inherit.Sports()
    site_regex(obj_sport)

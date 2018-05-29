#! python3
# https://www.w3.org/People/Raggett/book4/ch02.html




import sys, os
import requests
from bs4 import BeautifulSoup

# open empty file
#text_file = open('NEW_TEXT.txt','w').close()
#text_file.truncate()
res = requests.get('https://www.w3.org/People/Raggett/book4/ch02.html') # read in html from site
#always check for request failure

try:
    text_file = open('NEW_TEXT.txt','w') # truncate + binary mode
except Exception as err:
    print("FILE OPEN ERROR: " + err)

lines = tuple(res.text)

res.raise_for_status()
assert res.status_code == requests.codes.ok,"UNABLE TO ACCESS WEBPAGE"

count = 0
# read 10% of file
# while x < len(res.text)/10:

for line in res.text:
    if count == int(len(res.text)/10):
        break
    else:
        #write to file
        text_file.write(line)
        count +=1


# Create soup object
soup_obj = BeautifulSoup(res.text,'html.parser')

# Choose element
p_elem = soup_obj.select('p')
h3_elem = soup_obj.select('h3')
h1_elem=soup_obj.select('h1')
h2_elem=soup_obj.select('h2')
li_elem=soup_obj.select('li')
ul_elem=soup_obj.select('ul')
title_elem=soup_obj.select('title')
body_elem=soup_obj.select('body')
# add soup attrs to dict html_attrs

#create dictionary from elements
file_items = {}
file_items['p_elem'] = p_elem


# parse file into paragraphs/titles/dates

# parse w/o headers

try:
    clean_text = open('CLEAN_TEXT.txt','w') # truncate + binary mode
except Exception as err:
    print("FILE OPEN ERROR: " + err)

i = (len(p_elem))
iter_elem = 0

for line in p_elem :
    if iter_elem < i:
        #text_file.write(line)
        clean_text.write(p_elem[iter_elem].getText())
        iter_elem +=1
    else:
        break

# write attributes to file
    try:
        attr_text = open('ATTR_TEXT.txt','w') # truncate + binary mode
    except Exception as err:
        print("FILE OPEN ERROR: " + err)

for line in p_elem:
    if iter_elem < i:
        attr_text.write(p_elem[iter_elem].attrs)
        iter_elem +=1
    else:
        break

text_file.close()

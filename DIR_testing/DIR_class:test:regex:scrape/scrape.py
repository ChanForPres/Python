import webbrowser, sys, requests, bs4
from bs4 import BeautifulSoup
 # webbrowser.open('https://www.google.com')

# get sys-args

print(sys.argv)

for i in sys.argv:
    print(i)

print( "\n".join(sys.argv) )
print( len(sys.argv) )





if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])

print(address)
print(sys.argv[0:len(sys.argv)])

#webbrowser.open(sys.argv[1])

r = requests.get('https://github.com/')
#r = requests.get('https://www.google.com')

print(r.status_code)

# POST request
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
print(r.status_code)

r = requests.head('http://httpbin.org/get')
r = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(r.status_code)

# checks for file download error
try:
    r.raise_for_status()
except Exception as err:
    print('There was a problem: %s' % (err))

payload = {'key1': 'value1', 'key2': 'value2'}

# already created file
data_file = open('request.txt','w')
for line in r.text:
    data_file.write(line) #write to file
data_file.close()

# create new file
new_file = open('DataFile.txt','wb')
# iter.content ensures large files don't overwrite memory
for line in r.iter_content(100000):
    new_file.write(line)
new_file.close()

#beautiful soup
print('=========================================================================================================')
#soup_match = bs4.BeautifulSoup(r.text)
#type(soup_match)
print('=========================================================================================================')
quote_page = 'http://www.bloomberg.com/quote/SPX:IND'
new_page = requests.get(quote_page) # get html of page
new_page.raise_for_status()
soup_var = BeautifulSoup(new_page.text)# parse html using BeautifulSoup
type(soup_var)

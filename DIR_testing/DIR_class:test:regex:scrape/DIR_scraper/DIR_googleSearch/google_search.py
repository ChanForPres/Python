import requests,webbrowser,sys
from bs4 import BeautifulSoup


#parse through google search results

def search():

    # https://www.google.com/search?q=SEARCH_TERM_HERE.
    url = "https://www.google.com/search?q="
    # always except when getting input
    try:
        term = input('SEARCH CONTENT: ')
    except Exception as err:
        print('ERROR' + str(err))

    url = url+''.join(term)
    print(url)
    # request WEBPAGE
    # res = requests.get('https://www.w3.org/People/Raggett/book4/ch02.html') # read in html from site

    search_page = requests.get(url)
    search_page.raise_for_status() #check valid url
    assert search_page.status_code==requests.codes.ok, "INVALID URL"

    # create BeautifulSoup object
    soup_obj = BeautifulSoup(search_page.text,'html.parser')
    assert soup_obj!=None,'SOUP CREATION FAILURE '

    # parse 5 urls
    # <a href="... " >
    # walk DOM tree until reach <h3>

    header_list = soup_obj.find_all("h3 class=")
    url_list = soup_obj.find_all("a href=/" )
    linkElems = soup_obj.select('.r a')

    str(linkElems).split(',') # split URLs by comma
    # open 5 results in new tabs

    # ' <a class="sla" href="/url?q=
    # https://www.apple.com/iphone/&amp;sa=U&amp;ved=0ahUKEwig1-_zzavbAhVRLX0KHU1_DlEQjBAIJzAB&amp;usg=AOvVaw26p1
    # _W8EaMi3X2JtriJ1h9">iPhone</a>'


    # extract from href="/url?q=" ... ">
    print(url)
    for i in linkElems:
        print(url + str(i.get("href")) )
        webbrowser.open( 'http://google.com' + i.get("href") )

def main():
    search()

if __name__ == '__main__':
    main()

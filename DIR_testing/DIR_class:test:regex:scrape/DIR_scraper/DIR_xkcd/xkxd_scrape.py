# https://xkcd.com/archive/

import requests, sys,webbrowser
from bs4 import BeautifulSoup



def comic_get():

    try:
        input("") # how many comics to download
    except Exception as err:
        print("EXCEPTION " + str(err))

    # request site
    req_obj = requests.get('https://xkcd.com/archive/'')
    req_obj.raise_for_status() # test valid URL


    # init BeautifulSoup object to parse
    soup_obj = BeautifulSoup(req_obj.text,'html.parser')
    assert soup_obj.status_code==requests.codes.ok, "SOUP CANNOT BE CREATED"

    # get link
    comic_links = soup_obj.get('.r a')

    for i in comic_links:
        print('https://xkcd.com/archive/' + i.get('href') ) # retrieve comic url
        #webbrowser.open('https://xkcd.com/archive/' + i.get('href') ) # retrieve comic url


    # create sub folder for every 10 years

    # download image to file


def main():
    comic_get()

if __name__ == '__main__':
    main()

#multiinheritance

'''
Data: Url , wordcount, popular words, imagecount
'''
#types of pages to scrape
class Webpage(object):
    """docstring for ."""

    def __init__(self):
        self.site = input("ENTER SITE: ")
        print('PARENT SITE: ', self.site)

class Social(Webpage):
    """docstring for ."""
    def __init__(self):
        super().__init__()
        print('SOCIAL SITE: ', self.site)


class Sports(Webpage):
    """docstring for ."""
    def __init__(self):
        super().__init__()
        print('SOCIAL SITE: ', self.site)

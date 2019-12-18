import requests
from bs4 import BeautifulSoup
import pprint
import urllib

class scraper:
    def __init__(self, url):
        self.url = url
        self.reqs = self.checkURL(url)
        self.soup = BeautifulSoup(self.reqs.text, 'html.parser')

    def checkURL(self, url):
        try:
            req = requests.get(self.url)
            return req
        except:
            print(f'{self.url} is not valid. Try again.')
            exit('Sucker')

    def find(self):
        soups = ['title', 'h1', 'h2', 'h3']
        for tag in enumerate(soups):
            self.find2(tag)

    def find2(self, tag):
        soup = BeautifulSoup(self.reqs.content.decode(), 'html.parser')
        title_tags = soup.find_all(tag)
        if title_tags:
            for title_tag in enumerate(title_tags):
                pprint.pprint(f"{tag[1]}: {title_tag}")
                print('\n')
        else:
            print(f"{self.url} does not appear to have any <{tag[1]}> tags.")

    def usrCheck(self):
        response = requests.get(self.url).json()
        print(f"There are {response['data'][0]['active_visitors']} active visitors. On {self.url}")


    def docConts(self):
        headers = {'Range': f'bytes=0-{2999}'}
        response = requests.get(self.url, headers=headers)
        print(response.content.decode())

    def docConts2(self):
        linkR = urllib.request.urlopen(self.url)
        book = linkR.read().decode()
        print(book)
        
def one():
    scrape = scraper('https://www.python.org')
    scrape.find()

def two():
    govs = scraper('https://analytics.usa.gov/data/live/realtime.json')
    govs.usrCheck()

def three():
    pyFour = scraper('http://www.py4inf.com/code/romeo-full.txt')
    pyFour.docConts2()

def four():
    one()
    two()
    three()

def main():
    selection = 7
    while selection > 6:
        selection = int(input('''To see the solutions for the questions make a selection:
        For 1, 2, 3, and 5: Press 1
        For 2, and 4: Press 2
        For 2, and 6: Press 3
        For all: Press 4
        To exit: press 5: '''))
    if selection == 1:
        one()
    elif selection == 2:
        two()
    elif selection == 3:
        three()
    elif selection == 4:
        one()
        two()
        three()
        four()
    elif selection == 5:
        exit('Thanks for playing!')
    else:
        print('How did you get here?')
        main()

if __name__ == "__main__":
    main()
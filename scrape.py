import requests
from bs4 import BeautifulSoup
from random import randint
import argparse

class Scraper:
    def __init__(self):
        self.headers = None

    def setRandomHeader(self):
        userAgentDict = {0:'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
        1:'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0;  Trident/5.0)',
        2:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
        3:'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'}
        self.headers = requests.utils.default_headers()
        self.headers.update({'User-Agent':userAgentDict[randint(0,len(userAgentDict)-1)]})

    def setUpProxy(self):
        self.session = requests.session()
        self.proxies = {}
        self.session.proxies['http'] = 'socks5h://localhost:9050'
        self.session.proxies['https'] = 'socks5h://localhost:9050'

    def getPage(self, url):
        if self.headers == None:
            html = self.session.get(url)
        else:
            html = self.session.get(url,headers=self.headers)
        return html


s = Scraper()
s.setRandomHeader()
s.setUpProxy()
print(s.getPage('http://httpbin.org/ip').text)
print(s.getPage('http://httpbin.org/user-agent').text)
print(s.getPage('http://httpbin.org/cookies').text)

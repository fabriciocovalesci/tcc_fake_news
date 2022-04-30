import re
import requests
from bs4 import BeautifulSoup

from .portal_r7_bot import PortalR7Bot

class ActaBot:
    
    def __init__(self, urls):
        self.urls = urls
        
    def request_site(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'}
        result = requests.get(url, headers=headers)
        return result.content
        
    def object_soup(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup
        
    def filter_urls(self, domain, soup):
        """Description

    Args:
        soup (Object): Instance type BeautifulSoup

    Returns:
        list: List of string with valid url
    """
        list_url = []    
        for a in soup.find_all('a', href=True):
            if (re.search(domain, a['href'])) and (a['href'] not in list_url) and not(a['href'] in EXCLUD_URLS):
                list_url.append(a['href'])
        return list_url
        
    def get_domain(self):
        for url in self.urls:
            if url == 'https://www.portalbr7.com/':
                portal_r7_bot = PortalR7Bot(url)
                obj_scraping = portal_r7_bot.get_text()
                return obj_scraping
            # match url:
            #     case 'https://www.portalbr7.com/':
            #         #portal_r7_bot = PortalR7Bot(url)
            #         print(url)
            #     # case 'www.google.com/':
            #     #     print('google')
            #     case _:
            #         raise TypeError("Url ainda não configurada para ActaBot")
        
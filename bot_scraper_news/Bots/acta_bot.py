#!/usr/bin/env python3

import re
import requests
from bs4 import BeautifulSoup
import asyncio

from .portal_r7_bot import PortalR7Bot
from .uol_bot import UolBot

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
        
    def start(self):
        obj_scraping = []
        
        for url in self.urls:
            
            if  url == 'https://www.portalbr7.com/':
                    portal_r7_bot = PortalR7Bot(url)
                    obj_scraping_portal = asyncio.run(portal_r7_bot.get_text())
                    obj_scraping.append(obj_scraping_portal)
                    
            elif url == 'https://www.uol.com.br/':
                uol_bot = UolBot(url)
                obj_scraping_uol = asyncio.run(uol_bot.get_text())
                obj_scraping.append(obj_scraping_uol)

        return obj_scraping
        
#!/usr/bin/env python3

import re
from types import coroutine
import requests
from bs4 import BeautifulSoup
import aiohttp
import asyncio

EXCLUD_URLS = [
    'https://www.portalbr7.com/category/politica/', 'https://www.portalbr7.com/category/curiosidades/',
    'https://www.portalbr7.com/contato/', 'https://www.portalbr7.com/politica-de-privacidade-2/',
    'https://www.portalbr7.com/', 'https://www.portalbr7.com/2022/04/28/%ef%bf%bc%ef%bf%bc-2/#comments',
    'https://www.portalbr7.com/category/atualidades/'
]


class PortalR7Bot:
    
    def __init__(self, domain):
        if domain == "https://www.portalbr7.com/":
            self.domain = domain
            self.base_url_politica = self.domain + "category/politica/"
        else:
            raise TypeError("Domain Portal R7 invalida.")
        
    
    async def _request_site_async(self, url: str) -> str:
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'}
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                html = await response.text()
                return html
    
    
    def _object_soup(self, html: str) -> object:
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    
    
    async def _filter_urls(self) -> list:
        """Description

        Args:
            soup (Object): Instance type BeautifulSoup

        Returns:
            list: List of string with valid url
        """
        task = asyncio.create_task(coro=self._request_site_async(self.base_url_politica))
        html_page = await task
        
        soup = self._object_soup(html_page)
        list_url = []    
        for a in soup.find_all('a', href=True):
            if (re.search(self.domain, a['href'])) and (a['href'] not in list_url) and not(a['href'] in EXCLUD_URLS):
                list_url.append(a['href'])
        return list_url
        
        
    async def _scraping_site(self, url: str) -> list:
        try:
            data_site = {
                "title": "",
                "date": "",
                "domain": self.domain,
                "url": url,
                "author": "",
                "text": []
            }
            
            task = asyncio.create_task(coro=self._request_site_async(url))
            content = await task
            
            soup = self._object_soup(content)
            data_site['title'] = soup.find('h1', {"class": "jeg_post_title"}).text
            
            divs = soup.findChild("div", {"class": "jeg_meta_date"})
            date_pt_br = divs.find('a').text
            data_site['date'] = date_pt_br #format_date(date_pt_br.split('de'))
            
            div = soup.find('div', {"class": "content-inner"})
            children = div.findChildren("p" , recursive=False)
            
            text_elements = []
            for child in children:
                if len(child.get_text()) != 0:
                    text_elements.append(child.get_text().strip())

            data_site['text'] = text_elements
            return data_site
        except:
            return []
    
        
    async def get_text(self) -> list:
        result = []
        list_urls = await self._filter_urls()
        for url in list_urls[0:2]:
            content = await self._scraping_site(url)
            if len(content) != 0:
                result.append(content)
                print(f"Add new title: {content['title']} | url {content['url']}")
        return result

            
    
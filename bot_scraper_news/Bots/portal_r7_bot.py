#!/usr/bin/env python3

import re
from types import coroutine
import requests
from bs4 import BeautifulSoup
import aiohttp
import asyncio
from datetime import date, datetime, timedelta

EXCLUD_URLS = [
    'https://www.portalbr7.com/category/politica/', 'https://www.portalbr7.com/category/curiosidades/',
    'https://www.portalbr7.com/contato/', 'https://www.portalbr7.com/politica-de-privacidade-2/',
    'https://www.portalbr7.com/', 'https://www.portalbr7.com/2022/04/28/%ef%bf%bc%ef%bf%bc-2/#comments',
    'https://www.portalbr7.com/category/atualidades/'
]


class PortalR7Bot:
    
    def __init__(self):
        self.domain = "https://www.portalbr7.com/"
        self.base_url_politica = self.domain + "category/politica/"

    
    async def _request_site_async(self, url: str) -> str:
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'}
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    html = await response.text()
                    return html
        except Exception as err:
            print(f"ERROR - Portal R7: function [_request_site_async()] : {err}")
    
    
    def _object_soup(self, html: str) -> object:
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    
    
    def _format_date(self, date):
        """Convert date in full to date

        Args:
            date (str): Date publication of the news 

        Returns:
            date: Returns post date type Date
        """
        day = date[0].strip()
        mounth = date[1].strip()
        year = date[2].strip()
        month_name = {
            'janeiro' :'1',
            'fevereiro': '2',
            'março' : '3',
            'abril': '4',
            'maio': '5',
            'junho': '6',
            'julho': '7',
            'agosto': '8',
            'setembro': '9',
            'outubro': '10',
            'novembro': '11',
            'dezembro': '12' 
            }
        date_formated = datetime.strptime(f'{day}/{month_name.get(mounth)}/{year}', "%d/%m/%Y").date()
        return date_formated
    
    
    def _clean_data(self, data):
        text = data.replace("“", '').replace("”", '').replace("`", '').replace("´", '').replace("’", '').replace("‘", '').strip()
        return text
    
    
    async def _filter_urls(self, search_date) -> list:
        """Description

        Args:
            soup (Object): Instance type BeautifulSoup

        Returns:
            list: List of string with valid url
        """
        try:
            task = asyncio.create_task(coro=self._request_site_async(self.base_url_politica))
            html_page = await task
            
            soup = self._object_soup(html_page)
            urls = soup.find_all("div", { "class": "jeg_meta_date" })
            
            list_url = []
            for _date in urls:
                date_page = self._format_date(_date.text.split('de'))
                if date_page and date_page == search_date:
                    list_url.append({ "date": datetime.strftime(date_page, "%d/%m/%Y") , "url": _date.find("a", href=True).get('href') })
            
            return list_url
        except Exception as err:
            print(f"ERROR - Portal R7: function [_filter_urls()] : {err}")
                    
        
    async def _scraping_site(self, url: str, date: str) -> list:
        try:
            data_site = {
                "title": "",
                "date": date,
                "domain": self.domain,
                "status": "",
                "url": url,
                "author": "Colunista Portal R7",
                "text": []
            }
            
            task = asyncio.create_task(coro=self._request_site_async(url))
            content = await task
            
            soup = self._object_soup(content)
            title = soup.find('h1', {"class": "jeg_post_title"}).text
            if title:
                data_site['title'] = self._clean_data(title)
            else:
                data_site['title'] = title
            
            # Get date with soup
            # divs = soup.findChild("div", {"class": "jeg_meta_date"})
            # date_pt_br = divs.find('a').text
            # data_site['date'] = date_pt_br #format_date(date_pt_br.split('de'))
            
            div = soup.find('div', {"class": "content-inner"})
            children = div.findChildren("p" , recursive=False)
            
            text_elements = []
            for child in children:
                if len(child.get_text()) != 0:
                    text_elements.append(self._clean_data(child.get_text()))
                    
            text_elements = ''.join(map(str,text_elements))
            
            data_site['text'] = text_elements
            return data_site
        except Exception as err:
            print(f"ERROR - Portal R7: function [_scraping_site()] : {err}")
    
        
    async def get_text(self) -> list:
        try:
            result = []
            last_day = datetime.today() - timedelta(days=1)
            list_urls = await self._filter_urls(last_day.date())
            for url in list_urls:
                content = await self._scraping_site(url['url'], url['date'])
                if len(content) != 0:
                    result.append(content)
                    print(f"Add new title: {content['title']} | url {content['url']}")
            return result
        except Exception as err:
            print(f"ERROR - Portal R7: function [get_text()] : {err}")

            
    
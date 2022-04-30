import re
import requests
from bs4 import BeautifulSoup


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
        
    def _request_site(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'}
        result = requests.get(url, headers=headers)
        return result.content
    
    def _object_soup(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    
    
    def _filter_urls(self):
        """Description

        Args:
            soup (Object): Instance type BeautifulSoup

        Returns:
            list: List of string with valid url
        """
        html_page = self._request_site(self.base_url_politica)
        soup = self._object_soup(html_page)
        list_url = []    
        for a in soup.find_all('a', href=True):
            if (re.search(self.domain, a['href'])) and (a['href'] not in list_url) and not(a['href'] in EXCLUD_URLS):
                list_url.append(a['href'])
        return list_url
        
        
    def _scraping_site(self, url):
        try:
            data_site = {
                "title": "",
                "date": "",
                "domain": self.domain,
                "url": url,
                "text": []
            }
            content = self._request_site(url)
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
        
    def get_text(self):
        result = []
        list_urls = self._filter_urls()
        for url in list_urls[0:10]:
            content =  self._scraping_site(url)
            if len(content) != 0:
                result.append(content)
                print(f"Add new title: {content['title']} | url {content['url']}")
        return result
            
    
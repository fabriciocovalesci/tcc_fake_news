import requests
from bs4 import BeautifulSoup
import re
import urllib3
from datetime import date, datetime, timedelta

from filter_urls import filter_urls

BASE_URL_POLITICA = "https://www.portalbr7.com/category/politica/"

BLOCK_LIST = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    'webkit',
    'footer',
    'figure',
    'blockquote',
    'figcaption'
]

def format_date(date):
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



def request_site(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'}
    result = requests.get(url, headers=headers)
    return result.content

def function_soup(content):
    soup = BeautifulSoup(content, 'html.parser')
    return soup


def scraping_site(url):
    if len(urllib3.get_host(url)) != 0:
        domain = urllib3.get_host(url)[1]
    try:
        data_site = {
            "title": "",
            "date": "",
            "domain": domain,
            "url": url,
            "text": []
        }
        content = request_site(url)
        soup = function_soup(content)
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



html_page = request_site(BASE_URL_POLITICA)
SOUP_BASE_URL = function_soup(html_page)

list_urls = filter_urls(SOUP_BASE_URL)

divs = SOUP_BASE_URL.findChild("div", {"class": "jeg_meta_date"})


date_pt_br = divs.find('a').text

date_publish_site = format_date(date_pt_br.split('de'))
date_request_now = datetime.today().date()

list_content = []
if abs(date_publish_site - date_request_now).days == 1:
# if date_publish_site == date_request_now:
    for url in list_urls:
        content =  scraping_site(url)
        if len(content) != 0:
            list_content.append(content)
            print(f"Add new title: {content['title']} | url {content['url']}")
    
# https://github.com/brauliotegui/FAKE/blob/master/NLP_model.ipynb


print(list_content)
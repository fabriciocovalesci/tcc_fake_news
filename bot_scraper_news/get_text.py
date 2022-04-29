import requests
from bs4 import BeautifulSoup
from datetime import date, datetime, timedelta

from filter_urls import filter_urls

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


BASE_URL_POLITICA = "https://www.portalbr7.com/category/politica/"

res = requests.get(BASE_URL_POLITICA, headers={'User-Agent': 'Mozilla/5.0'})
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')

list_urls = filter_urls(soup)

divs = soup.findChild("div", {"class": "jeg_meta_date"})

print(divs.find('a').text)

date_pt_br = divs.find('a').text

date_publish_site = format_date(date_pt_br.split('de'))
date_request_now = datetime.today().date()


if abs(date_publish_site - date_request_now).days == 1:
    print('Bora!!')
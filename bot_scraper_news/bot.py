import requests
from bs4 import BeautifulSoup
from filter_urls import filter_urls

url_base_politica = "https://www.portalbr7.com/category/politica/"

res = requests.get(url_base_politica, headers={'User-Agent': 'Mozilla/5.0'})
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')

divs = soup.find_all("div", {"class": "jeg_thumb"})



text = soup.find_all(text=True)

output = ''
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    'webkit',
    'style',
    'endif'
    'footer'
    './footer'
]

for t in text:
    if t.parent.name not in blacklist:
        output += '{} '.format(t)
    
urls_filted = filter_urls(soup)

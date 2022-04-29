import re

exclude_urls = [
    'https://www.portalbr7.com/category/politica/', 'https://www.portalbr7.com/category/curiosidades/',
    'https://www.portalbr7.com/contato/', 'https://www.portalbr7.com/politica-de-privacidade-2/',
    'https://www.portalbr7.com/', 'https://www.portalbr7.com/2022/04/28/%ef%bf%bc%ef%bf%bc-2/#comments'
]

domain = 'https://www.portalbr7.com/'

def filter_urls(soup):
    """Description

    Args:
        soup (Object): Instance type BeautifulSoup

    Returns:
        list: List of string with valid url
    """
    list_url = []    
    for a in soup.find_all('a', href=True):
        if (re.search(domain, a['href'])) and (a['href'] not in list_url) and not(a['href'] in exclude_urls):
            list_url.append(a['href'])
    return list_url

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

query_url = 'http://www.iciba.com/'


# str -> list[str]
def query(word):
    word.replace(' ', '%20')
    html = urlopen(query_url + word)
    bsObj = BeautifulSoup(html.read(), 'html.parser')
    content = bsObj.select('div.collins-section')[0]
    lst = []
    for part in content.children:
        content = re.sub(r'<.*?>', '', str(part))
        lst += list(filter(lambda x: len(x.strip()) != 0, content.split('\n')))
    return lst

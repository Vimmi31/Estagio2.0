import requests
from bs4 import BeautifulSoup
def test_connection(link):
    while True:
        try:
            response = requests.get(link)
        except:
            link = input('Link fora do ar ou invalido, tente novamente')
            continue
        else:
            return (link)
        
def capture_html(link):
    content = requests.get(link).content
    site = BeautifulSoup(content, 'html.parser')
    return(site)

def get_title(site, lan_quant = 1):
    if lan_quant == 1:
        title = site.find('h1', attrs={'class': 'article-title'})
        return (title.text)
    else:
        list_title = []
        cont = 0
        while cont < lan_quant:
            cont += 1
            title = site.find('h'+str(cont), attrs={'class': 'article-title'})
            list_title.append(title.text)
        return (list_title)
    
def get_abstract(site, lan_quant=1):
    if lan_quant == 1:
        section = site.find('article', attrs={'class': 'col-md-10 col-md-offset-2 col-sm-12 col-sm-offset-0', 'id':'articleText'})
        abstract = section.find('p').text
        return abstract

link = test_connection(input('Digite o link do artigo'))
site = capture_html(link)
section = site.find('article', attrs={'class': 'col-md-10 col-md-offset-2 col-sm-12 col-sm-offset-0', 'id':'articleText'})

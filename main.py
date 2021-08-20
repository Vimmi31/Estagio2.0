import requests
from bs4 import BeautifulSoup

def test_connection(link):
    while True:
        try:
            response = requests.get(link)
        except:
            link = input('Link fora do ar ou invalido, tente novamente: ')
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
    
def get_abstract(site):
        section = site.find('article', attrs={'class': 'col-md-10 col-md-offset-2 col-sm-12 col-sm-offset-0', 'id':'articleText'})
        abstract = section.find('p')
        return abstract.text

def get_keyword(site):
    section = site.find('article', attrs={'class': 'col-md-10 col-md-offset-2 col-sm-12 col-sm-offset-0', 'id':'articleText'})
    keyword = section.find('br').next_element
    return keyword

def get_author(site):
    section = site.find('div', attrs={'class': 'contribGroup'})
    authors = section.find_all('a')
    author = []
    range_authors = len((authors))
    for i in range(range_authors):
        if i == range_authors-1:
            pass
        elif i % 2 == 0 or i == 0 :
             author.append(authors[i].text)
    return author
    
link = test_connection(input('Digite o link do artigo: '))
site = capture_html(link)

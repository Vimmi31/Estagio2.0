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

def get_title(site, social = True):
        title = site.find('h1', attrs={'class': 'article-title'})
        if social:
            return (title.text.rstrip('\n'))
        else:
             return (title.text.rstrip('\n'))
    
def get_abstract(site):
        section = site.find('article', attrs={'class': 'col-md-10 col-md-offset-2 col-sm-12 col-sm-offset-0', 'id':'articleText'})
        abstract = section.find('p')
        return abstract.text

def get_keyword(site, Hashtag = True):
    section = site.find('article', attrs={'class': 'col-md-10 col-md-offset-2 col-sm-12 col-sm-offset-0', 'id':'articleText'})
    keyword = section.find('br').next_element
    if Hashtag == True:
        keyword = '#' + keyword.replace(" ", "").replace(';', ' #')
    return keyword

def get_author(site):
    section = site.find('div', attrs={'class': 'contribGroup'})
    authors = section.find_all('a')
    author = []
    range_authors = len((authors))
    for i in range(range_authors):
        if (i % 3 == 0) or (i == 0) :
             author.append(authors[i].text)
    author.pop() #Para tirar o lixo capturado(textos que não são nomes dos autores)
    return author


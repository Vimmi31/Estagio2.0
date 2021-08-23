import requests
from bs4 import BeautifulSoup

def test_connection(link):
    """
        Função que valida se o link digitado é correto, se não for pede para o user digitar um novo link, até que ele funcione
    Args:
        link [String]: Recebe o link do resumo 

    Returns:
        [str]: [Link funcional]
        [none]: [Quando não existir conexão]
    """
    while True:
        try:
            response = requests.get(link)
        except:
            link = input('Link fora do ar ou invalido, tente novamente: ')
            continue
        else:
            return (link)
        
def capture_html(link):
    """Retorna o conteudo html do link
    Args:
        link (String): Link do site
    """
    content = requests.get(link).content
    site = BeautifulSoup(content, 'html.parser')
    return(site)

def get_title(site, social = True):
    """Retorna o Titulo do resumo
    Args:
        site (BeautifulSoup): Conteudo html do resumo
        social (bool, optional): [description]. Defaults to True.

    Returns:
        [type]: [description]
    """
    title = site.find('h1', attrs={'class': 'article-title'})
    return (title.text.rstrip('\n'))
    
def get_abstract(site):
    """Retorna o resumo em si(apenas o texto principal)
    Args:
        site (BeautifulSoup): Conteudo html do resumo
    Returns:
        Str: Resumo do site
    """
    section = site.find('article', attrs={'class': 'col-md-10 col-md-offset-2 col-sm-12 col-sm-offset-0', 'id':'articleText'})
    abstract = section.find('p')
    return abstract.text

def get_keyword(site, Hashtag = True):
    """Retorna as palavras chaves do artigo
    Args:
        site (BeautifulSoup): Conteudo html do resumo
        Hashtag (bool, optional): Se verdadeiro retorna elas em formato de tags para redes sociais. Defaults to True.

    Returns:
        Str: Palavras chaves
    """
    section = site.find('article', attrs={'class': 'col-md-10 col-md-offset-2 col-sm-12 col-sm-offset-0', 'id':'articleText'})
    keyword = section.find('br').next_element
    if Hashtag == True:
        keyword = '#' + keyword.replace(" ", "").replace(';', ' #')
    return keyword

def get_author(site):
    """Retorna todos os autores do artigo
    Args:
        site (BeautifulSoup): Conteudo html do resumo
    Returns:
        Str: Autores
    """
    section = site.find('div', attrs={'class': 'contribGroup'})
    authors = section.find_all('a')
    author = []
    range_authors = len((authors))
    for i in range(range_authors):
        if (i % 3 == 0) or (i == 0) :
             author.append(authors[i].text)
    author.pop() #Para tirar o lixo capturado(textos que não são nomes dos autores)
    return author

def get_original_link(site):
    """Função que rotorna o link do texto completo(doi)

    Args:
        site (BeautifulSoup): Conteudo html do resumo
    Returns:
        Str: Link do texto completo
    """
    section = site.find('span', attrs={'class': 'group-doi'})
    original = section.find('a')
    return original.text


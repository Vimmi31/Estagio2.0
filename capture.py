import requests, os
from bs4 import BeautifulSoup

def test_connection(link):
    """
        Função que valida se o link digitado é correto, se não for pede para o user digitar um novo link, até que ele funcione.
        Também valida se o site digitado é ou não o do resumo, se não for tenta colocar o link para o resumo do artigo, se esse não existir, retorna o primeiro link funcional digitado
    Args:
        link [String]: Recebe o link do resumo 

    Returns:
        [str]: [Link funcional]
    """
    while True:
        try:
            r = requests.get(link)
        except :
            link = input('Link fora do ar ou invalido, tente novamente: ')
        else:
            break
    if 'abstract' not in link: # Verificando se o link colocado é de um Resumo
        transform = link.split('/')
        transform.insert(7, 'abstract')
        transformSTR = '/'.join(map(str, transform))
        try:
            r = requests.get(transformSTR, verify=False)
        except:
            print('Atenção o artigo do link em questão não tem uma pagina de resumo, isso pode fazer com que o software não consiga criar os textos corretamente, revise-os antes de postar.') 
            return(link)
        else: 
            return (transformSTR)
    else:
        return(link)
        
def capture_html(link):
    """Retorna o conteudo html do link
    Args:
        link (String): Link do site
    """
    content = requests.get(link).content
    site = BeautifulSoup(content, 'html.parser')
    return(site)

def get_title(site):
    """Retorna o Titulo do resumo
    Args:
        site (BeautifulSoup): Conteudo html do resumo
        social (bool, optional): [description]. Defaults to True.

    Returns:
        [type]: [description]
    """
    title = site.find('h1', attrs={'class': 'article-title'})
    return (title.text.replace('\n', ''))
    
def get_abstract(site):
    """Retorna o resumo em si(apenas o texto principal)
    Args:
        site (BeautifulSoup): Conteudo html do resumo
    Returns:
        Str: Resumo do site
    """
    try:
        section = site.find('article', attrs={'class': 'col-md-10 col-md-offset-2 col-sm-12 col-sm-offset-0', 'id':'articleText'})
        abstract = section.find('p')
        return abstract.text
    except:
        return "Não foi possivel capturar o resumo"

def get_keyword(site, Hashtag = True):
    """Retorna as palavras chaves do artigo
    Args:
        site (BeautifulSoup): Conteudo html do resumo
        Hashtag (bool, optional): Se verdadeiro retorna elas em formato de tags para redes sociais. Defaults to True.

    Returns:
        Str: Palavras chaves
    """
    try:
        section = site.find('article', attrs={'class': 'col-md-10 col-md-offset-2 col-sm-12 col-sm-offset-0', 'id':'articleText'})
        keyword = section.find('br').next_element
    except:
        return "Não foi possivel capturar as palavras chaves"
    else:
        if Hashtag == True:
            keyword = '#' + keyword.replace(" ", "").replace(';', ' #')
        else:
            keyword = keyword.replace(';', ',')
        return keyword

def get_author(site):
    """Retorna todos os autores do artigo
    Args:
        site (BeautifulSoup): Conteudo html do resumo
    Returns:
        Str: Autores
    """
    try:
        section = site.find('div', attrs={'class': 'contribGroup'})
        authors = section.find_all('a')
        author = []
        range_authors = len((authors))
        for i in range(range_authors):
            if (i % 3 == 0) or (i == 0) : # Os nomes dos autores são estão em posiçoes multiplas de 3 da lista
                author.append(authors[i].text.lstrip().rstrip())
        author.pop() #Para tirar o lixo capturado(textos que não são nomes dos autores)
        return author
    except:
        return ["Não foi possivel capturar os autores"]

def get_original_link(site):
    """Função que rotorna o link do texto completo(doi)

    Args:
        site (BeautifulSoup): Conteudo html do resumo
    Returns:
        Str: Link do texto completo
    """
    try:
        section = site.find('span', attrs={'class': 'group-doi'})
        original = section.find('a')
        return original.text
    except: 
        return 'Não foi possivel capturar o link original'

def get_kind(site):
    """retorna o tipo do artigo(Artigo, dossie, entrevista etc)
    Args:
        site (BeautifulSoup): Conteudo html do resumo

    Returns:
         [type]: [description]
    """
    kind = site.find('span', attrs={'class': '_articleBadge'})
    return kind.text
    
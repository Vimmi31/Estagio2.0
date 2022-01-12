"""Classe responsavel pela captação e tratamento inicial das infomaçoes contidas no site da Scielo"""

import requests, os
from bs4 import BeautifulSoup

class Capture:
    """Classe responsavel por capturar os elementos no site"""
    def __init__(self, link):
        """Metodo construtor que recebe os valores necessarios para a execução da classe, ele também:
        - Valida se o link digitado é correto, se não for pede para o user digitar um novo link, até que ele funcione.
        - Valida se o site digitado é ou não o do resumo, se não for tenta colocar o link para o resumo do artigo, se esse não existir, retorna o primeiro link funcional digitado
        - Captura o HTML do site

        Args:
            link (String): É o link para qual serão criados os textos.""" 
            
        #Validando Link
        self.title = ''
        self.link = link
        cont = 0
        while True:
            if cont < 4:   
                cont += 1 
                try:
                    requests.get(self.link)
                except:
                    self.link = input('Link fora do ar ou invalido, tente novamente: ')
                else:
                    break
            else:
                print("Algum problema de conexão com o site está acontecendo, verifique se o computador está conectado a internet e tente novamente mais tarde.")
                exit()
            
         # Verificando se o link colocado é de um Resumo    
        if 'abstract' not in self.link:
            transform = self.link.split('/')
            transform.insert(7, 'abstract')
            transformed = '/'.join(map(str, transform))
            try:
                requests.get(transformed)
            except:
                print('Atenção o artigo do link em questão não tem uma pagina de resumo, isso pode fazer com que o software não consiga criar os textos corretamente, revise-os antes de postar.')
            else:
                self.link = transformed
                
        #Capturando conteudo HTML do site
        content = requests.get(self.link).content
        self.site = BeautifulSoup(content, 'html.parser')
    
    def get_title(self):
        """Retorna o Titulo do resumo
        Returns:
        [String]: [Titulo do artigo]"""
        self.title = (self.site.find('h1', attrs={'class': 'article-title'})).text
        return self.title
        
    def get_summary(self):
        """Retorna o resumo em si(apenas o texto principal)
        Returns:
            Str: Resumo do site"""
        try:
            section = self.site.find('article',
                                     attrs={'class': 'col-md-10 col-md-offset-2 col-sm-12 col-sm-offset-0', 'id':'articleText'})
            summary = section.find('p')
            return summary.text
        except:
            return "Não foi possivel capturar o resumo"

    def get_keyword(self, hashtag = True):
        """Retorna as palavras chaves do artigo
        Args:
            site (BeautifulSoup): Conteudo html do resumo
            Hashtag (bool, optional): Se verdadeiro retorna elas em formato de tags para redes sociais. Defaults to True.

        Returns:
            Str: Palavras chaves"""
        try:
            section = self.site.find('article', 
                                     attrs={'class': 'col-md-10 col-md-offset-2 col-sm-12 col-sm-offset-0', 'id':'articleText'})
            keyword = section.find('br').next_element
        except:
            return "Não foi possivel capturar as palavras chaves"
        else:
            if hashtag == True:
                keyword = '#' + keyword.replace(" ", "").replace(';', ' #')
            else:
                keyword = keyword.replace(';', ',')
            return keyword

    def get_author(self):
        """Retorna todos os autores do artigo
        Args:
            site (BeautifulSoup): Conteudo html do resumo
        Returns:
            Str: Autores"""
        try:
            section = self.site.find('div', attrs={'class': 'contribGroup'})
            authors = section.find_all('a')
            author = []
            range_authors = len((authors))
            for i in range(range_authors):
                
                if (i % 3 == 0) or (i == 0) : 
                    author.append(authors[i].text.lstrip().rstrip())
            author.pop() #Para tirar o lixo capturado(textos que não são nomes dos autores)
            return author
        except:
            return ["Não foi possivel capturar os autores"]

    def get_original_link(self):
        """Função que rotorna o link do texto completo(doi)

        Args:
            site (BeautifulSoup): Conteudo html do resumo
        Returns:
            Str: Link do texto completo
        """
        try:
            section = self.site.find('span', attrs={'class': 'group-doi'})
            original = section.find('a')
            return original.text
        except: 
            return 'Não foi possivel capturar o link original'

    def get_kind(self):
        """retorna o tipo do artigo(Artigo, dossie, entrevista etc)
        Args:
            site (BeautifulSoup): Conteudo html do resumo

        Returns:
            [type]: [description]
        """
        kind = self.site.find('span', attrs={'class': '_articleBadge'})
        return kind.text
    
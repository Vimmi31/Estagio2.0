from os import makedirs
from capture import Capture

class Formating:
    def __init__(self, link):
        """Metodo inicial para a criação da pasta onde serão salvos os arquivos gerados.
        Args:
            title (String): Titulo do resumo, será usado como nome da pasta.
        """
        self.capturing = Capture(link)
        title = self.capturing.get_title()
        self.link = link
        self.caminho = "C://Users//Vinicius//Desktop"
        try:
            title_format = ''.join(char for char in title if char.isalnum())
            self.caminho = self.caminho + '\\' + title_format
            makedirs(self.caminho)
        except FileExistsError() :
            makedirs(self.caminho + '\\' + title.split[0])
            

    def txt_facebook(self, link):
        """Função que cria o texto de um post para o facebook, cria um arquivo de 
           texto no caminho especificado com o conteudo gerado
        Args:
            link (Str): Link do resumo
        caminho (Str): Aonde o aqrquivo será salvo no PC
            site (BeautifulSoup): Conteudo html do resumo
        """
        print("PARTE FACEBOOK")
        
        caminho_fb = self.caminho
        caminho_fb = caminho_fb + '\\' +'facebook.txt'
        try:
            open (caminho_fb, 'r+',) 
        except FileNotFoundError:
            open (caminho_fb, 'w+')    
        facebook = open (caminho_fb, 'a')
                
        # Escrevendo o Titulo do artido no .txt
        facebook.write(self.capturing.get_title() + ' - ')
                
        authors = self.capturing.get_author()
        # Escrevendo os nomes dos autores um a um
        for author in authors: 
            if len(authors) == 1: # verficando se há apenas um autor na lista
                facebook.write(author.rstrip())
                break
            if author == authors[-1]: #Verficando se é o ultimo autor da lista
                facebook.write(' e ' +author.rstrip())
            elif author == authors[-2]: # Verificando se é peloultimo
                facebook.write(author.rstrip())
            else:    
                facebook.write(author.rstrip() + ', ')
        facebook.write('\n\n')# Quebra de linha para organização
        # Escrevendo o resumo no arquivo .txt
        facebook.write(self.capturing.get_summary())
        facebook.write('\n\n')
        # Escrevendo o link no arquivo .txt
        facebook.write('Acesso em: ' + link)
        facebook.write('\n\n')
        # Escrevendo as palavras chaves no arquivo .txt
        facebook.write(self.capturing.get_keyword())
        facebook.close()

    def txt_twitter(self, link):
        """Função que cria o texto de um post para o Twitter, cria dois arquivos de texto no caminho especificado com o conteudo gerado(Um em Inglês, outro em portugues)

        Args:
            link (Str): Link do resumo
            caminho (Str): Aonde o aqrquivo será salvo no PC
            site_pb (BeautifulSoup): Conteudo html do resumo em Português
        """
        link_en = self.link.replace('pb', 'en')
        caminho = self.caminho + '//twitter.txt'
        site_pb = self.capturing
        site_en = Capture(link_en)
        try:
            open (caminho, 'r+') 
        except FileNotFoundError:
            open (caminho, 'w+')    
        twitter = open (caminho, 'a')
        twitter.write(Capture.get_title(site_pb))
        twitter.write('\n\n')
        twitter.write('Acesso em: ' + link)
        twitter.write('\n\n')
        twitter.write(Capture.get_keyword(site_pb))
            
        twitter.write('\n\n')
        twitter.write('_'*50)
        twitter.write('\n\n')
            
        twitter.write(Capture.get_title(site_en))
        twitter.write('\n\n')
        twitter.write('Access in: ' + link.replace('pt', 'en'))
        twitter.write('\n\n')
        twitter.write(Capture.get_keyword(site_en))
        twitter.close()

    # def txt_blog(link, caminho, site_pb, site_en, site_es):
    #     """Função que cria o texto de um post para o site, cria um arquivo de texto no caminho especificado com o conteudo gerado

    #     Args:
    #         link (Str): Link do resumo
    # caminho (Str): Aonde o aqrquivo será salvo no PC
    #         site (BeautifulSoup): Conteudo html do resumo
    #     """
    #     caminho = caminho.rstrip() + 'blog.txt'
    #     try:
    #         open (caminho, 'r+') 
    #     except FileNotFoundError:
    #         open (caminho, 'w+')    
    #     interface = open (caminho, 'a')
    # #For responsavel pela criação da linha de titulos
    #     for i in range(3):
    #         if i == 0:
    #             lan = site_pb
    #             tag = 'pb' # variavel tag recebe a linguagem da parte que está sendo executada no momento
    #         elif i == 1:
    #             lan = site_en
    #             tag = 'en'
    #         else:
    #             lan = site_es
    #             tag = 'es'
    #         interface.write(('[:' + tag + ']' + Capture.get_title(lan)).replace('\n', ''))
    #         if tag == 'es':
    #             interface.write('[:]')
    #     interface.write('\n\n') 
    # #For responsavel pela geração do corpo do site
    #     for i in range(3):
    #         if i == 0:
    #             lan = site_pb
    #             tag = 'pb'
    #             acssTxt = 'Acesso em:' # Variaveis que recebe o idioma da escrita
    #             keyTxt = 'Palavras-Chave: '
    #         elif i == 1:
    #             lan = site_en
    #             tag = 'en'
    #             acssTxt = 'Access in:'
    #             keyTxt = 'Keywords: '
    #         else:
    #             lan = site_es
    #             tag = 'es'
    #             acssTxt = 'Acceso en:'
    #             keyTxt = 'Palabras clave: '
                    
    #         interface.write('[:' + tag + ']' + '\n' + Capture.get_abstract(lan))
    #         interface.write('\n\n')
                
    #         interface.write('<strong>' + acssTxt +'</strong> <a href="' +Capture.get_original_link(lan) + '">' + Capture.get_original_link(lan)+'</a>')
    #         interface.write('\n\n')
                
    #         interface.write('<strong>' + keyTxt + '</strong>' + Capture.get_keyword(lan, Hashtag=False))
    #         interface.write('\n\n')
    #     interface.write('[:]')
        
    # def txt_publication (link, caminho, site_pb, site_en, site_es):
    """Função que cria o texto de um post para um site wordpress formatado em html, cria um arquivo de texto no caminho especificado com o conteudo gerado

        Args:
            link (Str): Link do resumo
     caminho (Str): Aonde o aqrquivo será salvo no PC
            site (BeautifulSoup): Conteudo html do resumo
        """
        # caminho = caminho.rstrip() + 'interface.txt'
        # try:
        #     open (caminho, 'r+') 
        # except FileNotFoundError:
        #     open (caminho, 'w+')    
        # publication = open (caminho, 'a')
        
        # authors = Capture.get_author(site_pb)
        # if authors != 'Não foi possivel capturar os autores':
            
        # Formatando os nomes do autores para a norma vancouver, EX: Vinicius Mendes Barbosa = Barbosa VM e escrevendo o nome dos autores sem formatação(para o campo "autores" do site)
        #     publication.write('Autores:\n')
        #     lfauthors = [] # lista dos autores formatados
        #     for author in authors:
        #         publication.write(author + ', ')
        #         author = author.split(' ')
        #         end = len(author) 
        #         fauthor = str() # autor formatado
        #         for i in range(end):
        #             if i == end - 1: # Se i for = a ultima passada do for ele para, para não tirar letras do ultimo nome
        #                 break
        #             else:
        #                 if fauthor == None:
        #                     fauthor =  author[i][0]
        #                 else: 
        #                     fauthor = fauthor + author[i][0]
        #         fauthor = author[-1] + ' ' + fauthor
        #         lfauthors.append(fauthor)
        # publication.write('\n\n' + '_'*50 + '\n\n')
        # for i in range(3):
        #     if i == 0:
        #         lan = site_pb
        #         acssTxt = 'Acesso em:' # Variaveis que recebe o idioma da escrita
        #         keyTxt = 'Palavras-Chave: '
        #     elif i == 1:
        #         acssTxt = 'Access in:'
        #         keyTxt = 'Keywords: '
        #         lan = site_en
        #     else:
        #         lan = site_es
        #         acssTxt = 'Acceso en:'
        #         keyTxt = 'Palabras clave: '
        #     # Escrevendo o cabeçalho
        #     if len(lfauthors) == 1:
        #         publication.write(lfauthors[0])
        #     else:
        #         publication.write(lfauthors[0] + ', et al. ')    
        #     original = Capture.get_original_link(lan)
        #     publication.write('<strong>' + Capture.get_title(lan) + '. </strong>' + ' Interface (Botucatu). 2021; 25 e' + original[34:] + ' ' + '<a href="' + original + '">' + original + '</a>' )
        #     # Escrevendo o Resumo
        #     publication.write('\n\n')
        #     publication.write(Capture.get_abstract(lan))
        #     # Escrevendo o link de acesso
        #     publication.write('\n\n')
        #     publication.write('<strong>' + acssTxt + '</strong> ' + '<a href="' + original + '">' + original + '</a>')
        #     # Escrevendo as palavras chaves
        #     publication.write('\n\n')
        #     publication.write('<strong>' + keyTxt + '</strong> ' + Capture.get_keyword(lan, Hashtag=False))
        #     publication.write('\n\n' + '_'*50 + '\n\n' )       
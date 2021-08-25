import capture

def txt_facebook(link, caminho, site):
    """Função que cria o texto de um post para o facebook, cria um arquivo de texto no caminho especificado com o conteudo gerado

    Args:
        link (Str): Link do resumo
        caminho (Str): Aonde o aqrquivo será salvo no PC
        site (BeautifulSoup): Conteudo html do resumo
    """
    caminho = caminho.rstrip() + 'facebook.txt'
    try:
        open(caminho, 'r+') 
    except FileNotFoundError:
        open(caminho, 'w+')    
    facebook = open(caminho, 'a')
    
    # Escrevendo o Titulo do artido no .txt
    facebook.write(capture.get_title(site) + ' - ')
    
    authors = capture.get_author(site)
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
    facebook.write(capture.get_abstract(site))
    facebook.write('\n\n')
    # Escrevendo o link no arquivo .txt
    facebook.write('Acesso em: ' + link)
    facebook.write('\n\n')
    # Escrevendo as palavras chaves no arquivo .txt
    facebook.write(capture.get_keyword(site))
    facebook.close()

def txt_twitter(link, caminho, site_pb, site_en): 
    """Função que cria o texto de um post para o Twitter, cria dois arquivos de texto no caminho especificado com o conteudo gerado(Um em Inglês, outro em portugues)

    Args:
        link (Str): Link do resumo
        caminho (Str): Aonde o aqrquivo será salvo no PC
        site_pb (BeautifulSoup): Conteudo html do resumo em Português
        site_en (BeautifulSoup): Conteudo html do resumo em Inglês
    """
    caminho = caminho.rstrip() + 'twitter.txt'
    try:
        open(caminho, 'r+') 
    except FileNotFoundError:
        open(caminho, 'w+')    
    twitter = open(caminho, 'a')
    twitter.write(capture.get_title(site_pb))
    twitter.write('\n\n')
    twitter.write('Acesso em: ' + link)
    twitter.write('\n\n')
    twitter.write(capture.get_keyword(site_pb))
    
    twitter.write('\n\n')
    twitter.write('_'*50)
    twitter.write('\n\n')
    
    twitter.write(capture.get_title(site_en))
    twitter.write('\n\n')
    twitter.write('Access in: ' + link.replace('pt', 'en'))
    twitter.write('\n\n')
    twitter.write(capture.get_keyword(site_en))
    twitter.close()

def txt_blog(link, caminho, site_pb, site_en, site_es):
    """Função que cria o texto de um post para o site, cria um arquivo de texto no caminho especificado com o conteudo gerado

    Args:
        link (Str): Link do resumo
        caminho (Str): Aonde o aqrquivo será salvo no PC
        site (BeautifulSoup): Conteudo html do resumo
    """
    caminho = caminho.rstrip() + 'blog.txt'
    try:
        open(caminho, 'r+') 
    except FileNotFoundError:
        open(caminho, 'w+')    
    interface = open(caminho, 'a')
    # For responsavel pela criação da linha de titulos
    for i in range(3):
        if i == 0:
            lan = site_pb
            tag = 'pb' # variavel tag recebe a linguagem da parte que está sendo executada no momento
        elif i == 1:
            lan = site_en
            tag = 'en'
        else:
            lan = site_es
            tag = 'es'
        interface.write(('[:' + tag + ']' + capture.get_title(lan)).replace('\n', ''))
        if tag == 'es':
            interface.write('[:]')
    interface.write('\n\n') 
    # For responsavel pela geração do corpo do site
    for i in range(3):
        if i == 0:
            lan = site_pb
            tag = 'pb'
            acssTxt = 'Acesso em:' # Variaveis que recebe o idioma da escrita
            keyTxt = 'Palavras-Chave: '
        elif i == 1:
            lan = site_en
            tag = 'en'
            acssTxt = 'Access in:'
            keyTxt = 'Keywords: '
        else:
            lan = site_es
            tag = 'es'
            acssTxt = 'Acceso en:'
            keyTxt = 'Palabras clave: '
            
        interface.write('[:' + tag + ']' + '\n' + capture.get_abstract(lan))
        interface.write('\n\n')
        
        interface.write('<strong>' + acssTxt +'</strong> <a href="' +capture.get_original_link(lan) + '">' + capture.get_original_link(lan)+'</a>')
        interface.write('\n\n')
        
        interface.write('<strong>' + keyTxt + '</strong>' + capture.get_keyword(lan, Hashtag=False))
        interface.write('\n\n')
    interface.write('[:]')
    
def txt_publication (link, caminho, site_pb, site_en, site_es):
    caminho = caminho.rstrip() + 'interface.txt'
    try:
        open(caminho, 'r+') 
    except FileNotFoundError:
        open(caminho, 'w+')    
    publication = open(caminho, 'a')
    
    authors = capture.get_author(site_pb)
    if authors != 'Não foi possivel capturar os autores':
    # Formatando os nomes do autores para a norma vancouver, EX: Vinicius Mendes Barbosa = Barbosa VM
        lfauthors = [] # lista dos autores formatados
        for author in authors:
            author = author.split(' ')
            end = len(author) 
            fauthor = str() # autor formatado
            for i in range(end):
                if i == end - 1: # Se i for = a ultima passada do for ele para, para não tirar letras do ultimo nome
                    break
                else:
                    if fauthor == None:
                        fauthor =  author[i][0]
                    else: 
                        fauthor = fauthor + author[i][0]
            fauthor = author[-1] + ' ' + fauthor
            lfauthors.append(fauthor)
    for i in range(3):
        if i == 0:
            lan = site_pb
            acssTxt = 'Acesso em:' # Variaveis que recebe o idioma da escrita
            keyTxt = 'Palavras-Chave: '
        elif i == 1:
            acssTxt = 'Access in:'
            keyTxt = 'Keywords: '
            lan = site_en
        else:
            lan = site_es
            acssTxt = 'Acceso en:'
            keyTxt = 'Palabras clave: '
        # Escrevendo o cabeçalho
        if len(lfauthors) == 1:
            publication.write(lfauthors[0])
        else:
            publication.write(lfauthors[0] + ', et al. ')    
        original = capture.get_original_link(lan)
        publication.write('<strong>' + capture.get_title(lan) + '</strong>' + ' Interface (Botucatu). 2021; 25 e' + original[34:] + ' ' + '<a href="' + original + '">' + original + '</a>' )
        # Escrevendo o Resumo
        publication.write('\n\n')
        publication.write(capture.get_abstract(lan))
        # Escrevendo o link de acesso
        publication.write('\n\n')
        publication.write('<strong>' + acssTxt + '</strong> ' + '<a href="' + original + '">' + original + '</a>')
        # Escrevendo as palavras chaves
        publication.write('\n\n')
        publication.write('<strong>' + keyTxt + '</strong> ' + capture.get_keyword(lan, Hashtag=False))
        publication.write('\n\n' + '_'*50 + '\n\n' )
        
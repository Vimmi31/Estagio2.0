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
    facebook.write(capture.get_title(site) + ' -')
    authors = capture.get_author(site)
    for author in authors:
        facebook.write(author.rstrip() + ',')
    facebook.write('\n\n')
    facebook.write(capture.get_abstract(site))
    facebook.write('\n\n')
    facebook.write('Acesso em: ' + link)
    facebook.write('\n\n')
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

def txt_interface(link, caminho, site_pb, site_en, site_es):
    """Função que cria o texto de um post para o site, cria um arquivo de texto no caminho especificado com o conteudo gerado

    Args:
        link (Str): Link do resumo
        caminho (Str): Aonde o aqrquivo será salvo no PC
        site (BeautifulSoup): Conteudo html do resumo
    """
    caminho = caminho.rstrip() + 'publicação.txt'
    try:
        open(caminho, 'r+') 
    except FileNotFoundError:
        open(caminho, 'w+')    
    interface = open(caminho, 'a')
    for i in range(3):
        if i == 0:
            lan = site_pb
        elif i == 1:
            lan = site_en
        else:
            lan = site_es
        interface.write(capture.get_title(lan))
        interface.write("_"*30)
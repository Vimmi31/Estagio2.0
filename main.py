import capture

link = capture.test_connection(input('Digite qual o link do resumo? '))
site_pb = capture.capture_html(link)
site_en = capture.capture_html(link.replace('pt', 'en'))

def txt_facebook(link, caminho, site):
    caminho = caminho.rstrip() + 'facebook.txt'
    try:
        open(caminho, 'r+') 
    except FileNotFoundError:
        open(caminho, 'w+')    
    facebook = open(caminho, 'a')
    facebook.write(capture.get_title(site))
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
    
    twitter.write(capture.get_title(site_en))
    twitter.write('\n\n')
    twitter.write('Access in: ' + link.replace('pt', 'en'))
    twitter.write('\n\n')
    twitter.write(capture.get_keyword(site_en))
    twitter.close()

caminho = "D:\Programas\ "
txt_facebook(link, caminho, site_pb)
txt_twitter(link, caminho, site_pb, site_en)
import capture

link = capture.test_connection(input('Digite qual o link do resumo? '))
site = capture.capture_html(link)
title = capture.get_title(site)
authors = capture.get_author(site)
abstract = capture.get_abstract(site)
keywords = capture.get_keyword(site)
print(type(title))
print(type(authors[0]))


def txt_facebook(title, authors, caminho):
    try:
        open(caminho, 'r+') 
    except FileNotFoundError:
        open(caminho, 'w+')    
    facebook = open(caminho, 'a')
    facebook.write(title.rstrip('\n') + ' -')
    for author in authors:
        facebook.write(author + ' ')

caminho = 'D:\Programas\q.txt'
txt_facebook(title, authors, caminho)
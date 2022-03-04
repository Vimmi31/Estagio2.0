from capture import Capture
from formating import Formating

link = input('Qual o link do artigo')
summary = Formating(link)
summary.txt_facebook(link)
summary.txt_twitter(link)

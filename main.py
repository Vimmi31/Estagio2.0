import capture
import formating

link = capture.test_connection(input('Digite qual o link do resumo? '))
site_pb = capture.capture_html(link)
site_en = capture.capture_html(link.replace('pt', 'en'))
site_es = capture.capture_html(link.replace('pt', 'es'))
original = capture.get_original_link(site_pb)

caminho = 'C:/Users/Vinicius/Desktop/Estagio2.0/Estagio2.0/Text/ '

formating.txt_facebook(link, caminho, site_pb)
formating.txt_twitter(link, caminho, site_pb, site_en)
formating.txt_blog(link, caminho, site_pb, site_en, site_es)
formating.txt_publication(link, caminho, site_pb, site_en, site_es)

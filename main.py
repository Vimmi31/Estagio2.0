import capture, format

link = capture.test_connection(input('Digite qual o link do resumo? '))
site_pb = capture.capture_html(link)
site_en = capture.capture_html(link.replace('pt', 'en'))
site_es = capture.capture_html(link.replace('pt', 'es'))

caminho = "D:\Programas\ "
format.txt_facebook(link, caminho, site_pb)
format.txt_twitter(link, caminho, site_pb, site_en)
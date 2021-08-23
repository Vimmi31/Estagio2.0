import capture, format

link = capture.test_connection(input('Digite qual o link do resumo? '))
site_pb = capture.capture_html(link)
site_en = capture.capture_html(link.replace('pt', 'en'))
site_es = capture.capture_html(link.replace('pt', 'es'))
original = capture.get_original_link(site_pb)
print(original)


caminho = "D:\Programas\ "
format.txt_facebook(link, caminho, site_pb)
format.txt_twitter(link, caminho, site_pb, site_en)
format.txt_interface(link, caminho, site_pb, site_en, site_es)
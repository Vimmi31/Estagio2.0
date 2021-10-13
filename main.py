import capture
import formating

abstract = capture.Capture(input('Digite o link do artigo: '))
abstract.test_connection()
abstract.capture_html()
a = abstract.get_title()
print(a)



caminho = 'C:/Users/Vinicius/Desktop/Estagio2.0/Estagio2.0/Text/ '



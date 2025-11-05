from googletrans import Translator

tradutor = Translator()

mensagem_pt_br = "Olá Mundo, muito obrigado por me receber Python! juntos realizaremos maravilhas na programação."

traducao = tradutor.translate(mensagem_pt_br, dest='en')

print(f'Texto Original: {traducao.origin}')
print(f'Idioma de Origem: {traducao.src}')
print(f'Texto Traduzido: {traducao.text}')
print(f'Idioma de destino: {traducao.dest}')
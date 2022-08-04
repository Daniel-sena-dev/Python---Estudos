mensagem = input('Digite uma frase: ').strip()

print({mensagem.lower().count('a')})
print(mensagem.lower().find('a')+1)
print(mensagem.rfind('a')+1)

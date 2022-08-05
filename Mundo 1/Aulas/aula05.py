#MANIPULANDO CADEIAS DE TEXTO
frase = 'Curso em vídeo python'

#FATIAMENTO
print(frase[0:5])
print(frase[0:5:2])
print(frase[:5])
print(frase[8:])
print(frase[9::3])

#ANÁLISE
print(len(frase)) #tamanho da string
print(frase.count('o')) #Vai contar quantos a letra o aparece
print(frase.count('o', 0, 13)) #contagem com fatiamento
print(frase.find('deo')) #vai encontrar a posição da frase "se retornar -1 quer dizer que nao foi encontrado"
print('Curso' in frase)

#Transformação
print(frase.replace('python', 'Android')) #vai substituir python por android
print(frase.upper()) #coloca em caixa alta
print(frase.lower()) #colocar em minusculo
print(frase.capitalize()) #Vai capitalizar a frase
print(frase.title()) #Ele vai capitalizar a primeira letra de cada frase

frase2 = '   Aprendendo Python   '
print(frase2.strip()) #remove espaços em brancos (rstrip remove espaços da direita, lstrip remove da esquerda)

#Divisão
print(frase.split()) #cria uma divisão entre os espaços
print('-'.join(frase)) #muda a configuração

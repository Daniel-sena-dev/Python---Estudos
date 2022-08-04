frase = input('Digite uma frase: ').lower()
fraseTratada = frase.replace(' ', '')
tamanhoFrase = len(fraseTratada)
fraseContraria =''.join(reversed(fraseTratada)) #inverter uma string
letrasIguais = 0

for contador in range(0, tamanhoFrase):

    if fraseTratada[contador] == fraseContraria[contador]:
        letrasIguais += 1

print(letrasIguais)

if letrasIguais == tamanhoFrase:
    print('A frase é um palíndromo! ')
else:
    print('A frase não é um palídromo! ')


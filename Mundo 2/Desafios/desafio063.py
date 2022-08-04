quantidadeTermos = int(input('Digite a quantidade de termos que você deseja: '))
anterior = 0
proximo = 1
atual = 0

while quantidadeTermos != 0:
    #A variavel atual recebe o valor do proximo
    atual = proximo
    #Valor anterior é printado
    print(anterior, end=' -> ')
    #Proximo recebe o valor atual dele + o valor anterior
    proximo = proximo + anterior
    #Anterior recebe o valor da variavel atual(proximo)
    anterior = atual
    #Contador e reduzido
    quantidadeTermos -= 1

print('Esta é a sequencia de fibonnaci')

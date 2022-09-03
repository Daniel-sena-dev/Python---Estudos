print('37- Senso academia: ')
codigo = list()
altura = list()
peso = list()
contador = 0
sair = False
maisPesada = maisLeve = maisAlta = maisBaixa = 0

while True:
    while True:
        try:
            codigo.append(int(input('Digite o seu codigo: ')))
        except ValueError:
            print('ERRO! valor invalido')
        else:
            if 0 < codigo[contador] < 1000:
                print('Codigo válido!')
                break
            elif codigo[contador] == 0:
                sair = True
                codigo.pop()
                break
            else:
                print('Codigo invalido!')
    if sair:
        break

    while True:
        try:
            altura.append(int(input('Digite o sua altura: ')))
        except ValueError:
            print('ERRO! valor invalido')
        else:
            if 0 < altura[contador]:
                print('altura válida!')
                break
            else:
                print('altura invalida!')

    while True:
        try:
            peso.append(int(input('Digite o seu peso: ')))
        except ValueError:
            print('ERRO! valor invalido')
        else:
            if 0 < peso[contador]:
                print('peso válido!')
                break
            else:
                print('peso invalido!')

    contador += 1

maisAlta = altura.index(max(altura))
maisBaixa = altura.index(min(altura))
maisPesada = peso.index(max(peso))
maisLeve = peso.index(min(peso))

print(codigo)
print(f'A pessoa mais alta foi {codigo[maisAlta]} com {max(altura)}m e a mais baixa é {codigo[maisBaixa]} com {min(altura)}m')
print(f'A pessoa mais pesada foi {codigo[maisPesada]} com Kg {max(peso)} e a mais leve é {codigo[maisLeve]} com Kg {min(peso)}')

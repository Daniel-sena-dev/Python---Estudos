import time

ordem = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
listaSaltos = list()
media = 0
atletas = list()
listaMedias = list()

while True:
    nome = str(input('Digite o nome do atleta (não digite nada para sair do programa): ')).strip()
    if nome == '':
        time.sleep(0.5)
        print('Finalizando', end='')
        for cont in range(0, 3):
            time.sleep(0.5)
            print('.', end='')
        print('')
        break
        
    atletas.append(nome)
    for cont in range(0, 5):
        while True:
            try:
                salto = float(input(f'{ordem[cont]} Salto: '))
            except ValueError:
                print('ERRO! Digite um valor valido')
            else:
                if salto > 0:
                    listaSaltos.append(salto)
                    break

    print(f'Melhor salto: {max(listaSaltos)}')
    print(f'Pior salto: {min(listaSaltos)}')
    listaSaltos.remove(max(listaSaltos))
    listaSaltos.remove(min(listaSaltos))
    for cont in range(0, 3):
        media += listaSaltos[0]
    listaMedias.append(media/3)
    print(f'Média dos demais saltos: {media/3:.02f}')
    listaSaltos.clear()
    media = 0

print('Resultado final: ')
for cont in range(0, len(atletas)):
    print(f'{atletas[cont]}: {listaMedias[cont]:.02f}')

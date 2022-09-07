print('47- Programa para calcular media de atletas: ')
listaNotas = list()
listaNomes = list()
atleta = notas = 0


atleta = str(input('Digite o nome do atleta: '))
# Coletando notas
for cont in range(0, 7):
    # Verificando notas
    while True:
        try:
            notas = float(input(f'{cont+1}º Nota: '))
        except ValueError:
            print('ERRO! Digite um valor valido')
        else:
            if notas > 0:
                listaNotas.append(notas)
                break
            else:
                print('Digite um valor valido!')

# SAIDA
print('Resultado final: ')
print(f'Atleta: {atleta}')
print(f'Melhor nota: {max(listaNotas)}')
print(f'Pior nota: {min(listaNotas)}')
# Removendo a melhor e pior nota:
listaNotas.remove(max(listaNotas))
listaNotas.remove(min(listaNotas))
media = 0
for cont in range(0, 5):
    media += listaNotas[cont]
print(f'Média: {media/5:.02f}')

import time
print('40- Programa para coleta de dados de uma cidade: ')
codigoCidade = list()
veiculosPasseio = list()
vitimasTransito = list()
mediaVeiculos = mediaAcidentes = tamanhoTotal = 0

for cont in range(0, 5):
    codigoCidade.append(int(input('Digite o codigo da cidade: ')))
    veiculosPasseio.append(int(input('Digite a quantidade de veiculos a passeio: ')))
    vitimasTransito.append(int(input('Digite a quantidade de vitimas em acidentes de transito: ')))
    mediaVeiculos += veiculosPasseio[cont]

    if veiculosPasseio[cont] < 2000:
        mediaAcidentes += vitimasTransito[0]
        tamanhoTotal += 1

maiorAcidentes = vitimasTransito.index(max(vitimasTransito))
menorAcidentes = vitimasTransito.index(min(vitimasTransito))
mediaVeiculos /= 5
mediaVeiculos /= tamanhoTotal

print(f'ESTATISTICA DE TRANSITOS:')
time.sleep(1)
print(f'Cidade com maior numero de acidentes: {codigoCidade[maiorAcidentes]} - {max(vitimasTransito)}')
time.sleep(1)
print(f'Cidade com menor numero de acidentes: {codigoCidade[menorAcidentes]} - {min(vitimasTransito)}')
time.sleep(1)
print(f'A media de veiculos das cinco cidades foi de {mediaVeiculos:.02f}')
time.sleep(1)
print(f'A media de acidentes de transito na cidades com menos de 2000 veiculos: {mediaAcidentes:.02f}')

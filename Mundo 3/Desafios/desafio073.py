tabelaBrasileirao = ('palmeiras', 'corinthians', 'fluminense', 'athletic-PR', 'flamengo', 'internacional', 'atletico-MG', 'bragantino', 'santos', 'são paulo', 'goias', 'botafogo', 'america-mg', 'ceara SC', 'coritiba', 'avaí', 'cuiaba', 'fortaleza', 'atletico-go', 'juventude')
#Primeiros colocados
posicao = 1
print('-=-' * 20)
print('Primeiros colocados da serie A: ')
for colocados in range(0, 5):
    print(f'O {posicao}º colocado: {tabelaBrasileirao[colocados]}')
    posicao += 1

print('-=-' * 20)
#Os ultimos colocados
print('Ultimos quatro colocados da serie A: ')
posicao = 16
for colocados in range(15, 20):
    print(f'O {posicao}º colocado: {tabelaBrasileirao[colocados]}')
    posicao += 1
print('-=-' * 20)
#ordem alfabetica
print('Tabela da serie A em ordem alfabetica: ')
print(sorted(tabelaBrasileirao))
print('-=-' * 20)

#onde está seu time?
time = input('\033[4mDigite o nome do seu time é veja em qual posição ele está!\033[m ').lower()

if time in tabelaBrasileirao:
    print(f'O {time} está na posição {tabelaBrasileirao.index(time)+1}')
else:
    print('O time foi rebaixado!')
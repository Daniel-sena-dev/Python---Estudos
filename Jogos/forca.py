# JOGO DA FORCA
import collections
import modulos

modulos.menus('BEM VINDO AO JOGO DA FORCA!')
palavraSecreta = modulos.sorteador()
ganhou = True
# Criando uma lista para armazenar o tamanho da palavra escolhida
tamanhoPalavra = list()
vidas = 6
for contador in range(0, len(palavraSecreta)):
    tamanhoPalavra.append('_')
# ======================================================
while True:
    # Mostrando a quantidade de letras:
    for contador in tamanhoPalavra:
        print(f'{contador}', end='')
    print(' ')
    print('-=-' * 10)

    # Verificando se o jogador ganhou
    if collections.Counter(tamanhoPalavra) == collections.Counter(palavraSecreta):
        break
    # Verificando se o jogador perdeu
    if vidas == 0:
        ganhou = False
        break

    # Validação de entrada:
    while True:
        try:
            letra = input('Digite uma letra: ').lower()[0]
        except IndexError:
            print('ERRO! Digite uma letra')
        else:
            if letra.isalpha():
                break
            else:
                print('Digite apenas letras! valores numericos não seram aceitos!')
                continue

    # Verificando se a letra está na palavra
    if letra in palavraSecreta:
        print('Parabens! você acertou!')
        # Adicionando a lista final
        for contador in range(0, len(palavraSecreta)):
            if letra == palavraSecreta[contador]:
                tamanhoPalavra[contador] = letra
    else:
        print('Errou!')
        vidas -= 1


if ganhou:
    print('Você ganhou')
else:
    print(f'Você perdeu, a palavra era {palavraSecreta}')

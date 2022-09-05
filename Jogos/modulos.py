# Criação de linhas
import random


def linhas(txt):
    tamanho = len(txt)
    print('-' * tamanho)


# Criação de menus
def menus(txt):
    linhas(txt)
    print(txt)
    linhas(txt)


# Sorteador de palavras
def sorteador():
    listaPalavras = ['banana', 'fruta', 'maça', 'uva', 'carro', 'cachorro', 'gato', 'puxador',
                     'sincero', 'fofoca', 'carnaval', 'cercado', 'idoso', 'compositor',
                     'aviao', 'python', 'javascript', 'html', 'css', 'praia', 'universidade', 'lua',
                     'coraçao', 'pulmao', 'olho', 'cabeça', 'barco']
    sortNum = random.randint(0, len(listaPalavras) - 1)
    return listaPalavras[sortNum]

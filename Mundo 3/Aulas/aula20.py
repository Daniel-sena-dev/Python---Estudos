# MODULOS
import aula20_1
#from uteis import fatorial, dobro

num = int(input('Digite um valor: '))
fato = aula20_1.fatorial(num)
print(f'O fatorial de {num} é {fato}')
print(f'O dobro de {num} é {aula20_1.dobro(num)}')

# Exercicios de estrutura sequencial do site python Brasil
import math

print('1- Programa que mostre mensagem na tela:')
print('Alo mundo')
print('-' * 20)

print('2- Programa que peça um numero e entao mostre a mensagem')
numero = int(input('Digite um numero: '))
print(f'O número informado foi {numero}')
print('-' * 20)

print('3- Programa de soma')
numeroSoma1 = int(input('Digite um número: '))
numeroSoma2 = int(input('Digite um número: '))
print(f'A soma de {numeroSoma1} + {numeroSoma2} = {numeroSoma1 + numeroSoma2}')
print('-' * 20)

print('4- Media de 4 notas')
nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
nota3 = int(input('Digite a terceira nota: '))
nota4 = int(input('Digite a quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4)/4
print(f'A mediaVeiculos das notas foi {media:.02f}')
print('-' * 20)

print('5- Converter metros para centimetros')
metros = float(input('Informe metros: '))
print(f'{metros}m == {metros*100}cm')
print('-' * 20)

print('6- Programa para calcular a area de um circulo')
raio = float(input('Digite o raio do circulo: '))
print(f'A area do circulo foi: {math.pi * (raio ** 2):.02f}')
print('-' * 20)

print('7- Programa que calcula a area de um quadrado: ')
comprimento = float(input('Digite o comprimento do quadrado: '))
largura = float(input('Digite a largura do quadrado: '))
area = comprimento * largura
dobro = area * 2
print(f'A area do quadrado é {area}m² e o dobro é de {dobro}m²')
print('-' * 20)

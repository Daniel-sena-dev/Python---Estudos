print('Programa para calcular mediaVeiculos 2.0v')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
if media == 10:
    print('O aluno foi aprovado com distinção!')
elif media >= 7:
    print('O aluno foi aprovado por média')
else:
    print('O aluno foi reprovado!')

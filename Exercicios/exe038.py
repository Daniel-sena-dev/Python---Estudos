print('14- Programa para media de alunos 3.0v')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 9:
    print(f'a nota do aluno foi {nota1} + {nota2} = {media}')
    print(f'O conceito foi A, o aluno foi APROVADO')
elif media >= 7.5:
    print(f'a nota do aluno foi {nota1} + {nota2} = {media}')
    print(f'O conceito foi B, o aluno foi APROVADO')
elif media >= 6.0:
    print(f'a nota do aluno foi {nota1} + {nota2} = {media}')
    print(f'O conceito foi C, o aluno foi APROVADO')
elif media >= 4.0:
    print(f'a nota do aluno foi {nota1} + {nota2} = {media}')
    print(f'O conceito foi D, o aluno foi REPROVADO')
else:
    print(f'a nota do aluno foi {nota1} + {nota2} = {media}')
    print(f'O conceito foi E, o aluno foi REPROVADO')
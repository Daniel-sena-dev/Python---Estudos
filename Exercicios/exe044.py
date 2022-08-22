print('20- Programa leitura para 3 notas de um aluno 3.0v')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
media = (nota1 + nota2 + nota3)/3

if 7 <= media < 10:
    print(f'A media foi {media:.02f}, aluno APROVADO ')
elif media < 7:
    print(f'A media foi {media:.02f}, aluno REPROVADO')
else:
    print(f'A media foi {media:.02f}, aluno APROVADO COM DISTINÇÃO')

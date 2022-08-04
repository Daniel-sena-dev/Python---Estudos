nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2

if media >= 6:
    print(f'Sua media foi {media}, Aprovado por nota')
if media <= 5:
    print(f'Sua media foi {media}, Reposição')
else:
    print(f'Sua media foi {media}, Reprovado')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2

if media < 5:
    print(f'\033[1mREPROVADO\033[m sua media foi \033[1m{media:.02f}\033[m')
elif media >= 5 and media <= 6.9:
    print(f'Sua media foi \033[1m{media:.02f}\033[m, você está de recuperação')
else:
    print(f'Você está aprovado! \033[1m{media:.02f}\033[m')


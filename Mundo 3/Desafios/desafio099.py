import random


def maior(*num):
    print('-=-' * 10)
    print('Analisando os valroes passados...')
    for i in num:
        print(i, end=' ')
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}')
    print('-=-' * 10)


maior(random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))

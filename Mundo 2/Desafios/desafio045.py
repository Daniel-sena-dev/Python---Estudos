import random


jogadaComputador = random.randint(1, 3)
print('-=-' * 20)
print('\033[1;040;0127mVamos jogar pedra, papel e tesoura ?\033[m')
print('[1] - Pedra \n[2] - Papel \n[3] - Tesoura')
print('-=-' * 20)
jogadaPlayer = int(input('Digite sua jogada: '))


#jogadas = ('Pedra', 'Papel', 'Tesoura')

if jogadaPlayer == jogadaComputador:
    print('Pedra, papel e tesoura!')
    print('\033[1mDeu empate\033[m')
#Vitoria player
elif jogadaPlayer == 1 and jogadaComputador == 3:
    print('Pedra, papel e tesoura!')
    print(f'Você jogou \033[1;030;107mpedra\033[m e o computador jogou \033[1;030;107mtesoura\033[m!')
    print('Parabens voce ganhou!')
elif jogadaPlayer == 2 and jogadaComputador == 1:
    print('Pedra, papel e tesoura!')
    print(f'Você jogou \033[1;030;107mpapel\033[m e o computador jogou \033[1;030;107mpedra\033[m!')
    print('Parabens voce ganhou!')
elif jogadaPlayer == 3 and jogadaComputador == 2:
    print('Pedra, papel e tesoura!')
    print(f'Você jogou \033[1;030;107mtesoura\033[m e o computador jogou \033[1;030;107mpapel\033[m!')
    print('Parabens voce ganhou!')
#=======================================================================
#Derrota player
elif jogadaPlayer == 3 and jogadaComputador == 1:
    print('Pedra, papel e tesoura!')
    print(f'Você jogou \033[1;030;107mpedra\033[m e o computador jogou \033[1;030;107mtesoura\033[m!')
    print('GAME OVER!')
elif jogadaPlayer == 1 and jogadaComputador == 2:
    print('Pedra, papel e tesoura!')
    print(f'Você jogou \033[1;030;107mpapel\033[m e o computador jogou \033[1;030;107mpedra\033[m!')
    print('GAME OVER!')
elif jogadaPlayer == 2 and jogadaComputador == 3:
    print('Pedra, papel e tesoura!')
    print(f'Você jogou \033[1;030;107mtesoura\033[m e o computador jogou \033[1;030;107mpapel\033[m!')
    print('GAME OVER!')
#========================================================================
#JOGADA INVALIDA
else:
    print('JOGADA INVALIDA')

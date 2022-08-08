def interactiveHelp():
    import time
    while True:
        print('\033[1;107;42m~\033[m' * 40)
        print('        \033[1;107;42mSISTEMA DE AJUDA PyHelp\033[m')
        print('\033[1;107;42m~\033[m' * 40)
        comando = input('Função ou Biblioteca > ')
        if comando.upper() in 'FIM':
            print('ATÉ LOGO!')
            break
        else:
            time.sleep(0.5)
            print('\033[1;107;44m~\033[m' * 60)
            print(f"         \033[1;107;44mAcessando o manual do comando '{comando}'\033[m ")
            print('\033[1;107;44m~\033[m' * 60)
            time.sleep(1)
            print(help(f'{comando}'))


interactiveHelp()

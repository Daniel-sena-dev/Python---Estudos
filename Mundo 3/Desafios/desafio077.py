palavras = ('aprender', 'programar', 'linguagem', 'python',
            'javascript', 'estudar', 'praticar', 'programador',
            'futuro', 'trabalhar', 'mercado')
tamanhoLista = len(palavras)

#Primeiro for vai pegar cada palavra da tupla e passar para o contador
for contador in palavras:
    #A palavra que foi armazenada no contador é printada na tela
    print(f'\nNa palavra {contador.upper()} temos ', end='')
    #O segundo for pega a palavra armazenada
    for letra in contador:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')


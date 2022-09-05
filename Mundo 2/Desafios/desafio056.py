pessoas = 4
somaIdade = 0
vinteMulheres = 0
idadeHomem = 0
nomeHomem = ''
for contador in range(0, pessoas):
    nome = input('Digite seu nome: ')
    idade = int(input(f'{nome} digite sua idade: '))
    print(f'{nome}, Qual é o seu sexo? digite\n [M] para masculino \n [F] para femino')
    sexo = input('Digite: ').lower()

    #soma das idades p/ mediaVeiculos
    somaIdade += idade

    if sexo == 'f' and idade < 20:
        vinteMulheres += 1
    elif sexo == 'm' and idade > idadeHomem:
        idadeHomem = idade
        nomeHomem = nome
#MEDIA IDADES
media = somaIdade / pessoas
print(f'A media de idade do grupo foi de {media}')

#Qual o homem mais velho
print(f'{nomeHomem} é o mais velho e tem {idadeHomem} anos')

#Quantidade de mulher abaixo dos 19
print(f'A quantidade de mulheres com menos de 20 anos é {vinteMulheres}')

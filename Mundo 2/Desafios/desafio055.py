peso = float(input('Digite seu peso: '))
maisPeso = peso
menosPeso = peso
pessoas = 4

for contador in range(0, pessoas):
    peso = float(input('Digite seu peso: '))

    if peso > maisPeso:
        maisPeso = peso

    if peso < menosPeso:
        menosPeso = peso

print(maisPeso)
print(menosPeso)
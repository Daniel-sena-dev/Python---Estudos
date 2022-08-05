#LISTAS COMPOSTAS
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])
print(pessoas[2][:])

#==========================================================
teste = list() # Criei a lista
teste.append('Daniel') # Adicionei elemento
teste.append(23) # Adicionei elemento
galera = list() #Criei outra lista
galera.append(teste[:]) # Coloquei a lista teste dentro da lista galera
teste[0] = 'Maria' # Adicionei elemento
teste[1] = 22 # Adicionei elemento
galera.append(teste[:])  # Coloquei a lista teste dentro da lista galera
print(galera) # Printei
#=============================================================

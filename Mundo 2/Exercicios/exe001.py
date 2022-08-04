cedulaCinquenta = 0
cedulaVinte = 0
cedulaDez = 0
cedulaUm = 0
valorSacado = 234

if valorSacado // 50:
    cedulaCinquenta = valorSacado // 50
    valorSacado = valorSacado - (valorSacado // 50)*50
if valorSacado // 20:
    cedulaVinte = valorSacado // 20
    valorSacado = valorSacado - (valorSacado//20)*20
if valorSacado // 10:
    cedulaDez = valorSacado // 10
    valorSacado = valorSacado - (valorSacado//10)*10
if valorSacado // 1:
    cedulaUm = valorSacado // 1
    valorSacado = valorSacado - (valorSacado//1)/1

print(valorSacado)
print(f'Cinquenta: {cedulaCinquenta}')
print(f'Vinte: {cedulaVinte}')
print(f'Dez: {cedulaDez}')
print(f'Um: {cedulaUm}')

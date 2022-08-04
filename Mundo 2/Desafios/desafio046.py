import time
import datetime

anoAtual = datetime.date.today().year

for contador in range(10, -1, -1):
    print(contador)
    time.sleep(1)

print(f' 🎆 FELIZ {anoAtual}! 🎆')


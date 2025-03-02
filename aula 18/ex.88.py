from random import randint
from time import sleep
games = list()
lista = []
x = 0
quantidades = int(input('Quantos jogos você quer: '))
for c in range(quantidades):
    while x < 6:
        games.append(randint(1,60))
        if games[-1] in games[:-1]:
            games.pop()
        else:
            x += 1
    lista.append(games[:])
    games.clear()
    x = 0
print(f'SORTEANDO {quantidades} JOGOS')
for y in range(quantidades):
    sleep(1)
    print(f'JOGO {y + 1}:', lista[y])
sleep(1)
print('BOA SORTE :)')
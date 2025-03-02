lista = list()
dados = []
x = 0
while True:
    lista.append(str(input('Nome: ')))
    lista.append(int(input('Peso: ')))
    continuar = input('Continuar? [Y/N] ').upper().strip()
    dados.append(lista[:])
    lista.clear()
    if 'N' in continuar:
        break
maior = menor = 0
pesos = []
for x in range(len(dados)):
    pesos.append(dados[x][1])

for y in range(len(dados)):
    if y == 0:
        maior = menor = pesos[y]
    else:
        if pesos[y] > maior:
            maior = pesos[y]
        elif pesos[y] < menor:
            menor = pesos[y]
leve = []
pesado = []
for c in range(len(dados)):
    if dados[c][1] == maior :
        pesado.append(dados[c][0])
    elif dados[c][1] == menor:
        leve.append(dados[c][0])

print(f'Pessoas cadastradas: {len(dados)}')
print(f'O maior peso foi {maior} peso de {pesado}')
print(f'O Menor pso foi {menor} peso de {leve}')
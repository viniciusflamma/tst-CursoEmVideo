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

leve = []
pesado = []
for c in range(len(dados)):
    if dados[c][1] >= 100:
        pesado.append(dados[c][0])
    elif dados[c][1] <= 70:
        leve.append(dados[c][0])

print(f'Pessoas cadastradas: {len(dados)}')
print(f'Pessoas pesadas: {pesado}')
print(f'Pessoas leves: {leve}')
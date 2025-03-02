x = 1
notas = list()
boletim = []
aluno = []
while True:
    nome = (str(input(f'Nome do {x}º aluno: ')))
    nota1 = float(input('1ª NOTA: '))
    nota2 = float(input('2ª NOTA: '))
    notas.append(nota1)
    notas.append(nota2)
    aluno.append(nome)
    aluno.append(notas[:])
    boletim.append(aluno[:])
    notas.clear()
    aluno.clear()
    x += 1
    continuar = str(input('CONTINUAR? [Y/N]: ')).upper()
    if continuar in 'N':
        break
#boletim = [['vini', [9, 8]], ['marcos', [6, 7]], ['josé', [10, 5]], ['armando', [3, 1]]]
print('=========================')
print('Nº -- NOME -------- MÉDIA')
print('-------------------------')
for a in range(len(boletim)):
    print(a + 1, end=' ')
    #print('   {}{}'.format(boletim[a][0], ' ' * (15 - len(boletim[a][0]))), end=' ')
    print(f'    {boletim[a][0]:<15}', end=' ')
    media = (boletim[a][1][0] + boletim[a][1][1]) / 2
    print(media)
while True:
    nota_aluno = int(input('Mostrar notas do aluno: (999 para encerrar): '))
    if nota_aluno == 999:
        break
    print(f'Notas de {boletim[nota_aluno - 1][0]}: {boletim[nota_aluno - 1][1]}')
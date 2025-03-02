matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for a in range(3):
    for b in range(3):
        matriz[a][b] = int(input(f'Entre a value for [{a}, {b}]: '))
for a in range(0, 3):
    for b in range(0, 3):
        print(f'[{matriz[a][b]:^5}]', end='')
    print()
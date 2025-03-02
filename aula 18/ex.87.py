matriz = [[], [], []]
for a in range(3):
    for b in range(3):
        num = int(input(f'Entre a value for [{a}, {b}]: '))
        matriz[a].append(num)
for a in range(3):
    for b in range(3):
        print(f'[  {matriz[a][b]}  ]', end='')
    print('')
even = 0
add = 0
greater = 0
for a in range(3):
    for b in range(3):
        if matriz[a][b] % 2 == 0:
            even += matriz[a][b]
        if b == 2:
            add += matriz[a][b]
        if a == 1:
            if greater < matriz[a][b]:
                greater = matriz[a][b]
print(f'The sum of the even values is: {even}')
print(f'The sum of the values in the third column is: {add}')
print(f'The largest value in the second row is: {greater}')

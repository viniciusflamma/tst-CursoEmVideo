c = 1
numbers = [[], []]
while c < 8:
    num = int(input(f'Enter the {c}st Value: '))
    if num % 2 == 0:
        numbers[0].append(num)
    else:
        numbers[1].append(num)
    c += 1
numbers[0].sort()
numbers[1].sort()
print(f'The even values were: {numbers[0]}')
print(f'The odd values were: {numbers[1]}')

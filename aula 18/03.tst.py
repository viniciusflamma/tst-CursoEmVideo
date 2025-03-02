numbers = str(input('Number: '))
lista = list(numbers)
lista.sort()
num = []
for x in range(len(lista)):
    num.append(int(lista[x]))
print(num)

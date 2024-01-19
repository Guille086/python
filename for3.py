
for x in range(5):
    print("*" * 5)

for x in range(5):
        print("*" * (x+1))

for x in range(5):
    if x == 0 or x == 4:
        print("* " * 5)
    else:
        print("*       *")

# solo bordes
fila = 5
columna = 5
tablero = [
    ['h', 'o', 'l', 'a', 's'],
    ['o', 's', 'm', 'a', 'l'],
    ['l', 'u', 'c', 'h', 'i'],
    ['a', 'i', 'r', 'a', 'm'],
    ['s', 'l', 'i', 'm', 'e']
    ]
for f in range(fila):
    for c in range(columna):
        if(f == 0 or f == (fila - 1) or c == 0 or c == (columna-1)):
            print(tablero[f][c], end= ' ')
        else:
            print(" ", end=' ')
        print(" ", end= ' ')
    print(end ='\n')
inicio = int(input("Ingrese el inicio"))
limite = int(input("Ingrese el límite"))


for x in range(inicio, limite):
    if(x % 2 == 0):
        print("| ",x)
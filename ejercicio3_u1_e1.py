# Operadores aritméticos
# imprimir la suma de 3 + 4
print("La suma de 3 + 4 es: ", 3 + 4)

# Resolver todas las operaciones: 10 - 4, 10*4, 10/4, 10%4, 10//4, 10**4
print("La resta de 10 - 4 es: ", 10 - 4)
print("La multiplicación de 10 X 4 es: ", 10*4)
print("El cociente de 10/4 es: ", 10/4)
print("El resto de la división 10/4 es: ", 10%4)
print("El cociente entero de 10/4 es: ", 10//4)
print("La potencia de 10**4 es: ", 10**4)

# Resolver la ecuación cuadrática 2x^2 - 7x + 3 = 0
a = 2
b = -7
c = 3
x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
print("Los dos valores posibles para x son: x1 = ", x1, "x2 = ", x2)

#Operaciones con cadena de texto
print("SNPP " + "CTFPP " + "PROGRAMACIÓN PYTHON")

#Operaciones mixtas
print("Tun chi" * 5)
print("Ja" * (2 ** 3))

# Operadores de comparación
print(3>4)
print(3<4)
print(3>=4)
print(4<=4)
print(3==4)
print(3!=4)
#Operaciones con cadenas de texto
print("python" > "PYTHON")
print("aaaa" >= "aaba") # Ordenación alfabética por ASCII
print(len("aaaa") >= len("aaba")) # Cuenta caracteres

print("python" != "PYTHON")

###Operadores lógicos

print(10 > 4 and "Z" > "A")
print(10 > 4 or "Z" > "A")
print(not(10 > 4 and "Z" > "A"))
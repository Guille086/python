valor1 = int(input("Ingrese un número entero"))
valor2 = int(input("Ingrese otro entero"))

if(valor1>valor2):
    print("El mayor es: ", valor1)
    if(valor1 % 2 == 0):
        print("El número es PAR", valor1)
    else:
        print("El número es IMPAR")
elif(valor1 < valor2):
    print("{} es mayor a {}".format(valor2,valor1))
    if(valor2 % 2 == 0):
        print("El número es par")
    else:
        print("El número es impar")
else:
    print("Los números ingresados son iguales")
print("------------------------------------")
usuario = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")
if(usuario == "admin" and password == "12345"):
    print("Acceso correcto")
else:
    print("Acceso denegado")
import random

while True:
    aleatorio = random.randrange(0, 3)
    eligePc = ""
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    opcion = int(input("Elige tu opción "))

    if opcion == 1:
        eligeusuario = "Piedra"
    elif opcion == 2:
        eligeusuario = "Papel"
    elif opcion == 3:
        eligeusuario = "Tijera"
    print("Elegiste: ", eligeusuario)

    if aleatorio == 0:
        eligePc = "Piedra"
    if aleatorio == 1:
        eligePc = "Papel"
    if aleatorio == 2:
        eligePc = "Tijera"
    print("La máquina eligió: ", eligePc)
    print("...")
    if eligePc == "Piedra" and eligeusuario == "Papel":
        print("Ganaste, papel envuelve Piedra")
    elif eligePc == "Papel" and eligeusuario == "Tijera":
        print("Ganaste, Tijera corta Papel")
    elif eligePc == "Tijera" and eligeusuario == "Piedra":
        print("Ganaste, Piedra machaca tijera")
    elif eligePc == "Papel" and eligeusuario == "Piedra":
        print("Perdiste, Papel envuelve Piedra")
    elif eligePc == "Tijera" and eligeusuario == "Papel":
        print("Perdiste, Tijera corta Papel")
    elif eligePc == "Piedra" and eligeusuario == "Tijera":
        print("Perdiste, Piedra machaca tijera")
    elif eligePc == eligeusuario:
        print("Empate")
    
import os
resp = 1
while resp != 0:
    print("Paint (1)")
    print("Calc (2)")
    print("Apagar PC en 2 horas (3)")
    print("Spotify (4)")
    print("Bloc de Notas (5)")
    print("Juegos (6)")
    print("Ver propiedades del sistema (7)")
    print("Personalización de Windows (8)")
    print("Google Chrome(9)")
    print("Salir (0)")
    resp = int(input("Seleccione: "))
    if(resp == 1):
        os.system("mspaint")
    elif(resp == 2):
        os.system("calc")
    elif(resp == 3):
        os.system("shutdown -s -t 7200")
    elif(resp == 4):
        os.system("start spotify")
    elif(resp == 5):
        os.system("notepad")
    elif(resp == 6):
        os.system("joy.cpl")
    elif(resp == 7):
        os.system("sysdm.cpl")
    elif(resp == 8):
        os.system("control color")
    elif(resp ==9):
        os.system("start chrome")
    else:
        print("No entiendo esa orden")


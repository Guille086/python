calificaciones = [1,2,3,4,5]
nombres = ["Moisés","Camila","Fernanda","Pablo","Tania"]
lista_variada = [True, 10.5, "abc", [0,1,1]]

print("Estudiante: ", nombres[2])
print("Calificación: ", calificaciones[-2])
print("Lista dentro de otra", lista_variada[3][0])
print("Imprimir un rango de slices", nombres[1:2])
print(lista_variada)

#agregar elementos a una lista
nombres.append("Anibal")
print(nombres)
#remover elementos de una lista
nombres.remove("Anibal")
print(nombres)
from biblioteca import Biblioteca
from libro import Libro

if __name__ == '__main__':
    ejecutar = True

    while ejecutar:
        print("- - - BIENVENIDO AL SISTEMA BIBLIOTECARIO - - -")
        opcion = int(
            input(
                "¿Qué vas a hacer?: \n1-Crear Biblioteca \n2-Agregar libro \n3-Ver Catálogo \n4-Quitar libro \n5-Salir \n:"
            )
        )
        if opcion == 1:
            nombre = input("Nombre de la biblioteca: ")
            biblioteca = Biblioteca(nombre)

            print(
                "Se creó la biblioteca: {}".format(
                    biblioteca.consultar_nombre_biblioteca()
                )
            )

        elif opcion == 2:
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            cantidad_de_paginas = input("Páginas: ")
            genero = input("Género: ")
            sinopsis = input("Sinopsis: ")

            libro = Libro(titulo, autor, cantidad_de_paginas, genero, sinopsis)
            biblioteca.agregar_libro(libro)

        elif opcion == 3:
            print("Catálogo de libros: ")
            for i in biblioteca.consultar_libros():
                print(i)

        elif opcion == 4:
            indice = int(input("Id del libro a eliminar: "))
            biblioteca.quitar_libro(indice)

        elif opcion == 5:
            print("Gracias por vistar. \n ;)")
            ejecutar = False

        else:
            print("Opción incorrecta")
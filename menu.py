from pack_input_mod.input import *
from os import system
from input_funcion import *
from peliculas import *
from archivos_peliculas import *

def menu_peliculas():
    """funcion del menu del programa, es el que llama a todas las demas funciones y las coordina para
    su correcta ejecucion
    """
    lista_peliculas = leer_csv("peliculas.csv")

    lista_opciones = ["Dar de alta", "Modificar", "Eliminar", "Mostrar peliculas", "Ordenar peliculas", "Buscar pelicula por titulo", "Calcular", "Calcular porcentaje", "Salir"]
    mensaje_ingreso = "Debe tener minimo UNA pelicula ingesada para poder usar el programa."
    print("Bienvenido, estas son sus opciones:")
    while True:
        for i in range(len(lista_opciones)):
            print(f"{i+1}_ {lista_opciones[i]}.")
        opcion = get_int( "Seleccione cual es la opcion que desee: ", "Error, ingrese una opcion valida:", 1, 9, 5)
        match opcion:
            case 1:
                id_peliculas =  generar_id("ids.json")
                pelicula = ingresar_peliculas(id_peliculas, lista_peliculas)
                lista_peliculas.append(pelicula)
                
                system("pause")
                system("cls")
            case 2:
                try:
                    if len(lista_peliculas) >= 1:
                        modificar_pelicula(lista_peliculas)
                    else:
                        print(mensaje_ingreso)
                except:
                    pass
                system("pause")
                system("cls")
            case 3:
                try:
                    if len(lista_peliculas) >= 1:
                        eliminar_pelicula(lista_peliculas)
                    else:
                        print(mensaje_ingreso)
                except:
                    pass
                system("pause")
                system("cls")
            case 4:
                try:
                    if len(lista_peliculas) >= 1:
                        tipos_de_mostrar(lista_peliculas)
                    else:
                        print(mensaje_ingreso)
                except:
                    pass
                system("pause")
                system("cls")
            case 5:
                try:
                    if len(lista_peliculas) >= 1:
                        ordenar(lista_peliculas)
                    else:
                        print(mensaje_ingreso)
                except:
                    pass
                system("pause")
                system("cls")
            case 6:
                try:
                    if len(lista_peliculas) >= 1:
                        buscar_por_titulo(lista_peliculas)
                    else:
                        print(mensaje_ingreso)
                except:
                    pass
                system("pause")
                system("cls")
            case 7:
                try:
                    if len(lista_peliculas) >= 1:
                        calcular(lista_peliculas)

                    else:
                        print(mensaje_ingreso)
                except:
                    pass
                system("pause")
                system("cls")
            case 8:
                try:
                    if len(lista_peliculas) >= 1:
                        porcentaje(lista_peliculas)
                    else:
                        print(mensaje_ingreso)
                except:
                    pass
                system("pause")
                system("cls")
            case 9:
                guardar_listado("peliculas.csv", lista_peliculas)
                system("cls")
                print("Gracias por usar el programa ;)")
                system("pause")
                system("cls")
                break


                


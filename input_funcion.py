from pack_input_mod.input import *
from datetime import date
from ingreso_datos import *


def registrar_pelicula(id: int, titulo: str, genero: str, año_lanzamiento: int, duracion: int, atp: bool, plataforma: list[str])-> dict:
    """funcion que obtiene los datos de la pelicula para componerlos en un diccionario

    Args:
        id (int): id unico de la pelicula
        titulo (str): titulo de la pelicula
        genero (str): genero de la pelicula
        año_lanzamiento (int): año en que fue lanzada esa pelicula
        duracion (int): duracion en min de la pelicula
        atp (bool): si es apto para todo publico o no

    Returns:
        dict: devuelve un diccionario con todos los items correspondientes a la pelicula.
    """
    pelicula = { "id": id,
                "titulo": titulo,
                "genero": genero,
                "lanzamiento": año_lanzamiento,
                "duracion": duracion,
                "atp": atp,
                "plataformas": plataforma
                }
    return pelicula

def ingresar_peliculas(id_incremental: int, lista_peliculas: list)-> dict:
    """funcion que ingresa las peliculas(opcion Dar de alta)

    Args:
        id_incremental (int): id unico de la pelicula que va a ingresar
        lista_peliculas (list): catalogo/lista de las peliculas ya ingresadas, y/o donde
        seran ingresadas las nuevas

    Returns:
        dict: retorna un diccionario despues de pedir los items y componer un diccionario
        con ellos.
    """
    titulo = ingreso_titulo(lista_peliculas, "ingrese el titulo de la pelicula nueva: ")

    genero = ingreso_genero("ingrese el genero de la pelicula nueva: ")

    actual = date.today()
    fecha_year = actual.year
    lanzamiento = get_int("Ingrese el año de lanzamiento de la pelicula: ", "Error, ingrese un dato valido: ", 1888, fecha_year, 5)

    duracion = get_int("Ingrese la duracion de la pelicula(min): ", "Error, ingrese un dato valido: ", 0, 9999999, 5)
    
    atp = ingreso_atp()

    plataformas = ingresar_plataformas()

    pelicula = registrar_pelicula(id_incremental, titulo, genero, lanzamiento, duracion, atp, plataformas)
    
    return pelicula



def modificar_pelicula(lista_pelicula: list[dict]):
    """funcion que permite modificar los parametros de una pelicula, a excepcion del id unico de dicha
    pelicula

    Args:
        lista_pelicula (list[dict]): catalogo/lista de las peliculas ya ingresadas y pueden modificarse
    """
    pelicula_a_modificar = input("Ingrese el titulo de la pelicula que quiere modificar: ").title()
    pelicula_a_modificar.strip()
    bandera = False
    
    while True:
        for pelicula in lista_pelicula:
            if pelicula["titulo"] == pelicula_a_modificar:
                keys = pelicula.keys()
                aux_contador = 0
                for i in keys:
                    if i != "id":
                        aux_contador += 1
                        print(f"#{i}")
                    
                parametro_modificado = input("Ingrese el parametro que quiere modificar: ").lower()
            else:
                continue

            match parametro_modificado:
                case "titulo":
                    pelicula[parametro_modificado] = ingreso_titulo(lista_pelicula, "Ingrese el titulo de la pelicula modificada: ")
                    bandera = True

                case "genero":
                    pelicula[parametro_modificado] = ingreso_genero("Ingrese el genero de la pelicula modificada: ")
                    bandera = True

                case "duracion":
                    pelicula[parametro_modificado] = get_int("Ingrese la duracion de la pelicula: ", "Error, ingrese un dato valido: ", 0, 9999999, 5)
                    bandera = True

                case "lanzamiento":
                    actual = date.today()
                    fecha_year = actual.year
                    pelicula[parametro_modificado] = get_int("Ingrese el año de lanzamiento de la pelicula: ", "Error, ingrese un dato valido: ", 1888, fecha_year, 5)
                    bandera = True

                case "atp":
                    pelicula[parametro_modificado] = ingreso_atp()
                    bandera = True
                    
                case "plataformas":
                    pelicula[parametro_modificado] = ingresar_plataformas()
                    bandera = True
                case "salir":
                    break

                case _:
                    continue

            break

        otra_modificacion = input(f"Se realizo la modificacion al {parametro_modificado}, quiere modificar otra cosa? ").title()
        if otra_modificacion == "Si":
            mod = False
        elif otra_modificacion == "No":
            mod == False
        else:
            mod == True
        while mod:
            otra_modificacion = input(f"Se realizo la modificacion al {parametro_modificado}, quiere modificar otra cosa? ").title()
        if otra_modificacion == "No":
            break


    if bandera:
        print(f"Se realizaron modificaciones en el {parametro_modificado} de la pelicula elegida.")
    else:
        print("No se realizaron modificaciones.")        
    

def eliminar_pelicula(lista_peliculas: list[dict]):
    """funcion que elimina/saca de la lista de peliculas a la pelicula seleccionada

    Args:
        lista_peliculas (list[dict]): catalogo/lista de las peliculas ya ingresadas y pueden eliminarse
    """
    pelicula_eliminada = input("Ingrese el titulo de la pelicula que quiere eliminar: ").strip()
    pelicula_eliminada = pelicula_eliminada.title()
    for i in range(len(lista_peliculas)):
        if lista_peliculas[i]["titulo"] == pelicula_eliminada:
            validacion = input("Se encontro la pelicula que quiere eliminar, quiere proceder? ").title()
            while validacion != "Si" and validacion != "No":
                validacion = input("Se encontro la pelicula que quiere eliminar, quiere proceder(si o no)? ").title()
            if validacion == "Si":
                eliminado = lista_peliculas.pop(i)
                eliminar = True
                break
            else:
                eliminar = False
                break
            
    if eliminar :
        print(f"La pelicula {pelicula_eliminada} fue eliminada correctamente.")
    else:
        print(f"Se anulo la eliminacion de la pelicula {pelicula_eliminada}.")

    

            



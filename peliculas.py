# from menu import *
from pack_input_mod.input import *
from archivos_peliculas import *

def mostrar_peliculas(lista_peliculas: list[dict]):
    """funcion que muestra la lista que sea ingresada como parametro

    Args:
        lista_peliculas (list[dict]): lista de peliculas que el usuario quiere mostrar
    """
    try:
        print('*' * 126)
        keys_peliculas = lista_peliculas[0].keys()
        cadena = "|"
        for elementos in keys_peliculas:
            if elementos != "id":
                cadena += f"{elementos :^{20}}|"
        print(cadena)
        print('-' * 126)
        for peliculas in lista_peliculas:
            cadena_peliculas = "|"
            data = peliculas.values()
            for obj in data:
                if obj != peliculas["id"]: 
                    if obj == True or obj == "True":
                        obj = "si"
                    elif obj == False or obj == "False":
                        obj = "no"
                    if obj == peliculas["duracion"]:
                        obj = f"{obj} min"
                    elif obj == peliculas["plataformas"]:
                        plataformas = ""
                        for i in obj:
                            plataformas += f"{i},"
                        obj = plataformas[:-1]
                        # if obj is list:
                        # else:
                        #     plataforma = obj[0]
                        #     obj = plataforma
                    cadena_peliculas += f"{obj :^{20}}|"
            print(cadena_peliculas)
        print('*' * 126)
    except IndexError:
        print("No tiene ninguna pelicula cargada...")
        


def mostrar_filtro(lista: list, filtrar_por: str):
    """funcion que filtra aquellas peliculas que quiere mostrar determinados parametros,
    para luego llamar a la funcion mostrar.

    Args:
        lista (list): lista de peliculas que quiere que filtren
        filtrar_por (str): parametro por el que quieren filtrar las peliculas
    """
    print(f"{filtrar_por} de peliculas que hay: ")
    lista_filtrada = []
    bandera = False
    iteracion = 0
    for pelicula in lista:
        if bandera:
            if pelicula[filtrar_por] not in lista_filtrada:
                lista_filtrada.append(pelicula[filtrar_por])
                
        else:
            bandera = True
            lista_filtrada.append(pelicula[filtrar_por])

    for elementos in lista_filtrada:
        iteracion += 1
        print(f"{iteracion}) {elementos}")

    elemento_filtrado = get_int("Seleccione una opcion que quieras filtrar: ", "error, ingresa un opcion valido: ", 1, len(lista_filtrada), 5)
    
    lista_del_filtro_seleccionado = []
    for peliculas in lista:
        if peliculas[filtrar_por] == lista_filtrada[elemento_filtrado - 1]:
            lista_del_filtro_seleccionado.append(peliculas)
    mostrar_peliculas(lista_del_filtro_seleccionado)

def mostrar_atp(apta: bool, lista_peliculas: list):
    """funcion que selecciona aquellas peliculas atp o no atp dependiendo lo que el usuario quiera,
    para luego llamar a mostrarlas

    Args:
        apta (bool): si es true muestra las peliculas atp, y es false muestra las no atp
        lista_peliculas (list): catalogo/lista de las peliculas ya ingresadas en el programa
    """
    lista_aux = []
    for pelicula in lista_peliculas:
        if pelicula["atp"] == apta or pelicula["atp"] == f"{apta}":
            lista_aux.append(pelicula)

    mostrar_peliculas(lista_aux)


def plataformas(lista: list[dict], parametro: str):
    """Funcion especializada que filtra las peliculas pasadas de la lista, bajo la plataforma que el usuario 
    seleccione. Para luego mostrarlas.

    Args:
        lista (list[dict]): lista de peliculas
        parametro (str): key'plataformas'
    """
    plataformas_en_catalogo = []
    pelicula_lista = []
    for pelicula in lista:
        for plataforma in pelicula[parametro]:
            if plataforma not in plataformas_en_catalogo:
                plataformas_en_catalogo.append(plataforma)
    iteracion = 0
    for elementos in plataformas_en_catalogo:
        iteracion += 1
        print(f"{iteracion}) {elementos}")
    plataforma_seleccionada = get_int("Seleccione una opcion que quieras filtrar: ", "error, ingresa un opcion valido: ", 1, len(plataformas_en_catalogo), 5)
    for pelicula in lista:
        for plataforma in pelicula[parametro]:
            if plataformas_en_catalogo[plataforma_seleccionada - 1] in plataforma:
                pelicula_lista.append(pelicula)
    mostrar_peliculas(pelicula_lista)



def tipos_de_mostrar(lista_peliculas: list):
    """funcion que le permite al usuario elegir como y cuales peliculas mostrar en consola,
    llamando a la determinada funcion que cumple ese rol.

    Args:
        lista_peliculas (list): catalogo/lista de las peliculas ya ingresadas en el programa
    """
    lista_mostrar = ["Todas las películas", "De determinado género", "De determinado año", "Todas las ATP",
                     "Todas las No ATP", "De determinada plataforma"]
    for i in range(len(lista_mostrar)):
        print(f"{i + 1}) {lista_mostrar[i]}")
    seleccion = get_int("Ingrese alguna de las opciones para ordenar: ", "Opcion invalida, ingrese una opcion existente: ", 1, len(lista_mostrar), 5)
    eleccion = lista_mostrar[seleccion - 1]
    match eleccion:
        case "Todas las películas":
            mostrar_peliculas(lista_peliculas)

        case "De determinado género":
            mostrar_filtro(lista_peliculas, "genero")

        case "De determinado año":
            mostrar_filtro(lista_peliculas, "lanzamiento")
        
        case "Todas las ATP":
            mostrar_atp(True, lista_peliculas)

        case "De determinada plataforma":
            plataformas(lista_peliculas, "plataformas")

        case _:
            mostrar_atp(False, lista_peliculas)



def buscar_por_titulo(lista_peliculas: list[dict]):
    """funcion que busca por el titulo a la pelicula dentro del catalogo, y muestra dicha pelicula.

    Args:
        lista_peliculas (list[dict]): catalogo/lista de las peliculas ya ingresadas en el programa
    """
    pelicula_titulo = input("Ingrese el titulo de la pelicula que quiere buscar: ").strip()
    pelicula_titulo = pelicula_titulo.title()
    for pelicula in lista_peliculas:
        if pelicula["titulo"] == pelicula_titulo:
            print('*' * 106)
            keys = pelicula.keys()
            cadena = "|"
            for key in keys:
                if key != "id":
                    cadena += f"   {key :^{20}}|"
            print(cadena)
            print('-' * 106)
            elementos = pelicula.values()
            cadena_ = "|"
            for elemento in elementos:
                if elemento != pelicula["id"]:
                    match elemento:
                        case True:
                            elemento = "si"
                        case False:
                            elemento = "no"

                    if elemento == pelicula["duracion"]:
                        elemento = f"{elemento} min"
                    cadena_ += f"   {elemento :^{20}}|"
            print(cadena_)
            print('*' * 106)
            break

def ordenar(lista_peliculas: list[dict]):
    """funcion que ordena la lista con los parametros que elija el usuario, usando un
    bubble sort(burbujeo).

    Args:
        lista_peliculas (list[dict]): catalogo/lista de las peliculas ya ingresadas en el programa
    """
    tipo_ordenamiento = input("Como quiere ordenar la lista de empleados(titulo, genero, lanzamiento o duracion)? ").lower()
    while tipo_ordenamiento != "titulo" and tipo_ordenamiento != "genero" and tipo_ordenamiento != "lanzamiento" and tipo_ordenamiento != "duracion":
        tipo_ordenamiento = input("Error, seleccione un ordenamiento valido(nombre, apellido o salario): ").lower()

    asc_o_desc = input("Quiere que sea de forma descendente o ascendente? ").lower()
    while asc_o_desc != "ascendente" and asc_o_desc != "descendente":
        asc_o_desc = input("Error, solo se puede ordenar de forma descendente o ascendente: ").lower()
    if asc_o_desc == "descendente":
        ordenamiento = True
    else:
        ordenamiento = False

    for i in range(0, len(lista_peliculas)):
        for j in range(i + 1, len(lista_peliculas)):
            if ordenamiento == False:
                if lista_peliculas[i][tipo_ordenamiento] > lista_peliculas[j][tipo_ordenamiento]:
                    aux = lista_peliculas[i]
                    lista_peliculas[i] = lista_peliculas[j]
                    lista_peliculas[j] = aux
            else:
                if lista_peliculas[i][tipo_ordenamiento] < lista_peliculas[j][tipo_ordenamiento]:
                    aux = lista_peliculas[i]
                    lista_peliculas[i] = lista_peliculas[j]
                    lista_peliculas[j] = aux

    print("Se ordeno correctamente.")


def calcular(lista_peliculas: list[dict]):
    """funcion que puede calcular la duración promedio de todas las películas, o
    la cantidad de películas lanzadas en cada año desde 2005 hasta 2024 llamando a funciones
    especificas.

    Args:
        lista_peliculas (list[dict]): catalogo/lista de las peliculas ya ingresadas en el programa
    """
    lista_opciones = ["Duración promedio de todas las películas.", "Cantidad de películas lanzadas en cada año desde 2005 hasta 2024."]
    print("Estas son las opciones que pued calcular:")
    aux = len(lista_opciones)
    for i in range(aux):
        print(f"{i + 1}_ {lista_opciones[i]}")
    opcion = get_int("Ingrese la opcion que quiere ejecutar: ", "Error, ingrese una opcion valida: ", 1, 2, 5)
    match opcion:
        case 1:
            calcular_duracion(lista_peliculas)
        case 2:
            #calcular_cantidad(lista_peliculas)
            calcular_cantidad_dos(lista_peliculas)


def calcular_duracion(lista_peliculas: list[dict]):
    """funcion calcula la duración promedio de todas las películas

    Args:
        lista_peliculas (list[dict]): catalogo/lista de las peliculas ya ingresadas en el programa
    """
    acumulador = 0
    for peli in lista_peliculas:
        acumulador += peli["duracion"]
    promedio = acumulador / (len(lista_peliculas))
    print(f"El promedio de duracion de las peliculas son {promedio}min.")

def calcular_cantidad(lista_peliculas: list[dict]):
    """funcion que calcula la cantidad de películas lanzadas en cada año desde 2005 hasta 2024,
    mostrandolos en forma de lista.

    Args:
        lista_peliculas (list[dict]): catalogo/lista de las peliculas ya ingresadas en el programa
    """
    desde_año = 2005
    hasta_año = 2024
    lista_parametrada = []
    for peli in lista_peliculas:
        if peli["lanzamiento"] > desde_año and peli["lanzamiento"] < hasta_año:
            lista_parametrada.append(peli)
    
    print(lista_parametrada)
    print(f"Lista de peliculas desde el año {desde_año} hasta el año {hasta_año}:")
    mostrar_peliculas(lista_parametrada)

def calcular_cantidad_dos(lista_peliculas: list[dict]):
    """funcion que calcula la cantidad de películas lanzadas en cada año desde 2005 hasta 2024,
    mostrandolos de forma mas ordenada sin listas.

    Args:
        lista_peliculas (list[dict]): catalogo/lista de las peliculas ya ingresadas en el programa
    """
    desde_año = 2005
    hasta_año = 2024
    lista_parametrada = {}
    for peli in lista_peliculas:
        if peli["lanzamiento"] > desde_año and peli["lanzamiento"] < hasta_año:
            year = str(peli["lanzamiento"])
            if year not in lista_parametrada:
                lista_parametrada[year] = 1
            else:
                lista_parametrada[year] += 1

    years = lista_parametrada.keys()
    for year in years:
        print(f"En el año {year} hubo {lista_parametrada[year]} lanzamientos")

def porcentaje(lista_peliculas: list[dict]):
    """funcion que puede calcular el porcentaje por genero, o el porcentaje por ATP
    de la lista de peliculas llamando a funciones espeficicas para dicha tarea.

    Args:
        lista_peliculas (list[dict]): catalogo/lista de las peliculas ya ingresadas en el programa
    """
    lista_opciones = ["Porcentaje por genero", "Porcentaje por ATP"]
    print("Estas son las opciones que puede elegir:")
    aux = len(lista_opciones)
    for i in range(aux):
        print(f"{i + 1}_ {lista_opciones[i]}")
    opcion = get_int("Ingrese la opcion que quiere ejecutar: ", "Error, ingrese una opcion valida: ", 1, 2, 5)

    if opcion == 1:
        porcentaje_genero(lista_peliculas)
    else:
        porcentaje_atp(lista_peliculas)

def porcentaje_genero(lista: list[dict]):
    """funcion que calcula el porcentaje por genero de todos los generos existentes dentro
    de la lista de peliculas.

    Args:
        lista (list[dict]): catalogo/lista de las peliculas ya ingresadas en el programa
    """
    lista_parametrada = {}
    for peli in lista:
        genero = str(peli["genero"])
        if genero not in lista_parametrada:
            lista_parametrada[genero] = 1
        else:
            lista_parametrada[genero] += 1
    
    generos = lista_parametrada.keys()
    for gen in generos:
        porcentaje_peli = (lista_parametrada[gen]/ len(lista)) * 100
        print(f"El genero {gen} representa el {porcentaje_peli}%")
    
def porcentaje_atp(lista_peliculas: list[dict]):
    """funcion que calcula el porcentaje de ATP de todas las peliculas dentro
    de la lista de peliculas.

    Args:
        lista_peliculas (list[dict]): catalogo/lista de las peliculas ya ingresadas en el programa
    """
    contador_si = 0
    contador_no = 0
    for peli in lista_peliculas:
        if peli["atp"]:
            contador_si += 1
        else:
            contador_no += 1
    
    si = (contador_si / len(lista_peliculas)) * 100
    no = (contador_no / len(lista_peliculas)) * 100
    print(f"El porcentaje de peliculas atp es de {si}% y el porcentaje de los NO atp es {no}%")

        
    


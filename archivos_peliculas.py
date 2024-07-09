import json
from input_funcion import registrar_pelicula


#Todo lo relacionado con las funciones de guardado en archivo csv

def guardar_listado(path: str, lista_peliculas: list[dict]):
    """Funcion que guarda la lista de peliculas pasada en el parametro 'lista_peliculas', y las guarda en el archivo 
    del parametro 'path'.

    Args:
        path (str): url del archivo
        lista_peliculas (list[dict]): lista de peliculas
    """
    key_dicc = lista_peliculas[0].keys()
    with open(path, "w") as peliculas :
        cadena_index = ""
        for r in key_dicc:
            cadena_index += f"{r},"
        peliculas.write(f"{cadena_index}\n")
        for i in lista_peliculas:
            cadena_index = ""
            for j in key_dicc:
                cadena_index += f"{i[j]},"
            peliculas.write(f"{cadena_index}\n")
   
def leer_csv(path:str):
    """Funcion que extrae la lista de peliculas dentro de un archivo, y las retorna como list[dict].
    En caso de que no haya ninguna, crea una lista vacia para ir agregando las peliculas

    Args:
        path (str): url del archivo

    Returns:
        list: lista de las peliculas
    """
    try:
        lista = []
        with open(path, "r") as peliculas:
            lineas = peliculas.readlines()
        contador = 0
        for linea in lineas:
            if contador > 0:
                linea = linea.strip().split(",")
                plataforma = armar_lista(linea, "[","]")
                dicc = registrar_pelicula(linea[0],linea[1],linea[2],linea[3],linea[4],linea[5],plataforma)
                lista.append(dicc)
            else:
                contador += 1
    except:
        lista = []

    return lista

def armar_lista(lista_peli, caracter_uno, caracter_dos):
    """Funcion especializada para que al extraer la informacion del archivo csv, se pueda obtener la lista de 
    plataformas.

    Args:
        lista_peli (list[str]): info obtenida del archivo
        caracter_uno (_type_): caracter desde el que se inicia la lista('[')
        caracter_dos (_type_): caracter en el que finaliza la lista(']')

    Returns:
        list: devuelve la lista de plataformas
    """
    lista = []
    for linea in lista_peli:
        lineas = linea.strip().split(",")
        contador = 0
        for palabra in lineas:
            for caracteres in palabra:
                if caracteres == caracter_uno:
                    contador = 1
                    palabra = palabra.replace(caracter_uno, "").replace("'", "")
                elif caracteres == caracter_dos:
                    contador = 2
                    palabra = palabra.replace(caracter_dos, "").replace("'", "")
                if contador == 1:
                    if palabra not in lista:
                        lista.append(palabra)
                elif contador == 2:
                    lista.append(palabra)
                    contador += 1 
    return lista  

#--------------------------------------------------------------------------------------------------------------------
#Todo lo relacionado con el json de los id incrementales

def obtener_ids(path):
    try:
        with open(path, 'r') as archivo:
            datos = json.load(archivo)
            #print(datos)
            lista = datos['ids']
            retorna = lista
    except FileNotFoundError:
        retorna = []
    return retorna

def generar_id(path):
    try:
        ids = obtener_ids(path)
        id_actual = ids[len(ids) - 1]
        id_actual += 1
        ids.append(id_actual)
    except:
        ids = obtener_ids(path)
        id_actual = 1
        ids.append(id_actual)
    datos = {'ids': ids}
    with open(path, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    return id_actual




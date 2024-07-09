from pack_input_mod.input import *

#-------------------------------Funciones de ingreso de datos de las peliculas----------------------------------------

def ingreso_titulo(lista_peliculas: list, mensaje: str) -> str:
    """funcion para el ingreso del titulo

    Args:
        lista_peliculas (list): catalogo/lista de las peliculas ya existentes en el programa
        mensaje (str): mensaje que aparecera al querer ingresar el titulo

    Returns:
        str: en caso de que el titulo sea valido(no este repetido), se devolvera el mismo
        para que sea ingresado en el catalogo
    """
    titulo = get_str(mensaje, "Error, ingrese un titulo valido: ", 30, 5).title()
    titulo = titulo.strip()
    validar_titulo = validacion_titulo(lista_peliculas, titulo)
    while validar_titulo == False:
        titulo = get_str("El titulo ingresado ya existe, ingrese otro: ", "Error, ingrese un titulo valido: ", 30, 5).title()
        titulo = titulo.strip()
        validar_titulo = validacion_titulo(lista_peliculas, titulo)
    return titulo

def validacion_titulo(lista_peliculas: list, titulo_validado: str)-> bool:
    """funcion que valida que el titulo de la nueva pelicula por ingresar no este repetido
    ya en el catalogo existente.

    Args:
        lista_peliculas (list): catalogo/lista de las peliculas ya existentes en el programa
        titulo_validado (str): titulo de la pelicula nueva que debe ser validado

    Returns:
        bool: retorna un booleano dependiendo si el titulo ya existe o no dentro del catalogo.
    """
    try:
        retorna = True
        for pelicula in lista_peliculas:
            if titulo_validado == pelicula["titulo"]:
                retorna = False
                break
    except IndexError:
        retorna = True
    return retorna



def ingreso_genero(mensaje: str)-> str:
    """funcion para el ingreso del genero

    Args:
        mensaje (str):  mensaje que aparecera al querer ingresar el titulo

    Returns:
        str: en caso de que el genero sea valido, se devolvera el mismo
        para que sea ingresado en el catalogo
    """
    genero = get_str(mensaje, "Error, ingrese un genero valido: ", 30, 5).title()
    genero = genero.strip()
    validar_genero = genero_peliculas(genero)
    while validar_genero == False:
        genero = get_str("el genero ingresado no existe, ponga uno que sea valido: ", "Error, ingrese un genero valido: ", 30, 5).title()
        genero = genero.strip()
        validar_genero = genero_peliculas(genero)
    return genero

def genero_peliculas(genero_ingresado: str)-> bool:
    """funcion que valida que el genero ingresado de una nueva pelicula sea valido

    Args:
        genero_ingresado (str): genero de la pelicula nueva

    Returns:
        bool: retorna un booleano dependiendo si se hallo el genero correspondient
        a la pelicula.
    """
    set_generos = {"Accion", "Aventura", "Animacion", "Biografico", "Comedia", "Comedia romantica",
    "Comedia dramatica", "Crimen", "Documental", "Drama", "Fantasia", "Historico",
    "Infantil", "Musical", "Misterio", "Policiaco", "Romance", "Ciencia ficcion",
    "Suspenso", "Terror", "Western", "Belico", "Deportivo", "Noir", "Experimental",
    "Familiar", "Superheroes", "Espionaje", "Artes marciales", "Fantastico", 
    "Catastrofe", "Melodrama", "Erotico", "Cine independiente", "Zombies", "Vampiros",
    "Cyberpunk", "Steampunk", "Distopia", "Utopia", "Road Movie", "Docuficcion", 
    "Mockumentary", "Gotico", "Slasher", "Adolescente", "Culto", "Maravilloso"}
    retorna = False
    for genero in set_generos:
        if genero_ingresado == genero:
            retorna = True
            break
    return retorna


def ingreso_atp()-> bool:
    """funcion para el ingreso de si es atp o no

    Returns:
        bool: devuelve un booleano correspondiente en caso de que la pelicula sea
        atp o no
    """
    atp = get_str("La pelidula ingresada es ATP? ", "Error, ingreso no valido(debe ser si o no): ", 5, 5).strip()
    atp = atp.lower()
    while atp != "si" and atp != "no":
        atp = get_str("La pelidula ingresada es ATP(debe ser si o no)? ", "Error, ingreso no valido(debe ser si o no): ", 5, 5).strip()
        atp = atp.lower()
    atp_bool = False
    if atp == "si":
        atp_bool = True

    return atp_bool


def ingresar_plataformas():
    """Funcion para que el usuario ingrese las plataformas en la que esta disponible la pelicula.
    Dentro de la funcion llama a dos funciones aparte 'validar_plataforma()' y 'lista_plataformas()'

    Returns:
        list[str]: Devuelve una lista de las plataformas correspondientes a la pelicula.
    """
    lista_posibles_plataformas = ["Netflix", "Prime Video", "Disney+", "Hbo Max", "Apple Tv+"]
    lista = []
    mensaje = "Ingrese la plataforma a la que pertenece la pelicula: "
    longitud = 20
    while True:
        plataforma = input(mensaje).strip()
        validacion = validar_plataforma(plataforma, longitud)
        if validacion[0] == True:
            validar_lista = lista_plataformas(lista_posibles_plataformas, validacion[1])
            if validar_lista[0] == True:
                lista.append(validar_lista[1])
                consultar = input("Desea agregar otra plataforma? ").title().strip()
                while consultar != "Si" and consultar != "No":
                    consultar = input("Desea agregar otra plataforma(ponga Si o No)? ").title().strip()
                if consultar == "No":
                    break
                else:
                    pass
                mensaje = "Ingrese la plataforma a la que pertenece la pelicula: "   
        else:
            mensaje = "Ingrese una plataforma valida: "
    return lista

def validar_plataforma(plataforma:str, longitud: int):
    """Funcion que valida que la plataforma pasada este dentro de la longitud pasada como parametro, y tambien
    valida que la cadena tenga solo caracteres alfabeticos y caracteres especiales, sin contener numeros.

    Args:
        plataforma (str): plataforma que se valida
        longitud (int): longitud limite para el largo de la cadena

    Returns:
        tuple: devuelte una tupla que contiene un booleano que da fe de que la plataforma ingresada cumpla
        las especificaciones, y tambien en segunda instancia contiene la plataforma misma.
    """
    if longitud < len(plataforma):
        retorna = False
    else:
        retorna = True
    if retorna:
        for caracter in plataforma:
            if not caracter.isalpha() and not caracter in ['+', ' ', '-']:
                retorna = False
            else: 
                retorna = True
    return (retorna, plataforma)

def lista_plataformas(lista: list[str], plataforma: str):
    """funcion que valida que la plataforma ingresada este dentro de las plataformas validas, y estas deberan estar
    pasadas por el parametro 'lista'.

    Args:
        lista (list[str]): plataformas validas
        plataforma (str): plataforma ingresada

    Returns:
        tuple: devuelte una tupla que contiene un booleano que da fe de que la plataforma ingresada este dentro
        de la lista de plataformas validas, y tambien en segunda instancia contiene la plataforma misma.
    """
    cadena = plataforma.split()
    validacion = False
    if len(cadena) < 2:
        plataforma = cadena[0].title().strip()
    else:
        plataforma = ""
        for palabra in cadena:
            plataforma += f" {palabra.title().strip()}"
        plataforma = plataforma.strip()
    if plataforma in lista:
        validacion = True
    
    return (validacion, plataforma)


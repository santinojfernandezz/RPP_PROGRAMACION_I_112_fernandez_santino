from .validate import *

#pedir entero
def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int|bool :
    """Pide un numero entero y comprueba que este en los parametros establecidos.

    Args:
        mensaje (str): mensaje sobre lo que se pide
        mensaje_error (str): en caso de rror, mensaje que vuelva a pedir el elemento
        minimo (float): determinacion del minimo del parametro establecido
        maximo (float): determinacion del parametro maximo establecido
        reintentos (float): cantidad de errores permitidos posibles

    Returns:
        float|None: retorna el elemento ya comprobado, en caso de ser correspondiente 
        retorna el elemento original, de otra forma retorna uno acorde a los parametros 
        establecidos."""
    pedir_numero = input(mensaje).strip()
    validacion = validate_num(pedir_numero, minimo, maximo, mensaje_error, reintentos)
    if validacion[0] == False:
        pedir_numero = validacion[0]
    else:
        pedir_numero = int(validacion[1])
    return pedir_numero

#pedir flotante
def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: float) -> float|bool :
    """Pide un numero flotante y comprueba que este en los parametros establecidos.

    Args:
        mensaje (str): mensaje sobre lo que se pide
        mensaje_error (str): en caso de rror, mensaje que vuelva a pedir el elemento
        minimo (float): determinacion del minimo del parametro establecido
        maximo (float): determinacion del parametro maximo establecido
        reintentos (float): cantidad de errores permitidos posibles

    Returns:
        float|None: retorna el elemento ya comprobado, en caso de ser correspondiente 
        retorna el elemento original, de otra forma retorna uno acorde a los parametros 
        establecidos.
    """
    pedir_numero = input(mensaje).strip()
    validacion = validate_num(pedir_numero, minimo, maximo, mensaje_error, reintentos)
    if validacion[0] == False:
        pedir_numero = validacion[0]
    else:
        pedir_numero = validacion[1]
    return pedir_numero

#pedir str
def get_str (mensaje: str, mensaje_error: str, longitud: int, reintento)-> str|bool:
    """Pide ingresar una cadena de texto, para luego comprobar si esta en los parametros establecidos

    Args:
        mensaje (str): pide la cadena de txt
        mensaje_error (str): en caso de un error al superar los parametros, lo pide 
        nuevamente
        longitud (int): cantidad de caracteres que acepta como parametro la funcion
        reintento (_type_): cantidad de intentos aceptados antes de tirar error

    Returns:
        str|None: retorna la cadena pedida y comprobada, pero si no compre con los 
        parametros, retorna none
    """
    palabra_ingresada = input(mensaje).strip()
    validacion = validate_str(palabra_ingresada, mensaje_error, longitud, reintento)
    if validacion[0] == False:
        palabra_ingresada = validacion[0]
    else:
        palabra_ingresada = validacion[1]
        
    return palabra_ingresada

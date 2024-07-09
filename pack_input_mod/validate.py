def validate_num (numero: str, minimo: float|int, maximo: float|int, mensaje_error: str, reintentos: int):
    validacion = False
    contador_intentos = 0
    validate = numero.isdigit()
    if validate == True :
        validacion = True
        numero = int(numero)
        while numero < minimo or numero > maximo:
            numero = input(mensaje_error)
            validate = numero.isdigit()
            if contador_intentos == reintentos:
                numero = 0
                break
        retorna = (validacion, numero)

    else:
        while True:
            numero = input(mensaje_error)
            validate = numero.isdigit()
            if validate:
                validacion = True
                numero = int(numero)
                break
            if contador_intentos == reintentos:
                numero = 0
                break
        retorna = (validacion, numero)

    return retorna
    
def validate_str(palabra_ingresada: str, mensaje_error: str, longitud: int, reintento: int):
    contador = 0
    validacion = validar_caracteres(palabra_ingresada, mensaje_error, reintento)
    if validacion[0] == True:
        palabra_ingresada = validacion[1]
        largo = len(palabra_ingresada)
        while largo > longitud:
            if contador == reintento:
                validacion = False
                break
            palabra_ingresada = input(mensaje_error)
            validacion = validar_caracteres(palabra_ingresada, mensaje_error, reintento)
            palabra_ingresada = validacion[1]
            contador += 1
        retorna = validacion
    


    return retorna 


def validar_caracteres(palabra: str, mensaje_error: str, reintento: int):
    contador = 0
    validar_caracteres = palabra.isdigit()
    validacion = True
    while validar_caracteres == True:
        if contador >= reintento:
            validacion = False
            break
        palabra = input(mensaje_error)
        validar_caracteres = palabra.isalpha()
        contador += 1
    comprobacion = (validacion, palabra)
    return comprobacion


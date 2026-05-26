def crear_array(cantidad:int) -> int:
    """
    crea una lista de numeros enteros
    se inicializa en 0, con el tamaño especificado
    por parametro

    Args:
        cantidad (int): numero de elementos que tiene la lista

    Returns:
        int: una lista de enteros, rellena con 0
    """

    return[0] * cantidad

def cargar_array(cantidad:int) -> list:
    """
    le pide al usuario por consola para hacer una lista
    del tamaño especificado

    Args:
        cantidad (int): cantidad de numeros que se van a solicitar

    Returns:
        list: una lista con enteros ingresados por el usuario
    """

    mi_array = crear_array(cantidad)
    for i in range(cantidad):
        mi_array[i] = input(f"Ingrese el numero para la posicion [{i}]: ")
    return mi_array

def calcular_promedio(lista:list) -> float:
    """
    calcula el promedio de todos los numeros de la lista

    Args:
        lista (list): lista de numeros int/float

    Returns:
        float: el promedio de los numeros
    """

    if lista == None:
        print("Error, inserte valores numericos.")

    else:
        suma = 0.0
        for numero in lista:
            suma += numero

    return suma / len(lista)

def promedio_positivos(lista:list) -> float:
    """
    filtra los numeros mayores de la lista y calcula el promedio

    Args:
        lista (list): lista de numeros a evaluar

    Returns:
        float: el promedio de los numeros positivos
    """

    suma = 0.0
    contador = 0
    
    for numero in lista:
        if numero > 0:
            suma += numero
            contador += 1
    
    if contador == 0:
        print(f"{contador}")
    
    return suma / contador

def calcular_producto(lista: list) -> float:
    """
    multiplica todos los elementos de la lista

    Args:
        lista (list): lista de numeros

    Returns:
        float: el total
    """

    resultado = 1.0

    if lista == None:
        print("Error, prueba poniendo valores numericos.")
    
    else:
        for numero in lista:
            resultado *= numero
    
    return resultado

def posicion_maxima(lista: list) -> int:
    """
    busca el valor mas alto de la lista

    Args:
        lista (list): lista de numeros a buscar

    Returns:
        int: indice base 0 del valor maximo
    """

    if lista == None:
        print("Error, inserte valores enteros porfavor.")
    
    maximo = lista[0]
    posicion = 0

    for i in range(1, len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
            posicion = i
    
    return posicion

def obtener_posiciones_maximas(lista: list) -> list:
    """
    identifica el valor maximo de una lista y
    muestra todas las posiciones en las cuales aparece

    Args:
        lista (list): Lista de numeros a analizar

    Returns:
        list: Lista con los indices donde se encuentra el valor maximo
    """

    if lista == None:
        print("Error, Porfavor ingrese numeros enteros para la lista.")

    else:
        maximo = lista[0]
        for numero in lista:
            if numero > maximo:
                maximo = numero

        posiciones = []

        for i in range(len(lista)):
            if lista [i] == maximo:
                posiciones.append(i)
        
    return posiciones

def reemplazar_nombres(lista_nombres: list, 
                       nombre_antiguo:str, 
                       nombre_nuevo:str) -> int:
    """
    recorre una lista reemplazando un nombre especifico
    por uno nuevo

    Args:
        lista_nombres (list): lista de str que contiene los nombres
        nombre_antiguo (str): el nombre que se desea cambiar
        nombre_nuevo (str): el nuevo nombre que se cambiara por el antiguo

    Returns:
        int: la cantidad total de cambios que se hicieron
    """

    contador = 0
    
    for i in range(len(lista_nombres)):
        if lista_nombres[i] == nombre_antiguo:
            lista_nombres[i] = nombre_nuevo
            contador += 1
    
    return contador

def obtener_interseccion(array_1: list, array_2: list) -> list:
    """
    muestra la interseccion entre 2 listas, 
    omitiendo duplicados

    Args:
        array1 (list): primer lista de elementos
        array2 (list): segunda lista de elementos

    Returns:
        list: lista de elementos en comun
    """

    resultado = []

    for elemento in array_1:
        if elemento in array_2 and elemento not in resultado:
            resultado.append(elemento)
        
    return resultado

def obtener_union(array_1: list, array_2: list) -> list:
    """
    realiza la union de dos listas, no hay valores
    repetidos en la lista retorno

    Args:
        array_1 (list): primer lista de elementos
        array_2 (list): segunda lista de elementos

    Returns:
        list: lista con la combinacion de todos los elementos
    """

    resultado = []

    for elemento in array_1:
        if elemento not in resultado:
            resultado.append(elemento)
    
    for elemento in array_2:
        if elemento not in resultado:
            resultado.append(elemento)
    
    return resultado

def obtener_diferencia(array_1: list, array_2: list) -> list:
    """
    calcula la diferencia de dos listas, encuentra los
    elementos que estan en la primera lista pero no estan en la segunda

    Args:
        array_1 (list): lista del cual se extraen los elementos
        array_2 (list): lista que actua como filtro

    Returns:
        list: lista con los elementos que solo muestra el primer array
    """

    resultado = []

    for elemento in array_1:
        if elemento not in array_2 and elemento not in resultado:
            resultado.append(elemento)
    
    return resultado
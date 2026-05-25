def crear_array(cantidad:int) -> int:
    """
    _summary_

    Args:
        cantidad (int): _description_

    Returns:
        int: _description_
    """

    return[0] * cantidad

def cargar_array(cantidad:int) -> list:
    """
    _summary_

    Args:
        cantidad (int): _description_

    Returns:
        list: _description_
    """

    mi_array = crear_array(cantidad)
    for i in range(cantidad):
        mi_array[i] = int(input(f"Ingrese el numero para la posicion [{i}]: "))
    return mi_array

def calcular_promedio(lista:list) -> float:
    """
    _summary_

    Args:
        lista (list): _description_

    Returns:
        float: _description_
    """

    suma = 0.0

    if lista == None:
        print("Error, inserte valores numericos.")

    else:
        for numero in lista:
            suma += numero

    return suma / len(lista)

def promedio_positivos(lista:list) -> float:
    """
    _summary_

    Args:
        lista (list): _description_

    Returns:
        float: _description_
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
    _summary_

    Args:
        lista (list): _description_

    Returns:
        float: _description_
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
    _summary_

    Args:
        lista (list): _description_

    Returns:
        int: _description_
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
    _summary_

    Args:
        lista (list): _description_

    Returns:
        list: _description_
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
    
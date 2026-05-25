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
        for num in lista:
            suma += num

    return suma / len(lista)
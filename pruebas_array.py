from .array_unidimensional import *

numeros_test = [3, -5, 12, 8, -2, 12, 0, 7]
nombres_test = ["Ana", "Pedro", "Luis", "Ana", "María"]
conjunto_1 = ['a', 'b', 'c', 'j', 'f']
conjunto_2 = ['g', 'b', 'l', 'e', 'i', 'h']

array_vacio = crear_array(4)
print(f"Crear array vacio de tamaño {len(array_vacio)}: {array_vacio}")

promedio_total = calcular_promedio(numeros_test)
print(f"Promedio de todos los elementos: {promedio_total}")

positivos = promedio_positivos(numeros_test)
print(f"Promedio de positivos: {positivos}")

lista_corta = [2, -3, 4]
producto_calculado = calcular_producto(lista_corta)
print(f"Producto de la lista {lista_corta}: {producto_calculado}")

primer_maximo_posicion = posicion_maxima(numeros_test)
print(f"Posicion del numero maximo: {primer_maximo_posicion}")

todas_posiciones_maximas = obtener_posiciones_maximas(numeros_test)
print(f"Todas las posiciones del valor maximo: {todas_posiciones_maximas}")

print(f"Lista de nombres original: {nombres_test}")
cantidad_cambios = reemplazar_nombres(nombres_test, "Ana", "Beatriz")
print(f"Lista modificada: {nombres_test}")
print(f"Cantidad de reemplazos efectuados: {cantidad_cambios}")

interseccion = obtener_interseccion(conjunto_1, conjunto_2)
print(f"Interseccion (C_1 n C_2): {interseccion}")

union = obtener_union(conjunto_1, conjunto_2)
print(f"Union (C_1 U C_2): {union}")

diferencia = obtener_diferencia(conjunto_1, conjunto_2)
print(f"Diferencia (M // N): {diferencia}")
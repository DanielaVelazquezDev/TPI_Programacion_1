# ordenamientos.py

def ordenar_paises(lista_paises, clave, descendente=False):
    """
    Ordena la lista de países por el criterio especificado sin romper el archivo original.
    'clave' puede ser: 'nombre', 'poblacion' o 'superficie'.
    'descendente=True' sirve para ordenar de mayor a menor (o Z a A).
    """
    # Usamos sorted con una función lambda, que es la forma nativa, eficiente
    # y recomendada en Python para ordenar listas de diccionarios.
    lista_ordenada = sorted(lista_paises, key=lambda x: x[clave], reverse=descendente)
    return lista_ordenada

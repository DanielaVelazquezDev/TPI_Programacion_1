# MÓDULO DE BÚSQUEDAS Y FILTROS: busquedas.py

def buscar_por_nombre(lista_paises, nombre_buscar):
    """
    Busca países que contengan el texto ingresado (coincidencia parcial).
    Usa .lower() para que no importe si se escribe en mayúsculas o minúsculas.
    """
    resultados = []
    for p in lista_paises:
        if nombre_buscar.lower() in p["nombre"].lower():
            resultados.append(p)
    return resultados

def filtrar_por_continente(lista_paises, continente_buscar):
    """
    Filtra países por coincidencia exacta del continente.
    """
    resultados = []
    for p in lista_paises:
        if p["continente"].lower() == continente_buscar.lower():
            resultados.append(p)
    return resultados

def filtrar_por_rango(lista_paises, clave, minimo, maximo):
    """
    Filtra la lista según un rango numérico.
    'clave' puede ser 'poblacion' o 'superficie'.
    """
    resultados = []
    for p in lista_paises:
        if minimo <= p[clave] <= maximo:
            resultados.append(p)
    return resultados

# MÓDULO DE ANALÍTICA: estadisticas.py

def calcular_indicadores(lista_paises):
    """Calcula el promedio, máximos y mínimos de población y superficie."""
    if not lista_paises:
        return None

    # Inicializamos con el primer país para comparar
    max_pob = min_pob = max_sup = min_sup = lista_paises[0]
    total_pob = 0
    total_sup = 0

    for p in lista_paises:
        total_pob += p["poblacion"]
        total_sup += p["superficie"]

        # Comparaciones de Población
        if p["poblacion"] > max_pob["poblacion"]:
            max_pob = p
        if p["poblacion"] < min_pob["poblacion"]:
            min_pob = p

        # Comparaciones de Superficie
        if p["superficie"] > max_sup["superficie"]:
            max_sup = p
        if p["superficie"] < min_sup["superficie"]:
            min_sup = p

    cantidad = len(lista_paises)
    
    return {
        "promedio_poblacion": total_pob / cantidad,
        "promedio_superficie": total_sup / cantidad,
        "pais_max_poblacion": max_pob,
        "pais_min_poblacion": min_pob,
        "pais_max_superficie": max_sup,
        "pais_min_superficie": min_sup
    }

def conteo_por_continente(lista_paises):
    """Cuenta cuántos países registrados hay en cada continente."""
    dicc_conteo = {}
    for p in lista_paises:
        continente = p["continente"]
        # Si el continente ya está en el diccionario sumamos 1, si no, lo iniciamos en 1
        if continente in dicc_conteo:
            dicc_conteo[continente] += 1
        else:
            dicc_conteo[continente] = 1
    return dicc_conteo

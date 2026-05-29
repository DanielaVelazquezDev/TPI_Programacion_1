# ==========================================
# MODULO DE PERSISTENCIA: datos.py
# ==========================================

import os

ARCHIVOCSV = "paises.csv"

def crear_csv_base_automatico():
    """Crea un archivo de texto con formato CSV básico si no existe."""
    # Líneas crudas de texto plano para evitar tildes rotas o bloqueos de librerías
    lineas = [
        "nombre,poblacion,superficie,continente\n",
        "Argentina,45376763,2780400,América\n",
        "Japón,125800000,377975,Asia\n",
        "Brasil,213993437,8515767,América\n",
        "Alemania,83149300,357022,Europa\n"
    ]
    try:
        with open(ARCHIVOCSV, mode="w", encoding="utf-8") as f:
            f.writelines(lineas)
        print(f"--> [Sistema] Archivo '{ARCHIVOCSV}' generado con éxito.")
    except Exception:
        print("[Error] No se pudo crear el archivo de datos local.")

def cargar_datos():
    """Lee el archivo de texto y lo transforma en una lista de diccionarios."""
    if not os.path.exists(ARCHIVOCSV):
        crear_csv_base_automatico()
        
    lista_paises = []
    try:
        with open(ARCHIVOCSV, mode="r", encoding="utf-8") as f:
            lineas = f.readlines()
            
            if len(lineas) <= 1:
                return lista_paises # Archivo vacío o solo con cabecera
                
            # Procesamos cada línea saltando la cabecera (línea 0)
            for linea in lineas[1:]:
                linea = linea.strip()
                if not linea:
                    continue
                # Separamos los campos por la coma
                campos = linea.split(",")
                if len(campos) == 4:
                    lista_paises.append({
                        "nombre": campos[0].strip(),
                        "poblacion": int(campos[1].strip()),
                        "superficie": int(campos[2].strip()),
                        "continente": campos[3].strip()
                    })
    except Exception:
        print("[Error] Problema al leer el archivo de texto.")
    return lista_paises

def guardar_datos(lista_paises):
    """Toma la lista de diccionarios y la escribe en el archivo de texto CSV."""
    try:
        with open(ARCHIVOCSV, mode="w", encoding="utf-8") as f:
            # Escribimos la cabecera obligatoria
            f.write("nombre,poblacion,superficie,continente\n")
            for p in lista_paises:
                fila = f"{p['nombre']},{p['poblacion']},{p['superficie']},{p['continente']}\n"
                f.write(fila)
    except Exception:
        print("[Error] No se pudieron guardar los cambios en el archivo.")

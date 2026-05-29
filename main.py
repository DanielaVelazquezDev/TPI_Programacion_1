# ==========================================
# ARCHIVO PRINCIPAL: main.py
# ==========================================

import os
import sys
import datos
import busquedas
import ordenamientos
import estadisticas

# ==========================================
# 1) VALIDACIONES DE ENTRADA (BLINDAJE)
# ==========================================

def solicitar_entero_positivo(mensaje):
    """Solicita un número entero por consola garantizando que sea válido y mayor a cero."""
    while True:
        try:
            valor = input(mensaje).strip()
            numero = int(valor)
            if numero > 0:
                return numero
            print("[Error] El número debe ser mayor a cero.")
        except ValueError:
            print("[Error] Entrada inválida. Ingrese un número entero (sin puntos, comas ni letras).")

def solicitar_texto_obligatorio(mensaje):
    """Garantiza que el usuario no deje campos vacíos o con espacios solos."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("[Error] Este campo no puede quedar vacío.")


# ==========================================
# 2) VISTA DE INTERFAZ (CONSOLA)
# ==========================================

def mostrar_tabla_real(lista):
    """Imprime el dataset o los resultados procesados en una tabla alineada."""
    if not lista:
        print("\n--> No se encontraron resultados para mostrar.")
        return
    print(f"\n{'Nombre':<15} | {'Población':<12} | {'Superficie (km²)':<16} | {'Continente':<12}")
    print("-" * 65)
    for p in lista:
        print(f"{p['nombre']:<15} | {p['poblacion']:<12} | {p['superficie']:<16} | {p['continente']:<12}")


# ==========================================
# 3) ORQUESTADOR / MENÚ INTERACTIVO
# ==========================================

def menu():
    # Carga inicial de datos reales desde paises.csv
    paises = datos.cargar_datos()
    
    while True:
        print("\n=======================================")
        print("     SISTEMA DE GESTIÓN DE PAÍSES      ")
        print("=======================================")
        print("1. Agregar nuevo país")
        print("2. Actualizar población y superficie")
        print("3. Buscar país por nombre")
        print("4. Filtrar países")
        print("5. Ordenar países")
        print("6. Ver estadísticas analíticas")
        print("7. Mostrar todos los países")
        print("8. Salir del programa")
        print("=======================================")
        
        # Atrapamos cualquier interrupción o bug de teclado en la terminal
        try:
            opcion = input("Seleccione una opción (1-8): ").strip()
        except (KeyboardInterrupt, Exception):
            print("\n\n[Aviso] Entrada interrumpida. Volviendo al menú...")
            continue
        
        # --- OPCIÓN 1: AGREGAR PAÍS ---
        if opcion == "1":
            print("\n--- AGREGAR NUEVO PAÍS ---")
            nombre = solicitar_texto_obligatorio("Nombre del país: ")
            
            # Validamos que el país no exista previamente
            existe = False
            for p in paises:
                if p["nombre"].lower() == nombre.lower():
                    existe = True
                    break
            
            if existe:
                print(f"[Error] El país '{nombre}' ya se encuentra registrado.")
                continue
                
            pob = solicitar_entero_positivo("Cantidad de Población: ")
            sup = solicitar_entero_positivo("Superficie en km²: ")
            cont = solicitar_texto_obligatorio("Continente al que pertenece: ")
            
            paises.append({"nombre": nombre, "poblacion": pob, "superficie": sup, "continente": cont})
            datos.guardar_datos(paises)
            print(f"¡Éxito! '{nombre}' fue guardado en el archivo.")
            
        # --- OPCIÓN 2: ACTUALIZAR PAÍS ---
        elif opcion == "2":
            print("\n--- ACTUALIZAR POBLACIÓN Y SUPERFICIE ---")
            nombre_buscar = input("Ingrese el nombre exacto del país a modificar: ").strip()
            
            encontrado = None
            for p in paises:
                if p["nombre"].lower() == nombre_buscar.lower():
                    encontrado = p
                    break
            
            if encontrado:
                print(f"Modificando datos actuales de: {encontrado['nombre']}")
                encontrado["poblacion"] = solicitar_entero_positivo("Nueva población: ")
                encontrado["superficie"] = solicitar_entero_positivo("Nueva superficie (km²): ")
                datos.guardar_datos(paises)
                print("¡Datos actualizados y guardados con éxito!")
            else:
                print("[Error] El país no fue encontrado. Verifique la ortografía.")
            
        # --- OPCIÓN 3: BUSCAR POR NOMBRE ---
        elif opcion == "3":
            print("\n--- BUSCAR PAÍS POR NOMBRE ---")
            nombre_b = input("Ingrese el nombre (o fragmento) a buscar: ").strip()
            resultados = busquedas.buscar_por_nombre(paises, nombre_b)
            mostrar_tabla_real(resultados)
            
        # --- OPCIÓN 4: FILTRAR DATASET ---
        elif opcion == "4":
            print("\n--- MÓDULO DE FILTRADOS ---")
            print("1. Filtrar por Continente")
            print("2. Filtrar por Rango de Población")
            print("3. Filtrar por Rango de Superficie")
            
            sub_opcion = input("Seleccione una opción de filtrado (1-3): ").strip()
            
            if sub_opcion == "1":
                cont_b = input("Ingrese el continente a filtrar: ").strip()
                resultados = busquedas.filtrar_por_continente(paises, cont_b)
                mostrar_tabla_real(resultados)
                
            elif sub_opcion in ["2", "3"]:
                clave = "poblacion" if sub_opcion == "2" else "superficie"
                print(f"\n[Filtrar por {clave.capitalize()}]")
                minimo = solicitar_entero_positivo("Ingrese el valor mínimo: ")
                maxi = solicitar_entero_positivo("Ingrese el valor máximo: ")
                
                resultados = busquedas.filtrar_por_rango(paises, clave, minimo, maxi)
                mostrar_tabla_real(resultados)
            else:
                print("[Error] Opción de filtrado inválida.")
                
        # --- OPCIÓN 5: ORDENAMIENTOS ---
        elif opcion == "5":
            print("\n--- MÓDULO DE ORDENAMIENTOS ---")
            print("1. Ordenar por Nombre")
            print("2. Ordenar por Cantidad de Población")
            print("3. Ordenar por Superficie (km²)")
            
            criterio = input("Seleccione el criterio de ordenamiento (1-3): ").strip()
            
            if criterio not in ["1", "2", "3"]:
                print("[Error] Criterio inválido.")
                continue
                
            clave = "nombre" if criterio == "1" else "poblacion" if criterio == "2" else "superficie"
            
            print("\n¿En qué sentido desea ordenar?")
            print("1. Ascendente (Menor a Mayor / A-Z)")
            print("2. Descendente (Mayor a Menor / Z-A)")
            sentido = input("Seleccione el sentido (1-2): ").strip()
            
            if sentido not in ["1", "2"]:
                print("[Error] Sentido inválido.")
                continue
                
            es_descendente = (sentido == "2")
            resultados = ordenamientos.ordenar_paises(paises, clave, es_descendente)
            
            print(f"\n[Resultados ordenados por {clave.capitalize()}]")
            mostrar_tabla_real(resultados)
            
        # --- OPCIÓN 6: ESTADÍSTICAS ---
        elif opcion == "6":
            print("\n--- MÓDULO DE ESTADÍSTICAS ANALÍTICAS ---")
            stats = estadisticas.calcular_indicators(paises)
            
            if not stats:
                print("[Aviso] No hay suficientes datos para calcular estadísticas.")
                continue
                
            print(f"\n📈 PROMEDIOS GENERALES:")
            print(f"- Población Promedio:  {stats['promedio_poblacion']:,.2f} habitantes")
            print(f"- Superficie Promedio: {stats['promedio_superficie']:,.2f} km²")
            
            print(f"\n🏆 VALORES EXTREMOS:")
            print(f"- Mayor Población:  {stats['pais_max_poblacion']['nombre']} ({stats['pais_max_poblacion']['poblacion']:,} hab.)")
            print(f"- Menor Población:  {stats['pais_min_poblacion']['nombre']} ({stats['pais_min_poblacion']['poblacion']:,} hab.)")
            print(f"- Mayor Superficie: {stats['pais_max_superficie']['nombre']} ({stats['pais_max_superficie']['superficie']:,} km²)")
            print(f"- Menor Superficie: {stats['pais_min_superficie']['nombre']} ({stats['pais_min_superficie']['superficie']:,} km²)")
            
            print(f"\n🗺️ DISTRIBUCIÓN POR CONTINENTE:")
            conteos = estadisticas.conteo_por_continente(paises)
            for cont, cant in conteos.items():
                print(f"- {cont}: {cant} país(es)")
            
        # --- OPCIÓN 7: LISTAR TODO ---
        elif opcion == "7":
            print("\n--- LISTADO ACTUAL DE PAÍSES (paises.csv) ---")
            mostrar_tabla_real(paises)
            
        # --- OPCIÓN 8: SALIDA ---
        elif opcion == "8":
            print("\n¡Gracias por usar el sistema! Saliendo de forma segura...")
            os._exit(0)
            
        else:
            print("\n[ERROR] Opción inválida. Ingrese un número del 1 al 8.")


if __name__ == "__main__":
    try:
        menu()
    except Exception:
        print(f"\n[Sistema] Reinicio controlado para evitar cierres inesperados.")
        menu()

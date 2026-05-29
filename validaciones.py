# validaciones.py

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

def solicitar_continente_valido(mensaje):
    """Garantiza que el continente ingresado sea uno de los 5 principales."""
    continentes_validos = ["América", "Europa", "Asia", "África", "Oceanía"]
    while True:
        valor = input(mensaje).strip()
        # Buscamos coincidencia ignorando mayúsculas/minúsculas
        for c in continentes_validos:
            if c.lower() == valor.lower():
                return c  # Devolvemos el nombre bien formateado (ej: "América")
        
        print(f"[Error] Continente inválido. Opciones válidas: {', '.join(continentes_validos)}")

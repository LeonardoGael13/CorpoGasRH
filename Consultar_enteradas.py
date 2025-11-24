from datetime import datetime

def consultar_entradas():
    """Muestra todas las entradas registradas en 'entradas.txt', ordenadas por fecha y hora."""
    try:
        with open("entradas.txt", "r", encoding="utf-8") as f:
            entradas = [linea.strip() for linea in f if linea.strip()]  # Quita líneas vacías

        if not entradas:
            print("No hay entradas registradas aún.")
            return

        # Función auxiliar para extraer la fecha y hora de cada línea
        def obtener_fecha(entrada):
            try:
                partes = entrada.split(" - ")
                fecha_hora_str = partes[3].strip()  # La fecha y hora siempre está en la posición 4
                return datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M:%S")
            except (IndexError, ValueError):
                return datetime.min  # Si hay error, lo pone al principio

        # Ordenar las entradas por fecha y hora
        entradas_ordenadas = sorted(entradas, key=obtener_fecha)

        print("\nEntradas registradas (ordenadas por fecha y hora):\n")
        for entrada in entradas_ordenadas:
            print(entrada)

    except FileNotFoundError:
        print("Aún no existe el archivo 'entradas.txt'.")


if __name__ == "__main__":
    consultar_entradas()

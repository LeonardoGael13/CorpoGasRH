from datetime import datetime, time
import os

ARCHIVO_HORARIOS = "horarios.txt"


def cargar_horarios():
    """Carga los horarios guardados, o usa valores por defecto si el archivo no existe."""
    if not os.path.exists(ARCHIVO_HORARIOS):
        horarios = {
            1: time(6, 0),
            2: time(14, 0),
            3: time(22, 0)
        }
        guardar_horarios(horarios)
        return horarios

    horarios = {}
    with open(ARCHIVO_HORARIOS, "r") as file:
        for linea in file:
            turno, hora = linea.strip().split("=")
            h, m = hora.split(":")
            horarios[int(turno)] = time(int(h), int(m))
    return horarios


def guardar_horarios(horarios):
    """Guarda los horarios en el archivo."""
    with open(ARCHIVO_HORARIOS, "w") as file:
        for turno, hora in horarios.items():
            file.write(f"{turno}={hora.hour}:{hora.minute}\n")


def menu_configurar_horarios():
    """Permite cambiar la hora de entrada de cada turno."""
    horarios = cargar_horarios()

    while True:
        print("\n=== CONFIGURAR HORARIOS DE TURNOS ===")
        print(f"1. Turno 1 → {horarios[1].hour}:{horarios[1].minute:02d}")
        print(f"2. Turno 2 → {horarios[2].hour}:{horarios[2].minute:02d}")
        print(f"3. Turno 3 → {horarios[3].hour}:{horarios[3].minute:02d}")
        print("4. Volver al menú principal")

        op = input("Selecciona el turno a modificar: ")

        if op in ["1", "2", "3"]:
            nuevo = input("Nueva hora (HH:MM): ")
            try:
                h, m = map(int, nuevo.split(":"))
                horarios[int(op)] = time(h, m)
                guardar_horarios(horarios)
                print("Horario actualizado correctamente.")
            except:
                print("Formato incorrecto. Usa HH:MM")
        elif op == "4":
            break
        else:
            print("Opción no válida.")


# REGISTRO DE ENTRADAS 

def determinar_estado(turno, fecha_hora):
    horarios = cargar_horarios()

    hora_entrada = horarios.get(turno)
    if not hora_entrada:
        return "Turno no válido"

    try:
        hora_real = datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M:%S").time()
    except ValueError:
        return "Formato de fecha inválido"

    diferencia = ((datetime.combine(datetime.today(), hora_real) -
                   datetime.combine(datetime.today(), hora_entrada)).total_seconds()) / 60

    if diferencia <= 0:
        return "A tiempo"
    elif 0 < diferencia <= 5:
        return "Retardo leve (dentro de tolerancia)"
    elif 5 < diferencia <= 10:
        return "Retardo"
    else:
        return "Falta"


def obtener_siguiente_id(archivo):
    if not os.path.exists(archivo):
        return 1

    with open(archivo, "r", encoding="utf-8") as f:
        lineas = f.readlines()

    if not lineas:
        return 1

    ultimo = lineas[-1].split(" - ")[0]
    try:
        return int(ultimo) + 1
    except ValueError:
        return 1


def guardar_entrada(empleado, turno, fecha_hora):
    try:
        turno = int(turno)
    except ValueError:
        turno = 1

    estado = determinar_estado(turno, fecha_hora)
    archivo = "entradas.txt"
    registro_id = obtener_siguiente_id(archivo)

    with open(archivo, "a", encoding="utf-8") as f:
        f.write(f"{registro_id} - {empleado} - Turno {turno} - {fecha_hora} - Estado: {estado}\n")

    print("\nEntrada registrada correctamente:")
    print(f"Número de registro: {registro_id}")
    print(f"Empleado: {empleado}")
    print(f"Turno: {turno}")
    print(f"Fecha y hora: {fecha_hora}")
    print(f"Estado: {estado}")


# MENÚ PRINCIPAL 

def menu_principal():
    while True:
        print("\n===== SISTEMA DE EMPLEADOS =====")
        print("1. Registrar entrada")
        print("2. Configurar horarios de turnos")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            empleado = input("Nombre del empleado: ")

            horarios = cargar_horarios()
            print("\nSelecciona turno:")
            print(f"1. Turno 1 → {horarios[1].hour}:{horarios[1].minute:02d}")
            print(f"2. Turno 2 → {horarios[2].hour}:{horarios[2].minute:02d}")
            print(f"3. Turno 3 → {horarios[3].hour}:{horarios[3].minute:02d}")

            try:
                turno = int(input("Turno (1-3): "))
                if turno not in [1, 2, 3]:
                    raise ValueError
            except ValueError:
                print("Turno no válido, se asigna Turno 1.")
                turno = 1

            fecha_hora = input("Fecha y hora de entrada (AAAA-MM-DD HH:MM:SS): ")

            guardar_entrada(empleado, turno, fecha_hora)

        elif opcion == "2":
            menu_configurar_horarios()

        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu_principal()
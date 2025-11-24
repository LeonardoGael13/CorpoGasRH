from Registro_empleados import guardar_entrada
from Consultar_enteradas import consultar_entradas
from Grafica import menu_graficas
from Registro_empleados import menu_configurar_horarios  # NUEVO: menú de turnos


def menu():
    while True:
        print("\n=== SISTEMA DE ENTRADAS DE EMPLEADOS ===")
        print("1. Registrar entrada de empleado")
        print("2. Consultar entradas")
        print("3. Ver gráficas")
        print("4. Configurar horarios de turnos")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        # 1. Registrar entrada
        if opcion == "1":
            empleado = input("Empleado: ")
            print("\nSelecciona el turno:")
            print("1. Turno 1")
            print("2. Turno 2")
            print("3. Turno 3")

            turno = input("Turno (1-3): ")
            fecha_hora = input("Fecha y hora de entrada (AAAA-MM-DD HH:MM:SS): ")

            guardar_entrada(empleado, turno, fecha_hora)

        # 2. Consultar
        elif opcion == "2":
            consultar_entradas()

        # 3. Gráficas
        elif opcion == "3":
            menu_graficas()

        # 4. Configurar turnos
        elif opcion == "4":
            menu_configurar_horarios()

        # 5. Salir
        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()

from datos import cargar_datos
import dueños
import mascotas
import citas

def main():
    datos = cargar_datos()

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar dueño")
        print("2. Listar dueños")
        print("3. Registrar mascota")
        print("4. Listar mascotas")
        print("5. Agendar cita")
        print("6. Listar citas")
        print("7. Eliminar cita")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            dueños.registrar_dueno(datos)

        elif opcion == "2":
            dueños.listar_duenos(datos)

        elif opcion == "3":
            mascotas.registrar_mascota(datos)

        elif opcion == "4":
            mascotas.listar_mascotas(datos)

        elif opcion == "5":
            citas.agendar_cita(datos)

        elif opcion == "6":
            citas.listar_citas(datos)

        elif opcion == "7":
            citas.eliminar_cita(datos)

        elif opcion == "8":
            print("Saliendo del sistema... ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()

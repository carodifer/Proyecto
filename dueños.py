from datos import guardar_datos, siguiente_id

def registrar_dueno(datos):
    print("\n--- Registrar Dueño ---")
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    direccion = input("Dirección: ").strip()

    dueno = {
        "id": str(siguiente_id(datos.get("duenos", []), "id")),
        "nombre": nombre,
        "telefono": telefono,
        "direccion": direccion
    }

    datos.setdefault("duenos", []).append(dueno)
    guardar_datos(datos)
    print(f"Dueño registrado correctamente. ID: {dueno['id']}")

def listar_duenos(datos):
    print("\n--- Lista de Dueños ---")
    if not datos.get("duenos"):
        print("No hay dueños registrados.")
        return
    for d in datos["duenos"]:
        print(f"- ID {d['id']}: {d['nombre']} | Tel: {d['telefono']} | Dir: {d['direccion']}")

def buscar_dueno_por_id(datos, dueno_id):
    return next((d for d in datos.get("duenos", []) if d["id"] == str(dueno_id)), None)
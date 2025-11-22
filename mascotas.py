from datos import guardar_datos, siguiente_id
from dueños import buscar_dueno_por_id

def registrar_mascota(datos):
    print("\n--- Registrar Mascota ---")
    nombre = input("Nombre: ").strip()
    especie = input("Especie: ").strip()
    raza = input("Raza: ").strip()
    edad = input("Edad: ").strip()

    if not datos.get("duenos"):
        print("No hay dueños registrados. Registre un dueño primero.")
        return

    print("Dueños registrados:")
    for d in datos["duenos"]:
        print(f"- ID {d['id']}: {d['nombre']}")

    dueno_id = input("Ingrese el ID del dueño asociado: ").strip()
    dueno = buscar_dueno_por_id(datos, dueno_id)
    if not dueno:
        print("ID de dueño no encontrado. Canceler registro de mascota.")
        return

    mascota = {
        "id": str(siguiente_id(datos.get("mascotas", []), "id")),
        "nombre": nombre,
        "especie": especie,
        "raza": raza,
        "edad": edad,
        "dueno_id": dueno["id"]
    }

    datos.setdefault("mascotas", []).append(mascota)
    guardar_datos(datos)
    print(f"Mascota registrada correctamente. ID: {mascota['id']}")

def listar_mascotas(datos):
    print("\n--- Lista de Mascotas ---")
    if not datos.get("mascotas"):
        print("No hay mascotas registradas.")
        return
    for m in datos["mascotas"]:
        dueno = next((d for d in datos.get("duenos", []) if d["id"] == m.get("dueno_id")), None)
        nombre_dueno = dueno["nombre"] if dueno else "Sin dueño"
        print(f"- ID {m['id']}: {m['nombre']} ({m['especie']}), Dueño: {nombre_dueno}")

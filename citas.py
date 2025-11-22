from datos import guardar_datos, siguiente_id
from mascotas import listar_mascotas
from dueños import listar_duenos

def listar_citas(datos):
    print("\n--- Lista de Citas ---")
    if not datos.get("citas"):
        print("No hay citas registradas.")
        return
    for c in datos["citas"]:
        print(f"- ID {c.get('id')}: Mascota ID {c['mascota_id']} | Dueño ID {c['dueno_id']} | {c['fecha']} {c['hora']} | {c.get('motivo','')}")

def agendar_cita(datos):
    print("\n--- Agendar Cita ---")
    if not datos.get("mascotas"):
        print("No hay mascotas registradas. Registre una mascota primero.")
        return
    if not datos.get("duenos"):
        print("No hay dueños registrados. Registre un dueño primero.")
        return

    print("Mascotas registradas:")
    listar_mascotas(datos)
    mascota_id = input("Ingrese el ID de la mascota: ").strip()
    mascota = next((m for m in datos["mascotas"] if m["id"] == mascota_id), None)
    if not mascota:
        print("No se encontró la mascota.")
        return


    dueno = next((d for d in datos["duenos"] if d["id"] == mascota.get("dueno_id")), None)
    if not dueno:
        print("La mascota no tiene dueño válido asociado. Revise registros.")
        return

    fecha = input("Ingrese la fecha de la cita (YY-MM-DD): ").strip()
    hora = input("Ingrese la hora de la cita (HH:MM): ").strip()
    motivo = input("Ingrese el motivo de la cita: ").strip()

    for c in datos.get("citas", []):
        if c["fecha"] == fecha and c["hora"] == hora:
            print(f"ERROR: Ya existe una cita programada para {fecha} a las {hora}. No es posible agendar.")
            return

    cita = {
        "id": str(siguiente_id(datos.get("citas", []), "id")),
        "mascota_id": mascota["id"],
        "dueno_id": dueno["id"],
        "fecha": fecha,
        "hora": hora,
        "motivo": motivo
    }

    datos.setdefault("citas", []).append(cita)
    guardar_datos(datos)
    print(f"Cita agendada exitosamente para {mascota['nombre']} el {fecha} a las {hora}. (ID cita: {cita['id']})")

def eliminar_cita(datos):
    listar_citas(datos)
    cid = input("Ingrese el ID de la cita a eliminar: ").strip()
    antes = len(datos.get("citas", []))
    datos["citas"] = [c for c in datos.get("citas", []) if c.get("id") != cid]
    if len(datos.get("citas", [])) < antes:
        guardar_datos(datos)
        print("Cita eliminada.")
    else:
        print("No se encontró la cita.")

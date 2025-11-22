import json
RUTA_ARCHIVO = "datos.json"

def cargar_datos():
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        datos = {"mascotas": [], "duenos": [], "citas": []}
        guardar_datos(datos)
        return datos

def guardar_datos(datos):
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def siguiente_id(items, clave="id"):
    """Devuelve el siguiente id entero (1,2,3...) basado en la lista de dicts."""
    if not items:
        return 1
    try:
        return max(int(item.get(clave, 0)) for item in items) + 1
    except ValueError:
        return 1
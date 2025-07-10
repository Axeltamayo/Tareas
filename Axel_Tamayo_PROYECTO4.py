# --- Importación de librerías necesarias ---
import requests
import json
import os

# --- Función para obtener datos del Pokémon desde la API ---
def obtener_datos_pokemon(nombre_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "nombre": data["name"],
            "peso": data["weight"],
            "altura": data["height"],
            "tipos": [tipo["type"]["name"] for tipo in data["types"]],
            "habilidades": [habilidad["ability"]["name"] for habilidad in data["abilities"]],
            "movimientos": [movimiento["move"]["name"] for movimiento in data["moves"]],
            "imagen": data["sprites"]["front_default"]
        }
    elif response.status_code == 404:
        return None
    else:
        print("Error al consultar la API.")
        return None

# --- Función para mostrar los datos del Pokémon en consola ---
def mostrar_datos(pokemon):
    print(f"\n📛 Nombre: {pokemon['nombre'].capitalize()}")
    print(f"⚖️ Peso: {pokemon['peso']}")
    print(f"📏 Altura: {pokemon['altura']}")
    print(f"🔥 Tipos: {', '.join(pokemon['tipos'])}")
    print(f"💡 Habilidades: {', '.join(pokemon['habilidades'])}")
    print(f"🎯 Movimientos: {', '.join(pokemon['movimientos'][:5])}...")  # Solo los primeros 5
    print(f"🖼️ Imagen: {pokemon['imagen']}")

# --- Función para guardar los datos en un archivo JSON ---
def guardar_en_json(pokemon):
    if not os.path.exists("pokedex"):
        os.makedirs("pokedex")

    archivo = f"pokedex/{pokemon['nombre']}.json"
    with open(archivo, "w") as f:
        json.dump(pokemon, f, indent=4)
    print(f"\n✅ Datos guardados en: {archivo}")

# --- Función principal del programa ---
def main():
    nombre = input("🔍 Introduce el nombre de un Pokémon: ").strip()

    datos_pokemon = obtener_datos_pokemon(nombre)

    if datos_pokemon:
        mostrar_datos(datos_pokemon)
        guardar_en_json(datos_pokemon)
    else:
        print("❌ Pokémon no encontrado. Verifica el nombre.")

# --- Ejecutar el programa solo si este archivo es el principal ---
if __name__ == "__main__":
    main()
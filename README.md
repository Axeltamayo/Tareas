# Tareas

🔍 Importaciones

import requests      # Permite hacer solicitudes HTTP para obtener datos de la API.

import json          # Permite guardar la información como archivo JSON.

import os            # Permite trabajar con archivos y directorios del sistema.

from PIL import Image      # Librería para trabajar con imágenes.

from io import BytesIO     # Convierte datos binarios en un flujo que PIL puede leer.

 1. Función: get_pokemon_data(name)

def get_pokemon_data(name):

    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    
    response = requests.get(url)
    
Se construye la URL usando el nombre del Pokémon en minúsculas.

Se hace una solicitud GET a la API.
    if response.status_code == 200:
        return response.json()
    else:
        return None
        
Si la respuesta fue exitosa (200 OK), devuelve los datos en formato JSON.

Si no, devuelve None (lo usaremos para mostrar un mensaje de error).

🖼️ 2. Función: show_pokemon_info(data)

def show_pokemon_info(data):
    name = data["name"].capitalize()
    weight = data["weight"]
    height = data["height"]
    image_url = data["sprites"]["front_default"]
    
Extrae el nombre, peso, altura e imagen frontal del Pokémon desde los datos JSON.
    types = [t["type"]["name"] for t in data["types"]]
    abilities = [a["ability"]["name"] for a in data["abilities"]]
    moves = [m["move"]["name"] for m in data["moves"]]
Usa listas por comprensión para extraer:

Tipos

Habilidades

Movimientos
    print(f"\n📛 Nombre: {name}")
    print(f"📏 Altura: {height}")
    print(f"⚖️ Peso: {weight}")
    print(f"🌈 Tipos: {', '.join(types)}")
    print(f"💡 Habilidades: {', '.join(abilities)}")
    print(f"🌀 Primeros 5 movimientos: {', '.join(moves[:5])}")
    print(f"🖼️ Imagen: {image_url}")
Muestra la información en consola de forma legible.
    show_image(image_url)
    
Llama a la función que abre la imagen del Pokémon.
    return {
        "name": name,
        "height": height,
        "weight": weight,
        "types": types,
        "abilities": abilities,
        "moves": moves,
        "image_url": image_url
    }
Devuelve un diccionario con toda la información para guardarla luego en JSON.

 3. Función: show_image(url)
def show_image(url):
    try:
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        image.show()
Descarga la imagen de la URL.

Usa BytesIO para leer los datos binarios de imagen.

Usa Pillow (Image) para abrirla y mostrarla en una ventana.
    except Exception as e:
    print(f"⚠️ Error al cargar la imagen: {e}")
        
Captura cualquier error y lo muestra en pantalla si algo sale mal.

 4. Función: save_to_json(pokemon_info)

def save_to_json(pokemon_info):
    if not os.path.exists("pokedex"):
        os.makedirs("pokedex")
        
Crea una carpeta llamada pokedex/ si no existe.
    filename = f"pokedex/{pokemon_info['name'].lower()}.json"
    with open(filename, "w") as f:
        json.dump(pokemon_info, f, indent=4)
        
Guarda la información del Pokémon como archivo .json con su nombre en minúsculas.
    print(f"\n✅ Información guardada en {filename}")
    
Confirma en consola que se ha guardado correctamente.

 5. Función principal: main()

def main():
    name = input("🔍 Introduce el nombre de un Pokémon: ")
    data = get_pokemon_data(name)
    
Pide al usuario el nombre del Pokémon e intenta obtener sus datos.
    if data:
        pokemon_info = show_pokemon_info(data)
        save_to_json(pokemon_info)
    else:
        print("❌ Pokémon no encontrado. Verifica el nombre.")
        
Si los datos existen, los muestra y guarda.

Si no, avisa que no se encontró el Pokémon.

 6. Bloque de ejecución principal

if __name__ == "__main__":
    main()

Proyecto 3

1. Importación de bibliotecas

import random

import matplotlib.pyplot as plt

*random se usa para simular las decisiones aleatorias (izquierda o derecha).

*matplotlib.pyplot se usa para graficar el histograma final de resultados.

2. Función simular_galton

def simular_galton(n_canicas, niveles):

Esta función simula el recorrido de muchas canicas por la máquina.

Dentro de la función:

contenedores = [0] * (niveles + 1)

Se crea una lista con niveles + 1 elementos, ya que si una canica tiene 12 decisiones (niveles), puede terminar en 13 posibles posiciones (de 0 a 12).

for _ in range(n_canicas):

    derecha = 0
    
Se itera una vez por cada canica. derecha contará cuántas veces la canica se fue a la derecha.

for _ in range(niveles):

    if random.random() > 0.5:
    
        derecha += 1
        
Se hace una decisión aleatoria por cada nivel.

Si el número aleatorio es mayor a 0.5, se considera que la canica fue a la derecha.

contenedores[derecha] += 1

Se incrementa el contador del contenedor que corresponde a esa cantidad de movimientos a la derecha.

3. Función graficar_histograma
   
def graficar_histograma(resultados):

Esta función crea un histograma a partir de la lista resultados.

plt.bar(range(len(resultados)), resultados, color='skyblue', edgecolor='black')

Dibuja las barras del histograma. Cada barra representa un contenedor.

plt.xlabel('Contenedores (posición final)')

plt.ylabel('Número de canicas')

plt.title('Simulación de una máquina de Galton con 3000 canicas y 12 niveles')

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

Se configuran las etiquetas, el título y se muestra la gráfica.

4. Ejecución del programa
   
n_canicas = 3000

niveles = 12

Define que se simularán 3000 canicas y 12 niveles.

resultados = simular_galton(n_canicas, niveles)

graficar_histograma(resultados)

Llama a las funciones para simular y luego graficar los resultados.

5. Resultado esperado

La gráfica mostrará una distribución similar a una campana de Gauss, con la mayoría de las canicas cayendo en los contenedores del medio (alrededor de 6), y menos en los extremos (0 o 12).

Proyecto 2 

Parte 1: Verificar longitud de palabra

Función: verificar_longitud_palabra()

✔ Objetivo:

Verifica cuántas letras tiene una palabra ingresada por el usuario y da un mensaje según su longitud.

Paso a paso:

Se le pide al usuario que ingrese una palabra.

Se calcula la longitud de esa palabra usando len(palabra).

Luego se usa una estructura if-elif-else para evaluar:

Si la longitud está entre 4 y 8 letras (inclusive), se dice que la palabra es correcta.

Si tiene menos de 4 letras, se indica que faltan letras.

Si tiene más de 8 letras, se indica que sobran letras.

Ejemplo:

Si el usuario escribe "gato", el programa responde:

La palabra es correcta.

Parte 2: Identificar el cuadrante de un punto

Función: identificar_cuadrante()

✔ Objetivo:

Determina en qué cuadrante del plano cartesiano se encuentra un punto (X, Y) ingresado por el usuario.

Paso a paso:

Se piden dos coordenadas: x y y. Se convierten a tipo float para permitir números decimales.

Usa try-except para capturar errores si el usuario no ingresa un número válido.

Luego evalúa en qué cuadrante está el punto:

Si x == 0 o y == 0, no se puede determinar el cuadrante, porque el punto está sobre un eje.

Según los signos de x e y, determina el cuadrante:

x > 0 y y > 0: Cuadrante I

x < 0 y y > 0: Cuadrante II

x < 0 y y < 0: Cuadrante III

x > 0 y y < 0: Cuadrante IV

Ejemplo:

Si el usuario escribe x = 2 y y = -5, el programa dirá:

El punto se encuentra en el cuadrante IV.

Ejecución del programa

Al final, el programa llama a ambas funciones:

verificar_longitud_palabra()

identificar_cuadrante()

Esto hace que:

Primero se ejecute la verificación de la palabra.

Luego se ejecute la verificación del cuadrante del punto.

Mis reflexiones que llevo hasta ahorta son las siguientes:
Gacias a los que llevo de clases me han ayudado bastante a mejorar mis conocimientos hacia la programacion, las clases son muy informativas y me estan ayudandon bastante, mediente pasan las clases ire mejorando. 

Proyecto 1 Calculadora imc

Este es el resumen de la realizacion de mi programa:

1. Funciones auxiliares para la entrada de datos
Se crean dos funciones para solicitar datos al usuario de forma segura:
   
*solicitar_texto(campo)
Recibe el nombre del campo (ej. "nombre", "apellido").
Usa un bucle while para asegurarse de que el usuario no deje el campo vacío.
.strip() elimina espacios al inicio y al final.
Si el usuario no ingresa nada, muestra un mensaje de error y vuelve a pedir el dato.

**solicitar_numero(campo)
Similar a solicitar_texto, pero verifica que el dato sea un número válido y mayor que cero.
Usa try-except para atrapar errores si el usuario no ingresa un número.
Convierte el valor a float.

2. Recolección de datos del usuario
Se utilizan las funciones anteriores para pedir al usuario:

Nombre

Apellido paterno

Apellido materno

Edad (en años)

Peso (en kilogramos)

Estatura (en metros)

3. Cálculo del IMC
   
El IMC (Índice de Masa Corporal) se calcula con la fórmula:

imc= peso/estatura**2

4. Mostrar los resultados
   
Se presentan los datos ingresados y el IMC calculado con dos decimales.

 5. Clasificación del IMC

Dependiendo del valor del IMC, se clasifica en diferentes categorías:

< 18.5: Bajo peso

18.5 - 24.9: Peso normal

25 - 29.9: Sobrepeso

30 - 34.9: Obesidad grado 1

35 - 39.9: Obesidad grado 2

≥ 40: Obesidad grado 3 (obesidad mórbida)

Esto se hace usando condicionales if-elif-else.

Las reflexiones que me a dado el curso son muy interesantes ya que esta mejorando mis conocimientos hacia la programacion ya que tengo noción de las estructuras de la misma ya que llevo desde la prepa ocupando programacion ya sea java, greenfood y c++ ya que las 4 son casi similares con sus estructuras de los codigos, pero el curso me esta ayudando a mejorar mis conocimientos

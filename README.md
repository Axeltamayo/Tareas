# Tareas
Proyecto 2 
🔹 Parte 1: Verificar longitud de palabra
Función: verificar_longitud_palabra()
✔️ Objetivo:
Verifica cuántas letras tiene una palabra ingresada por el usuario y da un mensaje según su longitud.

📌 Paso a paso:
Se le pide al usuario que ingrese una palabra.

Se calcula la longitud de esa palabra usando len(palabra).

Luego se usa una estructura if-elif-else para evaluar:

Si la longitud está entre 4 y 8 letras (inclusive), se dice que la palabra es correcta.

Si tiene menos de 4 letras, se indica que faltan letras.

Si tiene más de 8 letras, se indica que sobran letras.

🧪 Ejemplo:
Si el usuario escribe "gato", el programa responde:

nginx
Copiar
Editar
La palabra es correcta.
🔹 Parte 2: Identificar el cuadrante de un punto
Función: identificar_cuadrante()
✔️ Objetivo:
Determina en qué cuadrante del plano cartesiano se encuentra un punto (X, Y) ingresado por el usuario.

📌 Paso a paso:
Se piden dos coordenadas: x y y. Se convierten a tipo float para permitir números decimales.

Usa try-except para capturar errores si el usuario no ingresa un número válido.

Luego evalúa en qué cuadrante está el punto:

Si x == 0 o y == 0, no se puede determinar el cuadrante, porque el punto está sobre un eje.

Según los signos de x e y, determina el cuadrante:

x > 0 y y > 0: Cuadrante I

x < 0 y y > 0: Cuadrante II

x < 0 y y < 0: Cuadrante III

x > 0 y y < 0: Cuadrante IV

🧪 Ejemplo:
Si el usuario escribe x = 2 y y = -5, el programa dirá:

nginx
Copiar
Editar
El punto se encuentra en el cuadrante IV.
🔹 Ejecución del programa
Al final, el programa llama a ambas funciones:

python
Copiar
Editar
verificar_longitud_palabra()
identificar_cuadrante()
Esto hace que:

Primero se ejecute la verificación de la palabra.

Luego se ejecute la verificación del cuadrante del punto.


Calculadora imc

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

# Tareas
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

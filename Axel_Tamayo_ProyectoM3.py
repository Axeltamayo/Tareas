import random
import matplotlib.pyplot as plt

def simular_galton(n_canicas, niveles):
    """
    Simula el recorrido de n_canicas a través de una máquina de Galton con un número dado de niveles.
    Devuelve una lista con la cantidad de canicas que caen en cada contenedor.
    """
    contenedores = [0] * (niveles + 1)  # Hay niveles + 1 contenedores
    for _ in range(n_canicas):
        derecha = 0
        for _ in range(niveles):
            if random.random() > 0.5:
                derecha += 1  # La canica se va a la derecha
        contenedores[derecha] += 1  # El número de veces que se va a la derecha determina el contenedor
    return contenedores

def graficar_histograma(resultados):
    """
    Grafica un histograma con los resultados de la simulación.
    """
    plt.bar(range(len(resultados)), resultados, color='skyblue', edgecolor='black')
    plt.xlabel('Contenedores (posición final)')
    plt.ylabel('Número de canicas')
    plt.title('Simulación de una máquina de Galton con 3000 canicas y 12 niveles')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Parámetros de la simulación
n_canicas = 3000
niveles = 12

# Ejecutar simulación y graficar resultados
resultados = simular_galton(n_canicas, niveles)
graficar_histograma(resultados)
# Parte 1: Verificar longitud de palabra
def verificar_longitud_palabra():
    palabra = input("Ingresa una palabra: ")
    longitud = len(palabra)
    
    if 4 <= longitud <= 8:
        print("La palabra es correcta.")
    elif longitud < 4:
        print(f"Hacen falta letras. Solo tiene {longitud} letras.")
    else:
        print(f"Sobran letras. Tiene {longitud} letras.")

# Parte 2: Identificar el cuadrante de un punto
def identificar_cuadrante():
    try:
        x = float(input("Ingrese X: "))
        y = float(input("Ingrese Y: "))
        
        if x == 0 or y == 0:
            print("Ninguna coordenada puede ser 0.")
        elif x > 0 and y > 0:
            print("El punto se encuentra en el cuadrante I.")
        elif x < 0 and y > 0:
            print("El punto se encuentra en el cuadrante II.")
        elif x < 0 and y < 0:
            print("El punto se encuentra en el cuadrante III.")
        elif x > 0 and y < 0:
            print("El punto se encuentra en el cuadrante IV.")
    except ValueError:
        print("Por favor, ingrese números válidos para las coordenadas.")

# Ejecutar ambas funciones
verificar_longitud_palabra()
identificar_cuadrante()
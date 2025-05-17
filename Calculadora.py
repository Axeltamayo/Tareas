def solicitar_texto(campo):
    while True:
        valor = input(f"Ingrese su {campo}: ").strip()
        if valor:
            return valor
        else:
            print(f"⚠️  Error: El campo '{campo}' no puede quedar vacío.\n")

def solicitar_numero(campo):
    while True:
        valor = input(f"Ingrese su {campo}: ").strip()
        try:
            numero = float(valor)
            if numero > 0:
                return numero
            else:
                print(f"⚠️  Error: El valor de '{campo}' debe ser mayor que 0.\n")
        except ValueError:
            print(f"⚠️  Error: Debe ingresar un número válido para '{campo}'.\n")

# Solicitar datos
nombre = solicitar_texto("nombre")
apellido_paterno = solicitar_texto("apellido paterno")
apellido_materno = solicitar_texto("apellido materno")
edad = solicitar_numero("edad")
peso = solicitar_numero("peso en kilogramos")
estatura = solicitar_numero("estatura en metros")

print("\n--- Interpretación del IMC ---")

if imc < 18.5:
    print("Clasificación: Bajo peso")
elif 18.5 <= imc < 24.9:
    print("Clasificación: Peso normal")
elif 25 <= imc < 29.9:
    print("Clasificación: Sobrepeso")
elif 30 <= imc < 34.9:
    print("Clasificación: Obesidad grado 1")
elif 35 <= imc < 39.9:
    print("Clasificación: Obesidad grado 2")
else:
    print("Clasificación: Obesidad grado 3 (obesidad mórbida)")



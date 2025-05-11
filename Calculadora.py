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

# Calcular IMC
imc = peso / (estatura ** 2)

# Mostrar resultados
print("\n--- Datos del Usuario ---")
print(f"Nombre completo: {nombre} {apellido_paterno} {apellido_materno}")
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} m")
print(f"Índice de Masa Corporal (IMC): {imc:.2f}")


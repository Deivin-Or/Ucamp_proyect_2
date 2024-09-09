# Inicio de proyecto de Calculo de coordenadas

# Importe de libreria para graficar las coordenadas por medio de matplotlib
import matplotlib.pyplot as graf

# Bienvenida al usuario
welcome = "Bienvenido a la calculadora de coordenadas"
print(welcome.capitalize())
print("""Soy Toto y seré su calculador el día de hoy, muchogusto de trabajar contigo.""")

while True:
    num_dot = input("""Para empezar Toto necesita saber:
    ¿Cuántos puntos va a procesar?: """)
    if num_dot.isalpha():
        print("Toto no necesita el alfabeto por el momento")
    elif not num_dot.isdigit():
        print("Toto solo acepta valores númericos")
    elif (num_dot.count(".") >= 1) or (num_dot <= ("0")):
        print("Toto no puede trabajar con decimales, negativos o mixtos")
    elif int(num_dot) == 0:
        print("Toto no puede trabajar con un valor nulo")
    else:
        num_dot = int(num_dot)
        break

# Lista que contendran los resultados
x_coords = []
y_coords = []


# Listas que guardaran las repuestas y el color del cuadrante
result = []
dot_color = []

for position_dot in range(num_dot):
    print(f"Toto está ingresando la el punto No.{position_dot + 1}")

    # Ingreso de coordenadas en X
    while True:
        x_axis = input("Toto necesita la coordenada en el eje X: ")
        if x_axis == (""):
            print("Toto no puede trabajar con un valor vacío")
        elif x_axis  == ("0"):
            print("Toto no acepta valores nulos")
        elif x_axis .isalpha():
            print("Toto necesita un valor númerico")
        elif not (x_axis.isdigit() or (x_axis.startswith('-') and x_axis[1:].isdigit())):
            # x_axis.isdigit() evalua si es un numero y si encuntra al simbolo diferente a ello que marque true pero lo invierto con not
            # para poder continuar ya que quiero que de true a la hora que ideintifique alguna letra
            # (x_axis.startswith('-') and x_axis[1:].isdigit()) es por que quiero que a la hora de ingresar negativos los reconozco como numeros
            # ya que isdigit no reconoce el - tengo que hacer una función que de true a la hora de encontarlo para poder invertirlo al final con not
            # y el programa continue

            print("Toto no puede trabajar vales mixtos")
        else:
            x_axis = int(x_axis)
            break
    x_coords.append(x_axis)

    # Ingreso de coordenadas en y
    while True:
        y_axis = input("Toto necesita la coordenada en el eje y: ")
        if y_axis == (""):
            print("Toto no puede trabajar con un valor vacío")
        elif y_axis == ("0"):
            print("Toto no acepta valores nulos")
        elif y_axis.isalpha():
            print("Toto necesita un valor númerico")
        elif not (y_axis.isdigit() or (y_axis.startswith('-') and y_axis[1:].isdigit())):
            print("Toto no puede trabajar vales mixtos")
        else:
            y_axis = int(y_axis)
            break
    y_coords.append(y_axis)

    # Lista de respuestas
    message_quadrant = [
    """Toto detecta el cuadrante I.""",
    """Toto detecta el cuadrante II.""",
    """Toto detecta el cuadrante III.""",
    """Toto detecta el cuadrante IV."""
    ]

    if x_axis > 0 and y_axis > 0:
        result.append(message_quadrant[0])
        dot_color.append("green")
    elif x_axis < 0 and y_axis > 0:
        result.append (message_quadrant[1])
        dot_color.append("black")
    elif x_axis < 0 and y_axis < 0:
        result.append(message_quadrant[2])
        dot_color.append("purple")
    elif x_axis > 0 and y_axis < 0:
        result.append(message_quadrant[3])
        dot_color.append("blue")


# Creación y configuración del gráfico que generamos
fig, ax = graf.subplots()
ax.axhline(0, color = "black", linewidth=1)  # Eje X
ax.axvline(0, color = "black", linewidth=1)  # Eje Y
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
ax.grid(True, which = "both", linestyle = "--", linewidth = 0.5)

# Marcación de los puntos y anotación con coordenadas
for x_axis, y_axis, quadrant_result, color in zip(x_coords, y_coords, result, dot_color):
    if x_axis != 0 or y_axis != 0:
        ax.plot(x_axis, y_axis, "o", color=color)
        message = f"{result}\nCoordenadas: ({x_axis}, {y_axis})"
        ax.text(x_axis, y_axis, message, fontsize=12, color=color, ha="right")

# Función que muestra el gráfico final
graf.show()


print("Las coordenadas ingresadas y los cuadrantes correspondientes son:")
for result_list in range(num_dot):
    print(f"Punto {result_list + 1}: Coordenadas ({x_coords[result_list]}, {y_coords[result_list]}) - {result[result_list]}")

print("Toto ha terminado su trabajo, muchas gracias por usarlo.")
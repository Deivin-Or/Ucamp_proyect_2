# Inicio de proyecto de Calculo de coordenadas

# Importe de libreria para graficar las coordenadas por medio de matplotlib
import matplotlib.pyplot as graf

# Bienvenida al usuario
# Y presentación de mascota Toto
welcome = "Bienvenido a la calculadora de coordenadas"
print(welcome.capitalize())
print("""
        ⣴⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣾⡿⠉⠙⢿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⠛⢻⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣼⡿⠁⣀⡀⠀⠙⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠋⢠⣤⡄⠙⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣿⠃⢰⠏⠻⣄⠀⠈⢿⣷⠀⠀⠀⠀⠀⠀⣼⡿⠁⣴⠏⠀⢻⣆⠈⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣸⡟⠀⡟⠀⠀⠹⣦⠀⠘⠿⠿⠿⠿⠟⠻⠿⠿⠅⢸⠃⠀⠀⠀⢹⡄⠸⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⡇⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣰⣿⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⢻⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣾⡟⠀⠀⠀⢀⣠⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠞⠋⠈⢻⣄⠀⠀⠀⠀⠀⠘⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣸⣿⠁⠀⠀⢀⣾⠁⠈⠻⣦⡀⠀⠀⠀⠀⢀⣤⠶⠋⠁⠀⠀⠀⠀⠹⣦⠀⠀⠀⠀⠀⠹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⠇⠀⠀⢀⡾⠁⠀⠀⠀⠈⠙⢷⣄⣠⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠘⠷⠤⢤⣄⠀⠀⢻⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⣿⢰⡟⠉⠉⡁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠘⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⡏⠈⣷⠀⠀⣿⣿⣷⡄⠀⠀⠀⢠⣤⣤⣤⣤⠀⠀⠀⠀⢠⣾⣿⣿⠀⠀⠀⠰⢿⣤⣄⡀⠀⢿⣷⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀
⣿⡇⠀⣸⡆⠀⠹⣿⣿⠇⠀⠀⠀⠸⠿⠿⠿⠿⠀⠀⠀⠀⠸⠿⠿⠋⠀⠀⠀⠀⠀⠀⢸⡇⠀⠘⣿⡆⠀⠀⠀⣠⣴⣾⠿⠛⢻⣿⠃
⣿⠁⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣶⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣟⣠⣴⣿⠿⠃⠀⣴⣾⡿⠋⠁⠀⠀⢸⡇⠀
⣿⣷⣬⣿⣄⣀⠀⠀⠀⠀⠀⠀⠘⢿⣏⠙⢀⣽⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⠿⠛⠉⠀⠀⣠⣾⡟⠋⠀⠀⠀⠀⠀⢸⡇⠀
⠀⠈⠉⠛⠛⠻⠿⢷⣶⣦⣤⣀⣀⣘⠛⠿⠟⠋⠀⢀⣀⣀⣀⣤⣴⣶⣶⠿⢿⣿⣅⠀⠀⠀⠀⠀⢠⣿⠏⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢹⡟⠛⠛⠿⠿⠿⠿⠿⠛⠛⠛⠋⠉⠉⠀⠀⠀⠀⠙⣿⣧⡀⠀⠀⠀⢸⡿⠀⣠⣤⡆⠀⠀⠀⠀⠀⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⡇⠀⠀⠀⠀⢤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣷⡀⠀⠀⢸⣷⠞⠋⢰⡇⠀⢀⣀⡀⠀⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⣶⡆⠀⠀⠀⠀⠀⠈⢿⣧⠀⠀⢸⡇⠀⠀⠀⠷⠴⠟⠁⢷⣼⣿⠀
⠀⠀⠀⠀⠀⠀⣾⡿⠿⣿⣾⣿⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⢠⣿⣥⣶⡿⠿⢿⣦⠀⠈⣿⡇⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⣸⣿⠃⠀
⠀⠀⠀⠀⠀⠀⣿⡇⠀⠈⢿⣿⡶⣄⣀⡴⠿⣿⣄⠀⣠⠶⠛⢹⣿⠟⠁⠀⠀⠈⣿⡇⠀⢹⣷⣾⡿⠁⠀⠀⠀⠀⠀⣠⣾⡿⠃⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣷⡀⠀⠈⢿⣇⠈⠉⠀⠀⣿⠛⠛⠁⠀⠀⢸⡇⠀⠀⠀⠀⢀⣿⠇⠀⢸⣿⠉⠀⠀⠀⠀⢀⣠⣾⡿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢿⣷⣄⡀⣸⣿⡀⠀⠀⢀⣿⡄⠀⠀⠀⠀⣸⡇⠀⠀⢀⣠⣾⡟⠀⢀⣾⣟⠀⣀⣠⣴⣾⠿⠛⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠻⠿⠿⠟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
Soy Toto y seré su calculador el día de hoy, mucho gusto de trabajar contigo.\n""")

# Pedida de cantidad de puntos a encontrar dentro del plano cartesiano
# Además del filtro de control para evitar error en el proceso
while True:
    num_dot = input("""Para empezar Toto necesita saber:
    ¿Cuántos puntos va a procesar?: """)
    if num_dot.isalpha():
        print("Toto no necesita el alfabeto por el momento")
    elif not num_dot.isdigit():
        print("Toto solo acepta valores númericos")
    elif (num_dot.count(".") >= 1) or (num_dot <= ("0")): # Función para no dejar pasar decimales o negativos
        print("Toto no puede trabajar con decimales, negativos o mixtos")
    elif int(num_dot) == 0:
        print("Toto no puede trabajar con un valor nulo")
    else:
        num_dot = int(num_dot)
        break

# Lista que contendran los resultados
# Para lluego agrergar el contenido con .append()
x_coords = []
y_coords = []


# Listas que guardaran las repuestas y el color del cuadrante
# Para lluego agrergar el contenido con .append() y asi poder modificar cada resultado en la impresión final
result = []
dot_color = []

# Itinerante que separara cada punto con cada cordenada para diferente eje y asi imprimir cada punto de forma separada
# en uns solo mismo plano
# Asi que la función contendra todo los bloque de código ya que cada punto pasara por el mismo proceso
for position_dot in range(num_dot):
    print(f"\nToto está ingresando la el punto No.{position_dot + 1}")

    # Ingreso de coordenadas en X
    while True:
        x_axis = input("\nToto necesita la coordenada en el eje X: ")
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
            print("Toto no puede trabajar valores mixtos o decimales.")
        else:
            x_axis = int(x_axis)
            break
    x_coords.append(x_axis)

    # Ingreso de coordenadas en y
    while True:
        y_axis = input("\nToto necesita la coordenada en el eje y: ")
        if y_axis == (""):
            print("Toto no puede trabajar con un valor vacío")
        elif y_axis == ("0"):
            print("Toto no acepta valores nulos")
        elif y_axis.isalpha():
            print("Toto necesita un valor númerico")
        elif not (y_axis.isdigit() or (y_axis.startswith('-') and y_axis[1:].isdigit())): 
            # uso del not ya que necesito que se invierta ya que se identifican
            # ya que no hay una cadena que compare o precese solo los numeros negativos y positivos a la misma vez, y iedentificar si hay letras para evitar errores
            # se usa or ya que si es negativo dara true en la parte (y_axis.startswith('-') and y_axis[1:].isdigit()) y asi poder invertir el valor final de true a false 
            # Lo mismo seria si fuera positivo dara solo true en .isdigit y con eso bastaria ya que da solo necesitari invertir con not
            # ya que or solo necesita un true para ser true 
            print("Toto no puede trabajar valores mixtos o decimales.")
        else:
            y_axis = int(y_axis)
            break
    y_coords.append(y_axis)

    # Lista de respuestas
    # Se usa una lista en dado caso de necesitar más
    message_quadrant = [
    """Toto detecta el cuadrante I.""",
    """Toto detecta el cuadrante II.""",
    """Toto detecta el cuadrante III.""",
    """Toto detecta el cuadrante IV."""
    ]

    # Identificación de cuadrante
    # y compradore de coordenadas
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
ax.axhline(0, color = "black", linewidth = 1)  # Eje X
ax.axvline(0, color = "black", linewidth = 1)  # Eje Y
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
ax.grid(True, which = "both", linestyle = "--", linewidth = 0.5)

# Marcación de los puntos y anotación con coordenadas
for x_axis, y_axis, quadrant_result, color in zip(x_coords, y_coords, result, dot_color):
    if x_axis != 0 or y_axis != 0:
        ax.plot(x_axis, y_axis, "o", color = color)
        message = f"{result}\nCoordenadas: ({x_axis}, {y_axis})"
        ax.text(x_axis, y_axis, message, fontsize=12, color=color, ha="right")

# Función que muestra el gráfico final
graf.show()


#Impresión para la terminal y asi evitar el uso de la libreria si se necesita, puede quedarse ya que no afecta ala gráfica ya que solo imprime datos adicionales en el terminal.
print("""------------------------------------------------------------------------------------------------------------
\nLas coordenadas ingresadas y los cuadrantes correspondientes son:\n""")
for result_list in range(num_dot):
    print(f"""Punto {result_list + 1}: Coordenadas ({x_coords[result_list]}, {y_coords[result_list]}) - {result[result_list]}\n
------------------------------------------------------------------------------------------------------------""")

print("\nToto ha terminado su trabajo, muchas gracias por visitarlo hasta la próxima")
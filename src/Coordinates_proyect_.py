# Inicio de proyecto de Calculo de coordenadas

# Importe de libreria para graficar las coordenadas por medio de matplotlib
import matplotlib.pyplot as graf

# Bienvenida al usuario
welcome = "Bienvenido a la calculadora de coordenadas"
print(welcome.capitalize)
print("""
                                                ..-+*%%@@%#+-.                                      
                                          .-#@@@@%%#*+===++*#%@@@@@+:.                              
                                    ...+%@@%+:...             ....-*@@@#:.                          
                                   :@@@@:.                          ...#@@@:.                       
                               .-@@@+.                                   .#@@@:                     
                            ..*@@+...                            ...-*%@@@@@@@@*..                  
                           .@@@:.                            .+%@@@@@@@@@@@@@--@@-                  
                        ..%@%.                       .:-#@@@@@@@@@@@@@@@@@@@#-..*@#.                
                       .#@%:.               ...:=#%@@@@#=%@..%*@@@@@@@@@@@@@..  .-@%.               
                      -@@-.              :*@@@@@@@@@@@@%**.=@=:=.%@@@@@@@@%       =@*               
                    .#@#.       ..:+%@@@@@@@@@@@@@@@@@@%@@@@..@@#@@@@@@@@=         %@.              
                   .@@- ...:+#@@@@@@-=@@@@@@@@@@@@@@%...:-=@@@@@@@@@@%*=:.         #@-              
                 .:@@=#@@@@@#@@@+.##*@:.%@@@@@@@@@@+..    ...@@#-...               %@.              
                .-@@+#=..   .=:@@@@-+::@*.*@@@@@@@+:                              #@+               
               .-@@@@.         ..+@@@%@@@@@@@@@@@#-                            .-@@=.               
               -@@.                .*=@@@@@*:...                              .%@#.                 
              .@@.                   ...                                    .#@%.                   
             .%@-.                                                       ..#@@:.                    
            .*@+.                                                     ..*@@%..                      
            :@%.                                                  ..=@@@%@%                         
           .@@:.                                              ..+%@@%=.. +@+.                       
           -@#.                                           .:#@@@%-..     .@@.                       
          .@@.           ..                          .:+@@@@#:            -@#.                      
          =@#.          -@*.                 ...:=#@@@@*-...              .%@:.                     
          #@..          .*@%:            .-*%@@@@%=:.                      :@@.                     
         :@%              .#@@@@@@@@@@@@@@@#=..                             #@=.                    
         *@+                .....::......                                   .@@.                    
         %@.                                                                .+@*.                   
       ..@#                                                                  .%@.                   
       .+@+                                        =%%+-..                   .=@#.                  
       .%@-                                        %@@@@@:      :#%*.         .%@.                  
       .@@.                                        .%@@@@@:.=@@@@@@@.          -@%.                 
      ..@%.                                          .=@@@@@@@@@@@%:.          .%@:                 
      .:@*                                            .@@@@@@@@@*              .:@%.                
      .+@=          *@=                          ..:#@@@@@@@@@@@@               .@@-                
      .#@-          #@.                    ..:=#@@@%*-.:@@@@@@@@:               ..@#.               
      .@@:          *@=               ..=#%@@@%=:.      ..+@@@@@.                 %@-               
      .@@.           #@@+.......-*@@@@@@@+.                                       -@#               
      .@@.           ..=#%@@@@%%#*=:...                                            %@:              
      :@@.                                                                         =@#              
      :@#                                                                           @@..            
     .-@*                                                                           +@=.            
     .-@+                                                                           :@@.            
     .=@=                                                                           .%@..           
     .+@-                                                                            =@+.           
     .*@:                                                                            :@@.           
     .*@:                                                                            .@@:           
     .#@.                                                                             #@-.          
     .%@.                                                                             +@=.          
     .@@.                                                                             =@+.          
     .@@.                                                                             +@=.          
     .@@.                                                                            .%@:           
      ...                                                                             ...           
                                                                                            """)

print("""Soy Toto y seré su calculador el día de hoy, muchogusto de trabajar contigo.""")

while True:
    num_dot = int(input("""Para empezar Toto necesita saber:
    ¿Cuántos puntos va a procesar?: """))
    if num_dot == 0:
        print("Toto no puede trabajar con un valor nulo")
    elif num_dot.isalpha():
        print("Toto no necesita el alfabeto por el momento")
    elif all (num_dot.coun(".") > 1 or num_dot.count("-") > 1):
        print("Toto no puede trabajar con decimales o negativos")
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
        else:
            x_axis = int(x_axis)
            break
    x_coords.append(x_axis)

    # Ingreso de coordenadas en y
    while True:
        y_axis_in = input("Toto necesita la coordenada en el eje y: ")
        if y_axis_in == (""):
            print("Toto no puede trabajar con un valor vacío")
        elif y_axis_in == ("0"):
            print("Toto no acepta valores nulos")
        elif y_axis_in.isalpha():
            print("Toto necesita un valor númerico")
        else:
            y_axis = int(y_axis_in)
            break
    y_coords.append(y_axis)

    # Lista de respuestas
    message_quadrant = [
    """Toto detecta \nel cuadrante I.\n""",
    """Toto detecta \nel cuadrante II.\n""",
    """Toto detecta \nel cuadrante III.\n""",
    """Toto detecta \nel cuadrante IV.\n"""
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
        result = message_quadrant[3]
        dot_color.append("blue")


# Creación del gráfico
fig, ax = graf.subplots()
ax.axhline(0, color = "black", linewidth=1)  # Eje X
ax.axvline(0, color = "black", linewidth=1)  # Eje Y
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
ax.grid(True, which = "both", linestyle = "--", linewidth = 0.5)

# Marcación de los puntos y anotación con coordenadas
for x_axis, y_axis, result, color in zip(x_coords, y_coords, result, dot_color):
    if x_axis != 0 or y_axis != 0:
        ax.plot(x_axis, y_axis, "o", color=color)
        message = f"{result}\nCoordenadas: ({x_axis}, {y_axis})"
        ax.text(x_axis, y_axis, message, fontsize=12, color=color, ha="right")

# Mostrar el gráfico
graf.show()
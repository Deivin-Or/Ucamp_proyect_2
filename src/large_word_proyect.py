# Inicio proyecto longitud de palabra
# Bienvenida usuario y presentación de Toots
print("""Bienvenido al detector de longitud de palabra
¡Hola soy Toots! Tu revisador de palabras, te indicaré si tu palabra tiene
la longitud correcta para poder ser un hashtag de Twitter **o X en este caso** :3\n

    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠾⠛⠋⠉⠉⠀⠀⠀⠉⠉⠉⠛⠻⠶⣤⣄⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⡶⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢶⣤⡀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣴⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠰⣼⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠈⠻⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀
⢀⡐⣴⠟⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣾⣷⡄⠀⠀⠀⠀⠀⠀
⣬⣿⠃⠀⠀⢠⣤⡄⠀⠀⠀⠀⠉⠲⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢷⣤⣄⣀⣀⡀⠀
⣿⣿⣄⠀⠀⣸⣿⡁⠀⠀⠀⠀⠀⣴⠀⠀⠈⠛⠻⠿⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣤⡽⠇⠀
⣿⣿⡛⠛⠛⠋⠈⠻⢦⣤⣠⣤⡾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣶⡄
⠈⠛⠿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⡶⢾⠛⠇
⠀⠀⠀⠀⢭⡛⣷⢶⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀⠀⠀⠀⠀⠀⢿⣄⣀⣤⣤⣴⣶⠟⠛⠋⢉⣤⣶⣮⠀⠀
⠀⠀⠀⠀⠀⣶⣇⠀⢀⣽⠟⠛⠛⠛⠛⠿⠿⠷⠶⠶⠶⠶⠶⠶⠶⠶⠾⢷⣤⣀⠀⢀⣠⣾⠟⠉⠁⠀⠈⢿⡟⠶⣶⣿⣿⡿⠟⠀⠀
⠀⠀⠀⠀⠀⠉⠛⢷⣾⠇⠀⢀⣤⣤⡀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠘⣷⠀⠸⣏⠹⣧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣼⡏⠀⠀⢺⣿⣿⡇⠀⠀⣟⠀⢰⣆⠀⠘⣷⠀⠀⠀⢰⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠻⣦⡿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⡇⢰⢤⡌⠉⠁⠀⠀⠀⠻⠶⠟⠙⠷⠾⠋⠀⠀⠀⠘⠿⠿⠿⠁⣀⢠⡄⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣿⣷⠈⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠚⠋⠀⠀⠀⠀⢠⡟⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣄⠀⢿⣟⢷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣤⢀⣆⣤⣀⣿⠀⢸⡏⠙⠛⠿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⣛⣿⡿⣿⡿⢛⡁⠸⢷⣀⠀⠀⠀⠈⠙⡛⠷⢶⣤⣤⣤⣀⣀⣀⣀⣀⣀⣠⣤⣤⡶⠾⣿⣋⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      
    ¡Empecemos!\n""")

# inicio ciclo while para verificar longitud de palabra
while True:
    # Ingreso de datos por usuario
    word = input("Escribe tu palabra, Toots te espera: ")
    # Se toma la longitud de la palbra en otro variable para evitar la mezcla de valos por si queremos usar la parabara para otra impresión o función.
    word_longer = len(word)

    # Estructara de control que identidica la cantidad de caracteres que falten, sobre o den con la longitud correcta
    if 4 <= word_longer <= 8:
        print("\nLa cantidad de letras es correcta puede seguir, Toots te felicita\n")
        break
    elif word_longer < 4:
        missing = 4 - word_longer
        print(f"Toots detecta que tu palabra {word} es demasiado corta\n Letras que le faltan a Toots ---> { missing}\nToots reinicia proceso.\n")
    elif word_longer > 8:
        missing = word_longer - 8
        print(f"Toots detecta que tu palabra {word} es demasiado larga\n Letras que le sobran a Toots ---> {missing}\nToots reinicia proceso.\n")

# Bloque de código de resultados finales, imprimiendo la palbra ingresad y la despidad de Toots.
print(f"""-----------------------------------------------------------------------------
La palabra {word} es aprobada por Toots tiene la longitud correcta.\n
¡Felicidades Toots te desea un buen día, hasta la próxima :3
-----------------------------------------------------------------------------""")


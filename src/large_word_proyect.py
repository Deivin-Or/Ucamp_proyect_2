# Inicio proyecto longitud de palabra
# Bienvenida usuario y presentación de Toots
print("""Bienvenido al detector de longitud de palabra
¡Hola soy Toots! Tu revisador de palabras, te indicaré si tu palabra tiene
la longitud correcta para poder ser un hashtag de Twitter **o X en este caso** :v\n

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

while True:
    word = input("Escribe tu palabra, Toots te espera: ")
    word_longer = len(word)
    if 4 <= word_longer <= 8:
        print("La cantidad de letras es correcta puede seguir, Toots te felicita")
        break
    elif word_longer < 4:
        missing = 4 - word_longer
        print(f"Toots detecta que tu palabra {word} es demasiado corta\n Letras que le faltan a Toots --->{ missing}\nToots reinicia proceso.\n")
    elif word_longer > 8:
        missing = word_longer - 8
        print(f"Toots detecta que tu palabra {word} es demasiado larga\n Letras que le sobran a Toots ---> {missing}\nToots reinicia proceso.\n")

print(f"""-----------------------------------------------------------------------------
La palabra {word} es aprobada por Toots tiene la longitud correcta.\n
¡Felicidades Toots te desea un buen día, hasta la próxima :3""")


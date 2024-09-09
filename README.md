# Ucamp_proyect_2
Repositorio destinado para el almacenamiento de proyectos del Módulo 2 de Ucamp "bootcamp fundamentos de Python".

OJO: Este repositorio hace uso de libreias para la generación de gráficas, por esa razón se deja el archivo requerimients.txt que contitne 
las librerias necesarias para la ejecución del proyecto, esto con la finalidad paraq ue puedea configurar su entorno de desarrollo y se evito la subida del archivo .env para eviotar problemas de compatibilidad. Esto es especificamente para la funcionalidada del archivo Coordinates_proyect_.py.

Alternativa: si por razones mayores no puede instalar las librerias en su entorno de desarrollo o solo quiere verificar la funcionalidad del código, solo debe convertir a comentarios los bloques de generación y configuración de gráfico hasta la Función que muestra el gráfico final, ya que este código se penso támbien para que imprimiera las coordenadas y cuadrantes finales. (Esto solo quitará la función de gráfica y no provocara errores en el código)

Contenido del repositorio:
Programa de calculo de longitud de palabra = Word_length.py
Programa de calculo de coordenadas = Coordinates_proyect.py

Tamaño de archivos:
large_word_proyect.py = 9kb ---> En disco = 12kb
Coordinates_proyect_.py = 5kb ---> En disco = 8kb

Tamaño completo de proyectos (Todos los archivos y librerias) = 114MB (En disco 121MB)

----------------------------------------------------------------------------------------------------------------------------------------------

Proyecto 1: large_word_proyect.py

Programa dirigido al calculo de longitud de una palabra de entre 4 y 8 caracteres.
Indica la cantidada de caracteres faltantes y sobrantes que tiene la palbra, tambien puede modificarse lasa longitudes si es necesario y además cuenta con la variable "word" de manera separada para que pueda utilizarse en otros funciones en actualizaciones futuras y no mezclar los valores.

En este programa se admiten tanto letras, números y simbolos ya que la función "len" de python es capaz de contarlos y asi puede verificar las palabras sin importar el idioma o clave que se utilize.

Nota: si se necesitara un filtro para las palabras se dara en próximas actualziaciones o se creara un nuevo código con dicha función.

El usuario estará acompañado por Toots la mascota de mi código, (Cuidenla por mi).

----------------------------------------------------------------------------------------------------------------------------------------------

Proyecto 2: Coordinates_proyect_.py

Programa dirigido para el calculo de coordenadas dentro de un plano cartesiano de hasta 100 puntos en cada eje (A qui se incluyen los negativos).

El usuario primero debe ordenar cuantas coordenadas quiere encontrar dentro del plano, luego podrá ingresar los numeros en cada eje para encontrar su cuadrante y coordenadas exactas al que pertenecen. Se le implemeto filtros para que no se puedan ingresar valores que afeten a la lectura como letras o números que no sean compatibles con el programas. (En dado caso que se encuentre un error por favor de infomar para poder solucionarlo o implementar un nuevo filtro, ya que en próximas actualizaciones o en un código nuevo se implementarán nuevas funciones para mejorar la lectura y poder usar hasta expresiones algebraicas pero será dentro de un futuro).

Este programa genera una gráfica para poder ser más especifica (Si se tienen las librerias) y una parte que imprime en terminal uno por uno cada punto que se haya ingresado en el programa para poder evitar la mezcla de coordenadas el usuario puede seleccionar que coordenadas necesita.

Develoopers:
La parte gráfica y la de impresión fueron separadas por la razón si se desea usar la gráfica o solo la impresión por terminal, esto queda dependiendo el gusto o la necesidad de cada programador, tambien permite elegir dejar comentado o eliminar ese frag,mento de código ya que no provocara errores, en dado caso de no instalar las librerias de requerimients.txt se recomeinedo eliminar el bloque de código de gráfica para no provocar problemas.

Notas: en este caso se notaran casos nuevos como ejemplo las listas vacias, estas se dejaron vacias ya que pense utilizarlas como variables que luego llenare, ya que los datos depeneden del usuario y asi poder agregarlas por medio de la función para lisatas .append (Agregar al final), y asi poder resolver el problema de solo poder ingresar un punto en el plano cartesiano, además que tambein ayuda a agregar los resltados y colores para que se vayan generando en conjunto y resolver el problema de impresión de resultados ya que solo en las comparaciones solo se necesita cambiar los indices que se agreagaran con .append y asi cambia cada impresión.

En la impresión por terminal funcióna de la misma manera ya que for iterara por el rango definido por el usuario en num_dot y generar cada respuesta ya que cada resultado de cada comparación solo cambiara el indice para mostrar el resultado de cada punto.

No se permite el uso de ceros (De acuerso a las instrucciones dadas en el documento de guía de proyecto del Módulo 2), asi que no se agrego ninguna función para demostar que el punto este en el origen o en un solo vertice, ya que se solicitó que siempre X, Y tengan las coordenadas diferentes a 0. Se puede agregar en próximas actrualizacione si llega a ser necesario.

----------------------------------------------------------------------------------------------------------------------------------------------

Comentarios:
Este es el programa que más me a costado crear hasta el momento ya que hay muchas nuevas funciones como las librerias, listas, entornos de desarrollo. para ser sincero llegue hasta el punto de creer que no lo hiba a lograr ya que a la hora de hacer la gráfica no me salia del todo y más aún cuando tenia que hacer posible que separar del código si en dado caso el usurio no instalará la libreria, fue algo nuevo y desafiante. 
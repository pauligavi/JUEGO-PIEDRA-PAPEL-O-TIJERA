# JUEGO-PIEDRA-PAPEL-O-TIJERA
Introducción:
Este proyecto consiste en el desarrollo del juego Piedra, Papel o Tijera en Python, donde el usuario juega contra la computadora.
El objetivo es aplicar funciones, estructuras de control y estructuras de datos para mejorar la organización del código.

Desarrollo:
El juego permite al usuario elegir una opción, mientras que la computadora selecciona otra de forma aleatoria.
Inicialmente, el programa funcionaba correctamente, pero utilizaba condicionales directos.
Luego, el código fue mejorado incorporando estructuras de datos para hacerlo más ordenado, claro y fácil de entender.

Resultados:
Al comparar el código inicial con el código modificado, se realizaron los siguientes cambios:
-Se agregó una tupla llamada opciones para almacenar piedra, papel y tijera, ya que estos valores no cambian.
-Se agregó un diccionario llamado reglas para definir qué opción gana a otra, reemplazando varias condiciones if.
-Se agregó un diccionario llamado puntaje para llevar el conteo de partidas ganadas por el usuario y la máquina.
-Se modificó la función eleccion_usuario() para mostrar las opciones usando la tupla.
-Se modificó la función eleccion_maquina() para que elija usando la tupla opciones.
-Se modificó la función ganador() para usar el diccionario reglas y actualizar el puntaje.
-Se añadieron comentarios para explicar cada parte del código y facilitar su comprensión.

Conclusión
El desarrollo de este proyecto permitió aplicar correctamente las funciones y estructuras de datos en Python.
La implementación de tuplas y diccionarios mejoró la organización, claridad y mantenimiento del código, sin afectar el funcionamiento del juego.
Gracias a estas mejoras, el programa es más fácil de entender, explicar y ampliar en el futuro.

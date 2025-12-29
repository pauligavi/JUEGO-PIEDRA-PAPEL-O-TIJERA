import random  # Importo la librería random para que la máquina pueda elegir al azar

# TUPLA: contiene las opciones del juego
opciones = ("piedra", "papel", "tijera")

# DICCIONARIO: define las reglas del juego
reglas = {
    "piedra": ("tijera",),
    "papel": ("piedra",),
    "tijera": ("papel",)
}

# DICCIONARIO: almacena el puntaje del juego
puntaje = {
    "usuario": 0,
    "maquina": 0
}

# FUNCIÓN: Muestra una pantalla de bienvenida
def bienvenida():
    """
    Muestra un mensaje inicial cuando inicia el programa.
    Esta función solo imprime texto decorativo.
    """
    print("      ¡Bienvenido al juego! 🗿 📄 ✂️")
    print("        Piedra, Papel o Tijera")


# FUNCIÓN: la elección del usuario
def eleccion_usuario():
    """
    Muestra el menú de opciones al usuario.
    Valida que la entrada sea correcta.
    Devuelve 'piedra', 'papel' o 'tijera'.
    """

    print("\nElige una opción:")

    # Recorremos la tupla opciones para mostrar el menú
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion.capitalize()}")

    opcion = input("Ingresa el número de tu elección: ")

    # Validación de entrada: solo acepta 1, 2 o 3
    while opcion not in ["1", "2", "3"]:
        print("Opción inválida. Intenta de nuevo.")
        opcion = input("Ingresa 1, 2 o 3: ")

    # Convertimos el número ingresado en la opción correspondiente
    return opciones[int(opcion) - 1]

# FUNCIÓN: Elección automática de la máquina
def eleccion_maquina():
    """
    Retorna una elección aleatoria usando random.choice.
    La máquina puede escoger: piedra, papel o tijera.
    """
    return random.choice(opciones)

# FUNCIÓN: Determinar ganador del juego
def ganador(usuario, maquina):
    """
    Compara las elecciones del usuario y de la máquina
    usando el diccionario de reglas.
    Retorna un mensaje con el resultado.
    """

    # Si ambos eligen lo mismo, es empate
    if usuario == maquina:
        return "Empate"

    # Si la elección de la máquina está dentro de lo que gana el usuario
    if maquina in reglas[usuario]:
        puntaje["usuario"] += 1  # Aumenta el puntaje del usuario
        return "¡GANASTE! 🎉"

    # Caso contrario, gana la máquina
    puntaje["maquina"] += 1
    return "Perdiste 😢"


# FUNCIÓN PRINCIPAL DEL JUEGO
def jugar():
    """
    Controla todo el flujo del juego:
    - Muestra la bienvenida
    - Permite jugar varias rondas
    - Muestra el puntaje
    """

    bienvenida()  # Llamamos a la bienvenida

    continuar = "si"  # Variable para controlar el ciclo repetitivo

    # Ciclo que se repetirá mientras el usuario quiera seguir jugando
    while continuar.lower() == "si":

        # Obtener la elección del jugador y de la máquina
        usuario = eleccion_usuario()
        maquina = eleccion_maquina()

        # Mostrar las elecciones
        print(f"\nTú elegiste: {usuario}")
        print(f"La máquina eligió: {maquina}")

        # Determinar el ganador
        resultado = ganador(usuario, maquina)
        print("\nResultado:", resultado)

        # Mostrar el puntaje actual
        print(f"Puntaje → Tú: {puntaje['usuario']} | Máquina: {puntaje['maquina']}")

        # Preguntar si desea jugar otra vez
        continuar = input("\n¿Quieres jugar de nuevo? (si/no): ")

        # Validar respuesta
        while continuar.lower() not in ["si", "no"]:
            continuar = input("Ingresa 'si' para sí o 'no' para no: ")

    # Mensaje final cuando el usuario decide terminar
    print("\nGracias por jugar ❤️ ¡Vuelve pronto!")

# INICIO DEL PROGRAMA
jugar()  # Llamo a la función principal para iniciar el juego







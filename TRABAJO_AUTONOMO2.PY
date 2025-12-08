import random  # Importo la librería random para que la maquina pueda elegir al azar
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
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    
    opcion = input("Ingresa el número de tu elección: ")

    # Validación de entrada: solo acepta 1, 2 o 3
    while opcion not in ["1", "2", "3"]:
        print("Opción inválida. Intenta de nuevo.")
        opcion = input("Ingresa 1, 2 o 3: ")

    # Convertimos el número a texto
    if opcion == "1":
        return "piedra"
    elif opcion == "2":
        return "papel"
    else:
        return "tijera"
# FUNCIÓN: Elección automática de la máquina
def eleccion_maquina():
    """
    Retorna una elección aleatoria usando random.choice.
    La máquina puede escoger: piedra, papel o tijera.
    """
    return random.choice(["piedra", "papel", "tijera"])
# FUNCIÓN: Determinar ganador del juego
def ganador(usuario, maquina):
    """
    Compara las elecciones del usuario y de la máquina y
    determina quién gana según las reglas tradicionales.
    Retorna un mensaje explicando el resultado.
    """

    # Si ambos eligen lo mismo → empate
    if usuario == maquina:
        return "Empate"

    # Condiciones donde el usuario gana
    if (
        (usuario == "piedra" and maquina == "tijera") or
        (usuario == "papel" and maquina == "piedra") or
        (usuario == "tijera" and maquina == "papel")
    ):
        return "¡GANASTE! 🎉"

    # Si no es empate ni victoria → el usuario pierde
    return "Perdiste 😢"
# FUNCIÓN PRINCIPAL DEL JUEGO
def jugar():
    """
    Controla todo el flujo del juego:
    - Muestra la bienvenida
    - Permite jugar varias rondas mediante un ciclo while
    - Llama a todas las demás funciones
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

        # Determinar el ganador llamando a la función correspondiente
        resultado = ganador(usuario, maquina)
        print("\nResultado:", resultado)

        # Preguntar si desea jugar otra vez
        continuar = input("\n¿Quieres jugar de nuevo? (si/no): ")

        # Validar respuesta
        while continuar.lower() not in ["si", "no"]:
            continuar = input("Ingresa 'si' para sí o 'no' para no: ")

    # Mensaje final cuando el usuario decide terminar
    print("\nGracias por jugar ❤️ ¡Vuelve pronto!")


# -------------------------------------------------------
# INICIO DEL PROGRAMA
# -------------------------------------------------------
jugar()  # Llamo a la función principal para iniciar el juego
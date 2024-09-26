import random


opciones = ["piedra", "papel", "tijeras"]

def ordenador_decide_jugada():
    res = random.choice(opciones)
    return res


def usuario_decide_jugada():
    eleccion_usuario = input("Elige piedra, papel o tijeras: ")
    while eleccion_usuario not in opciones:
        eleccion_usuario = input("Opción no válida, por favor elige piedra, papel o tijeras: ")
    return eleccion_usuario


def determina_ganador(jugada_usuario, jugada_ordenador):
    if jugada_usuario == jugada_ordenador:
        return "Empate"
    elif jugada_usuario == "piedra" and jugada_ordenador == "tijeras":
        return "Ganaste"
    elif jugada_usuario == "tijera" and jugada_ordenador == "papel":
        return "Ganaste"
    elif  jugada_usuario == "papel" and jugada_ordenador == "piedra":
        return "Ganaste"
    else:
        return "Perdiste"


# Ejercicio 3 (avanzado)
def jugar_torneo():
    print("Hello, this is game 'rock paper and scissors'!\n---Print control+c to exit---\n")
    user_score = 0
    computer_score = 0
    while True:
        computer_choice = ordenador_decide_jugada()
        user_choice = usuario_decide_jugada()

        if determina_ganador(user_choice, computer_choice) == "Ganaste":
            user_score += 1
        elif determina_ganador(user_choice, computer_choice) == "Empate":
            pass
        else:
            computer_score += 1

        print(f"\nComputer chose {computer_choice}\n{determina_ganador(user_choice, computer_choice)} !\nYour score: {user_score}, Computer Score: {computer_score}\n---Print control+c to exit---\n")

        if computer_score == 3:
            print("Computer win in this tournament")
            break
        elif user_score == 3:
            print("You win this tournament !")
            break
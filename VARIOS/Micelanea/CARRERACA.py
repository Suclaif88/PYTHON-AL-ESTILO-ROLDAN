import random
import time

def print_race(*horse_positions):
    print("\n" * 30)  # Limpia la consola para una nueva impresión
    track_length = 100  # Longitud de la pista
    print("Carrera de caballos:")
    for i, pos in enumerate(horse_positions, 1):
        print(f"Caballo {i}:", ">" if pos >= track_length else " " * pos + ">")
    print("-" * track_length)
    time.sleep(0.5)  # Pausa para hacer la animación más fluida

def race():
    num_horses = 7
    horse_positions = [0] * num_horses

    while max(horse_positions) < 100:  # Carrera hasta que un caballo llegue al final de la pista
        # Avance aleatorio de los caballos
        for i in range(num_horses):
            horse_positions[i] += random.randint(1, 3)
        print_race(*horse_positions)

    winners = [i + 1 for i, pos in enumerate(horse_positions) if pos >= 100]
    if len(winners) > 1:
        print("¡Es un empate entre los caballos:", ", ".join(map(str, winners)) + "!")
    else:
        print(f"¡El caballo {winners[0]} ha ganado!")

race()

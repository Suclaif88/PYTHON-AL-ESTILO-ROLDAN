import keyboard
import time

def press_key(key, duration, interval):
    end_time = time.time() + duration
    while time.time() < end_time:
        keyboard.press(key)
        time.sleep(interval)
        keyboard.release(key)

key_to_press = "r"  # Tecla a presionar
duration = 10     # Duración en segundos
interval = 0.0001 # Intervalo en segundos

press_key(key_to_press, duration, interval)
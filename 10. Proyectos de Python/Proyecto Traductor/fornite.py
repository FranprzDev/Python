import keyboard
import time

# Este es el contador que se usa, solamente hay que incrementarlo hasta el número deseado.
i=0
# Esto es para que te de tiempo para abrir el chat de la pesrona que quieras molestar xd
time.sleep(2)

while i in range(2):
    keyboard.write('Hola.') # Escribir toda una oración
    keyboard.press_and_release('t') # Escribir tecla por tecla
    keyboard.press_and_release('enter')
    time.sleep(0.1) # 0.1 segundos de espera, se puede reducir pero con una PC mala puede explotar.
    i+=1 # Si no está esto, el while es infinito, igual que while True:
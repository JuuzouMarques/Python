import pyautogui as auto
from time import sleep

print('Iniciando...')
sleep(10)
while True:
    auto.write('Oi meu bem!')
    auto.press('enter')
    sleep(0.2)
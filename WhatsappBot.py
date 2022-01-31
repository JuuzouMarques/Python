import pyautogui as auto
from time import sleep

print('\033[1;32m-' * 20)
print('WHATTSAPP BOT')
print('-\033[m' * 20)
msg = int(input('Digite a quantidade de mensagens você deseja enviar: '))
sleep(10)
auto.write('T^o fazendo uns teste aqui. Vou te enviar mais {} mensagens'.format(msg))
auto.press('enter')
for c in range(msg):
    auto.write('Oi meu bem!')
    auto.press('enter')
    sleep(0.2)
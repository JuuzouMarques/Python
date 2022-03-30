from tkinter import *
from time import sleep
import pyautogui as auto
from threading import Thread

wppColorW = '#ece5dd'
wppColorG = '#25d366'
red = '#ff6961'
stop = False

def verificaCampoVazio():
    global stop
    mensagem = message.get()
    if mensagem == '':
        warning['text'] = 'Campo Vazio!'
    else:
        stop = False
        message['state'] = 'readonly'
        Thread(target=enviarMensagens).start()

def enviarMensagens():
    global stop
    mensagem = message.get()
    sleep(5)
    while stop == False:
        auto.write(mensagem)
        auto.press('Enter')
        sleep(0.5)

def cancelarEnvio():
    global stop
    message['state'] = 'normal'
    if stop == False: stop = True

janela = Tk()
janela.title('Whatsapp Bot')
janela.iconphoto(False, PhotoImage(file='whatsapp_14158.ico'))
janela.configure(background=wppColorW)
janela.resizable(width=FALSE, height=FALSE)

label = Label(janela, text='Mensagem a ser enviada:', justify=CENTER, font=('Arial 10 bold'), bg=wppColorW)
label.grid(row=0, column=0, padx=10, pady=10)
message = Entry(janela, width=50, justify=CENTER)
message.grid(row=1, column=0, padx=10)
warning = Label(janela, text='', justify=CENTER, font=('Arial 10 bold'), bg=wppColorW)
warning.grid(row=2, column=0, padx=10, pady=10)


bttEnviar = Button(text='Enviar', anchor=CENTER, font=('Arial 10 bold'), command=verificaCampoVazio, bg=wppColorG)
bttEnviar.grid(row=3, column=0, padx=10)
bttCancelar = Button(text='Cancelar', anchor=CENTER, font=('Arial 10 bold'), command=cancelarEnvio, bg=red)
bttCancelar.grid(row=4, column=0, padx=10, pady=10)

janela.mainloop()
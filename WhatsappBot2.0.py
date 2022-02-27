from tkinter import *
from time import sleep
import pyautogui as auto

wppColorW = '#ece5dd'
wppColorG = '#25d366'
stop = False

def verificaCampoVazio():
    global stop
    mensagem = message.get()
    if mensagem == '':
        warning['text'] = 'Campo Vazio!'
    else:
        stop = False
        enviarMensagens()

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
    if stop == False: stop = True

janela = Tk()
janela.title('Whatsapp Bot')
janela.configure(background=wppColorW)
janela.resizable(width=FALSE, height=FALSE)

label = Label(janela, text='Mensagem a ser enviada:', justify=CENTER, font=('Arial 10 bold'), bg=wppColorW)
label.grid(row=0, column=0, padx=10, pady=10)
message = Entry(janela, width=50, justify=CENTER)
message.grid(row=1, column=0, padx=10)
warning = Label(janela, text='', justify=CENTER, font=('Arial 10 bold'), bg=wppColorW)
warning.grid(row=2, column=0, padx=10, pady=10)


bttEnviar = Button(text='Enviar', anchor=CENTER, font=('Arial 10 bold'), command=verificaCampoVazio)
bttEnviar.grid(row=3, column=0, padx=10)
bttCancelar = Button(text='Cancelar', anchor=CENTER, font=('Arial 10 bold'), command=cancelarEnvio)
bttCancelar.grid(row=4, column=0, padx=10, pady=10)

janela.mainloop()
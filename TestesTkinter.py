from tkinter import *
from random import randint
import pyperclip as pc

def verificaCampos():
    if bMaiuscula.get() == False and bMinuscula.get() == False and bNumero.get() == False and bEspecial.get() == False:
        senha['text'] = 'Selecione ao menos uma opção'
        bttCopiar['state'] = DISABLED
    else:
        bttCopiar['state'] = NORMAL
        gerarSenha()

def gerarSenha():
    sSenha = ''
    sMin = 'abcdefghijklmnopqrstuvwxyz'
    sMai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sNum = '0123456789'
    sEsp = '!@#$%&'
    sFinal = ''
    if bMaiuscula.get() == True: sSenha += sMai
    if bMinuscula.get() == True: sSenha += sMin
    if bNumero.get() == True: sSenha += sNum
    if bEspecial.get() == True: sSenha += sEsp

    Tam = int(nTamSenha.get())
    for i in range(Tam):
        pos = randint(0, (len(sSenha) - 1))
        sFinal += sSenha[pos]
    
    senha['text'] = (sFinal)

def copiar():
    pc.copy(senha['text'])

janela = Tk()

bMaiuscula = BooleanVar()
bMinuscula = BooleanVar()
bNumero = BooleanVar()
bEspecial = BooleanVar()
nTamSenha = DoubleVar()

janela.title('Gerador de Senhas')
titulo = Label(janela, text='-'*30 + '\nGERADOR DE SENHAS\n' + '-'*30)
titulo.grid(row=0, column=0, padx=20)

labelTamanhoSenha = Label(janela, text='Tamanho da Senha:')
labelTamanhoSenha.grid(row=1, column=0)
slider = Scale(janela, from_=1, to=30, orient=HORIZONTAL, variable=nTamSenha)
slider.grid(row=2, column=0)
optMaiuscula = Checkbutton(janela, text='Letras Maiúsculas', variable=bMaiuscula, onvalue=True, offvalue=False)
optMaiuscula.grid(row=3, column=0)
optMinuscula = Checkbutton(janela, text='Letras Minúsculas', variable=bMinuscula, onvalue=True, offvalue=False)
optMinuscula.grid(row=4, column=0)
optNumeros = Checkbutton(janela, text='Números', variable=bNumero, onvalue=True, offvalue=False)
optNumeros.grid(row=5, column=0)
optEspecial = Checkbutton(janela, text='Caracteres Especiais', variable=bEspecial, onvalue=True, offvalue=False)
optEspecial.grid(row=6, column=0)

button = Button(janela, text='Gerar Senha', command=verificaCampos)
button.grid(row=7, column=0, pady=10)
labelSenha = Label(janela, text='Senha Gerada:')
labelSenha.grid(row=9, column=0)
senha = Label(janela, text='')
senha.grid(row=10, column=0)
bttCopiar = Button(janela, text='Copiar Senha', command=copiar, state=DISABLED)
bttCopiar.grid(row=11, column=0, pady=10)

janela.mainloop()
from fileinput import close
from tkinter import *
from random import randint

def gerarSenha():
    sSenha = ""
    sMin = 'abcdefghijklmnopqrstuvwxyz'
    sMai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sNum = '0123456789'
    sEsp = '!@#$%&'
    sFim = ''

    nTamSenha = int(input('Digite o tamanho desejado para sua senha: '))
    q = input('Deseja letras minúsculas em sua senha? [S/N] \n')
    if q == 'S':
        sSenha += sMin
        q = ''
    q = input('Deseja letras maiúsculas em sua senha? [S/N] \n')
    if q == 'S':
        sSenha += sMai
        q = ''
    q = input('Deseja números em sua senha? [S/N] \n')
    if q == 'S':
        sSenha += sNum
        q = ''
    q = input('Deseja símbolos em sua senha? [S/N] \n')
    if q == 'S':
        sSenha += sEsp
        q = ''
    for i in range(nTamSenha):
        pos = randint(0, len(sSenha))
        sFim += sSenha[pos]

    print(f'Sua senha final é: {sFim}')

def gerarSenha2():
    sSenha = ''
    sMin = 'abcdefghijklmnopqrstuvwxyz'
    sMai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sNum = '0123456789'
    sEsp = '!@#$%&'
    sFinal = ''
    if bMaiuscula.get() == True:
        sSenha += sMai
    if bMinuscula.get() == True:
        sSenha += sMin
    if bNumero.get() == True:
        sSenha += sNum
    if bEspecial.get() == True:
        sSenha += sEsp

    for i in range(8):
        pos = randint(0, len(sSenha))
        sFinal += sSenha[pos]
    
    senha['text'] = sFinal
    print(bMaiuscula.get())


janela = Tk()

bMaiuscula = BooleanVar()
bMinuscula = BooleanVar()
bNumero = BooleanVar()
bEspecial = BooleanVar()

janela.title('Gerador de Senhas')
titulo = Label(janela, text='-'*30 + '\nGERADOR DE SENHAS\n' + '-'*30)
titulo.grid(row=0, column=0, padx=20)
optMaiuscula = Checkbutton(janela, text='Letras Maiúsculas', variable=bMaiuscula, onvalue=True, offvalue=False)
optMinuscula = Checkbutton(janela, text='Letras Minúsculas', variable=bMinuscula, onvalue=True, offvalue=False)
optNumeros = Checkbutton(janela, text='Números', variable=bNumero, onvalue=True, offvalue=False)
optEspecial = Checkbutton(janela, text='Caracteres Especiais', variable=bEspecial, onvalue=True, offvalue=False)

optMaiuscula.grid(row=1, column=0)
optMinuscula.grid(row=2, column=0)
optNumeros.grid(row=3, column=0)
optEspecial.grid(row=4, column=0)
button = Button(janela, text='Gerar Senha', command=gerarSenha2)
button.grid(row=5, column=0)
senha = Label(janela, text='')
senha.grid(row=6, column=0)
janela.mainloop()
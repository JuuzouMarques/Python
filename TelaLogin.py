from tkinter import *
from tkinter import Tk
from tkinter import messagebox

dados = ['juuzou', '1234']
# Cores:
co0 = "#f0f3f5"  # Preto
co1 = "#feffff"  # Branco
co2 = "#3fb5a3"  # Verde
co3 = "#38576b"  # Valor
co4 = "#403d3d"   # Letra

def verificaSenha():
    nome = e_usuario.get()
    senha = e_pass.get()

    if nome == dados[0] and senha == dados[1]:
        messagebox.showinfo('Login Efetuado', 'Login efetuado com sucesso')

        for widget in frame_baixo.winfo_children():
            widget.destroy()
        novaJanela()

    else:
        messagebox.showerror('Erro de login', 'Usuário ou senha incorretos')

def novaJanela():
    l_nome['text'] = 'Bem vindo, Juuzou!'

# Crio a janela
janela = Tk()
janela.title('Login')
janela.geometry('310x300')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

# Divide a janela
frame_cima = Frame(janela, width=310, height=50, bg=co1, relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
frame_baixo = Frame(janela, width=310, height=250, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Configura o frame superior
l_nome = Label(frame_cima, text='LOGIN', anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
l_nome.place(x=5, y=5)
l_linha = Label(frame_cima, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
l_linha.place(x=10, y=45)

# Configura o frame inferior
l_usuario = Label(frame_baixo, text='Usuário *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_usuario.place(x=10, y=20)
e_usuario = Entry(frame_baixo, width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid')
e_usuario.place(x=14, y=50)

l_pass = Label(frame_baixo, text='Senha *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_pass.place(x=10, y=100)
e_pass = Entry(frame_baixo, width=25, justify='left', show='*', font=('', 15), highlightthickness=1, relief='solid')
e_pass.place(x=14, y=130)

b_pass = Button(frame_baixo, text='Entrar', width=40, height=2, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE, command=verificaSenha)
b_pass.place(x=15, y=180)


janela.mainloop()

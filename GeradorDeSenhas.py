from random import randint

sSenha = ""
sMin = 'abcdefghijklmnopqrstuvwxyz'
sMai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sNum = '0123456789'
sEsp = '!@#$%&'
sFim = ''

print('-'*20)
print('GERADOR DE SENHAS')
print('-'*20)

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

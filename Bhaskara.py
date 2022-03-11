def calcularRaizes(): # Calcula e imprime as raízes da função
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)
    print('''RAÍZES DA FUNÇÃO:
    X1: {:.2f}
    x2: {:.2f}
    '''.format(x1, x2))

# Aqui o usuário vai entrar com os valores da função
print('FUNÇÃO DO SEGUNDO GRAU: a X² + b X + c')
a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))
print('FUNÇÃO INFORMADA: {} X² {} X + {}\n'.format(a, b, c))

# Achando o delta da função
delta = (b ** 2) - 4 * a * c
if delta > 0:
    print('Delta positivo! DUAS RAÍZES REAIS E DISTINTAS!')
    calcularRaizes()
elif delta == 0:
    print('Delta igual a zero! DUAS RAÍZES REAIS E IGUAIS!')
    calcularRaizes()
else:
    print('Delta negativo! SEM RAÍZES REAIS!\n')

# Pontos de Máximo e mínimo
xVertice = (-b) / (2 * a)
yVertice = (-delta) / (4 * a)
print('''PONTO DE {}
X do vértice: {:.2f}
Y do vértice: {:.2f}
'''.format('MÍNIMO' if a > 0 else 'MÁXIMA', xVertice, yVertice))

# Concavidade da função
print('''CONCAVIDADE DA FUNÇÃO:
Função concava para {}'''.format('cima' if a > 0 else 'baixo'))

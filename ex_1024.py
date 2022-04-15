n_teste = int(input())

linhas = []

for i in range(n_teste):
    linhas.append([x for x in input()])

saida = []

tam = len(linhas)

# primeira passada - deslocar 3 caracteres a direita
for i in range(tam):
    linhas[i] = [chr(ord(x)+3) if (ord(x) in range(65, 91)) or (ord(x) in range(97, 123))
                     else x for x in linhas[i]]

    '''
    for j in range(len(linhas[i])):
        # caracteres de 65-90 e 97-122
        if (ord(linhas[i][j]) in range(65, 91)) or (ord(linhas[i][j]) in range(97, 123)):
          linhas[i][j] = chr(ord(linhas[i][j]) + 3)
    '''

# segunda passada - inverter a linha
for i in linhas:
    i.reverse()

# terceira passada - todos caracteres, da metade em diante, deslocar 1 caractere a esquerda
for i in range(tam):
    for j in range(len(linhas[i]) // 2, len(linhas[i])):
        linhas[i][j] = chr(ord(linhas[i][j]) - 1)

# imprimir elementos da list como uma string
for i in linhas:
    print(''.join(str(x) for x in i))
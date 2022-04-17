t_instancias = int(input())

saida = []

# executa t instancias
for i in range(t_instancias):
    n_conjuntos = int(input())
    conjuntos = []

    # armazena elementos dos n conjuntos
    for j in range(n_conjuntos):
        conjuntos.append(set([int(x) for x in input().split()[1:]]))

    # q operacoes
    q_operacoes = int(input())

    # executa as q operacoes
    for k in range(q_operacoes):
        operacao = [int(x) for x in input().split()]
        if operacao[0] == 1:
            saida.append(len(conjuntos[operacao[1] - 1] & conjuntos[operacao[2] - 1]))
        else:
            saida.append(len(conjuntos[operacao[1] - 1] | conjuntos[operacao[2] - 1]))

for item in saida:
    print(item)


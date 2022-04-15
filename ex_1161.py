def fatorial(valor):
    resultado = 1
    for i in range(1, valor):
        resultado *= i+1

    return resultado

lista = []
while(True):
    try:
        m, n = [int(x) for x in input().split()]
        lista.append(fatorial(m) + fatorial(n))
    except EOFError:
        for item in lista:
            print(item)
        break
while True:
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    #print(x1, y1, x2, y2)
    # se a entrada for 0 0 0 0, o programa deve encerrar
    if (x1 + y1 + x2 + y2) == 0:
        break
    else:
        # posição destino == posicao atual
        if x2 == x1 and y2 == y1:
            print(0)

        # a posição de destino está na diagonal,
        # porque os valores de x e y aumentam proporcionalmente
        # ou, elemento está na mesma linha ou coluna
        elif abs(x2 - x1) == abs(y2 - y1) or (x1 == x2 or y2 == y1):
            print(1)

        # o máximo de movimentos necessários são 2 para alcançar qualquer casa pela dama
        else:
            print(2)

def minutos_ate_0(h, m):
    return 60 - m + (23 - h)*60


def minutos_apos_0(h, m):
    return m + h*60


while True:
    try:
        h1, m1, h2, m2 = [int(x) for x in input().split()]
        # criterio de parada
        if h1 == m1 == h2 == m2 == 0:
            break

        # no mesmo dia dia
        if h1 == h2 and m1 < m2:
            minutos1 = minutos_ate_0(h1, m1)
            minutos2 = minutos_ate_0(h2, m2)
            print(minutos1 - minutos2)

        # mesmo horario
        elif h1 == h2 and m1 == m2:
            print(0)

        elif h2 <= h1:
            # caso o periodo termine no dia seguinte deve-se somar os tempos
            # de ate meia noite e apos meia noite
            minutos1 = minutos_ate_0(h1, m1)
            minutos2 = minutos_apos_0(h2, m2)
            print(minutos1 + minutos2)

        # caso o periodo esteja dentro do mesmo dia eh calculado a diferenca
        # dos horarios ate meia noite
        else:
            minutos1 = minutos_ate_0(h1, m1)
            minutos2 = minutos_ate_0(h2, m2)

            print(minutos1 - minutos2)

    except EOFError:
        break

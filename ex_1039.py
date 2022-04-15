import math

def contem(lista):
    # distancia entre centros
    d = math.sqrt((lista[1] - lista[4])**2 + (lista[2] - lista[5])**2)
    # se o raio do circulo menor + a distance entre centros
    # for menor que o raio do maior, então o circulo está dentro do outro
    return (d + lista[3]) <= lista[0]

entrada = []
while(True):
    try:
        # R1 X1 Y1 R2 X2 Y2
        if contem([int(x) for x in input().split()]):
            print('RICO')
        else:
            print('MORTO')
    except EOFError:
        break
def switch(x):
    return {
        0:6,
        1:2,
        2:5,
        3:5,
        4:4,
        5:5,
        6:6,
        7:3,
        8:7,
        9:6}.get(x)

def num_leds(entra):
    leds = 0

    for i in entra:
        leds += switch(int(i))
    return leds


saida = []

# casos de teste
n = int(input())

for i in range(n):
    saida.append(num_leds(list(input())))

for i in saida:
    print(i, "leds")
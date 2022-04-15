n = int(input())
lista = []

# ler entrada
for i in range(n):
    lista.append(int(input()))

for i in range(n):
    if(lista[i] == 0):
        print("NULL")
    elif (lista[i] % 2) == 0:
        if lista[i] < 0:
            print("EVEN NEGATIVE")
        else:
            print("EVEN POSITIVE")
    else:
        if lista[i] < 0:
            print("ODD NEGATIVE")
        else:
            print("ODD POSITIVE")
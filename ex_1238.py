casos_teste = int(input())

for n in range(casos_teste):
    string1, string2 = input().split()
    palavra_final = []
    contador = 0
    for i, j in zip(string1, string2):
        palavra_final.append(i)
        palavra_final.append(j)
        contador += 1

    if (len(string1) > len(string2)):
        palavra_final.append(string1[contador:])

    if (len(string2) > len(string1)):
        palavra_final.append(string2[contador:])

    print("".join(palavra_final))
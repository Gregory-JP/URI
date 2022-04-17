casos_teste = int(input())

for i in range(casos_teste):
    sentenca_codificada = input()
    deslocamento = int(input())
    for j in sentenca_codificada:
        a = ord(j)
        if a - deslocamento < 65:
            #tmp = a - 64
            #print(chr(90 - (deslocamento - tmp)), end='')
            print(chr((a - deslocamento) + 26), end='')
        else:
            print(chr(a - deslocamento), end='')
    print()

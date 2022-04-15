while True:
    valor = float(input())
    cont = 0

    print("NOTAS:")

    while ((valor - 100.00) >= 0):
        valor -= 100.00
        cont += 1

    print("{} nota(s) de R$ 100.00".format(cont))

    cont = 0
    while ((valor - 50.00) >= 0):
        valor -= 50.00
        cont += 1

    print("{} nota(s) de R$ 50.00".format(cont))

    cont = 0
    while ((valor - 20.00) >= 0):
        valor -= 20.00
        cont += 1

    print("{} nota(s) de R$ 20.00".format(cont))

    cont = 0
    while ((valor - 10.00) >= 0):
        valor -= 10.00
        cont += 1

    print("{} nota(s) de R$ 10.00".format(cont))

    cont = 0
    while ((valor - 5.00) >= 0):
        valor -= 5.00
        cont += 1
    print("{} nota(s) de R$ 5.00".format(cont))

    cont = 0
    while ((valor - 2.00) >= 0):
        valor -= 2.00
        cont += 1
    print("{} nota(s) de R$ 2.00".format(cont))

    """ Moedas """
    print("MOEDAS:")
    cont = 0
    while ((valor - 1.00) >= 0):
        valor -= 1.00
        cont += 1
    print("{} moeda(s) de R$ 1.00".format(cont))

    cont = 0
    while ((valor - 0.50) >= 0):
        valor -= 0.50
        cont += 1
    print("{} moeda(s) de R$ 0.50".format(cont))

    cont = 0
    while ((valor - 0.25) >= 0):
        valor -= 0.25
        cont += 1
    print("{} moeda(s) de R$ 0.25".format(cont))

    cont = 0
    while ((valor - 0.10) >= 0):
        valor -= 0.10
        cont += 1
    print("{} moeda(s) de R$ 0.10".format(cont))

    cont = 0
    while ((valor - 0.05) >= 0):
        valor -= 0.05
        cont += 1
    print("{} moeda(s) de R$ 0.05".format(cont))

    cont = 0
    while (round((valor - 0.01),2) >= 0):
        valor -= 0.01
        cont += 1
    print("{} moeda(s) de R$ 0.01".format(cont))
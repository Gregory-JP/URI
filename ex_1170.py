n_testes = int(input())

for i in range(n_testes):
    qtd_comida = float(input())
    j = 0
    while(qtd_comida > 1):
        qtd_comida /= 2
        j += 1
    print('{} dias'.format(j))
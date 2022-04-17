# Kadane's algorithm (Algorithm 3: Dynamic Programming)
def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

while True:
    try:
        numero_dias = int(input())
        custo_por_dia = int(input())
        receita_por_dia = []

        # criado lista com o lucro diário (descontado custo)
        for i in range(numero_dias):
            receita_por_dia.append(int(input()) - custo_por_dia)

        # maximum subarray problem
        res = max_subarray(receita_por_dia)
        if res <= 0:
            print(0)
        else:
            print(res)

        '''
        # método por força bruta
        maximo = 0
        cont = 0
        for i in receita_por_dia:
            soma = 0
            receita_por_dia_aux = receita_por_dia[cont:]

            for j in receita_por_dia_aux:
                soma += j
                if soma >= maximo:
                    maximo = soma

            cont += 1

        print(maximo)
        '''
    except EOFError:
        break


casos_teste = int(input())

for i in range(casos_teste):

    # cria lista com apenas < e >
    entrada = [x for x in input() if x != '.']

    acabou = False

    # análise deve começar do indice 1
    i = 1
    diamantes = 0

    # lista deve ter pelo menos dois caracteres para ser avaliado
    if len(entrada) > 1:

        # enquanto não analisou tudo, não sai do loop
        while acabou is not True:

            # analisa se no indice i possui >
            if entrada[i] == '>':
                j = i - 1

                # verifica se o anterior é um > para fechar o diamante
                if entrada[j] == '<':
                    # remover diamante da lista
                    entrada.pop(i)
                    entrada.pop(j)

                    # mover variável de indice para uma posição atrás
                    # já que foi removido caracteres da lista
                    i -= 2
                    diamantes += 1

            # mover indice para próximo caractere
            i += 1

            # caso indice seja <= 0 ele deve começar de novo do valor 1
            if i <= 0:
                i = 1

            # caso de teste termina quando o indice a ser analisado não está na lista
            if i >= len(entrada):
                acabou = True

    print(diamantes)
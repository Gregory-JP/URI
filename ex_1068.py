while True:
    try:
        pilha = []
        for i in input():
            if i == '(':
                pilha.append(i)
            if i == ')':
                if not pilha:
                    pilha.append('algo')
                    break
                pilha.pop()
        if len(pilha) == 0:
            #print('correct', 'tamanho:', len(pilha))
            print('correct')
        else:
            #print('incorrect', 'tamanho:', len(pilha))
            print('incorrect')
    except EOFError:
        break
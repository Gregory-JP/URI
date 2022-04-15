while(True):
    try:
        hashmat, oponent = [int(x) for x in input().split()]
        print(abs(hashmat-oponent))
    except EOFError:
        break
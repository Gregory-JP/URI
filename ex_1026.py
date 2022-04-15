while True:
    try:
        a, b = [int(x) for x in input().split()]

        print(a ^ b)

    except EOFError:
        break
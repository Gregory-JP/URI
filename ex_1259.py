import bisect

n = int(input())

pares = []
impares = []
for i in range(n):
    num = int(input())
    if num % 2 == 0:
        bisect.insort(pares, num)
    else:
        bisect.insort(impares, num)

for i in pares:
    print(i)

for i in range(-1, -len(impares) - 1, -1):
    print(impares[i])

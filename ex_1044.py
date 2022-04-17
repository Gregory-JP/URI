a, b = input().split()

a = int(a)
b = int(b)

numbers = [a, b]
numbers.sort()

if numbers[1] % numbers[0] == 0:
    print ("Sao Multiplos")
else:
    print("Nao sao Multiplos")
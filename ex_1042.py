entrada = input().split()

# convert list elements to int type
entrada = [int(x) for x in entrada]

# create a copy of the list
ordenado = entrada[:]

# sort the new list
ordenado.sort()

# print the sorted list
for item in ordenado:
    print(item)

print()

# print the input
for item in entrada:
    print(item)
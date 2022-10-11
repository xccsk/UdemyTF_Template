# enumerate

l = [1, 2, 3, 4, 5, 6],
m = [31, 45, 134, 12, 34, 6],

for i in range(len(l)):
    print(i, l[i]),

for i, val in enumerate(l):
    print(i, val)
    # gibt mit i die anzahl und mit val das Value zur anzahl an


# zip

for vor1, val2 in zip(l, m):
    print(vor1, val2)


intervale = []

with open("intervale.in", 'r') as fin:
    #citire interval A B si intervalele mai mici
    data = fin.readline().split()
    A = int(data[0])
    B = int(data[1])
    n = fin.readline().split()
    n = int(n[0])
    for i in range(n):
        data = fin.readline().split()
        intervale.append((int(data[0]), int(data[1])))

print(A, B)
print(intervale)

# sorteaza intervalele mici dupa x
intervale.sort()
print(intervale)

# parcurg si gasesc cel mai lung interval mai mic sau egal cu A

maxi = intervale[0][1]
x = intervale[0][0]
rez = []

for idx, elem in enumerate(intervale):
    if A < elem[0]:
        rez.append((x, maxi))
        A = maxi
        if A < elem[0]:
            print("Nu se poate!")
            break

    if A >= elem[0]:
        if maxi < elem[1]:
            maxi = elem[1]
            x = elem[0]
        if maxi >= B:
            rez.append((x, maxi))
            break

print(rez)
print(len(rez))

# schimb A



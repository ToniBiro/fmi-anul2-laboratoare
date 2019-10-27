
data = []

with open("arbore.in", 'r') as fin:
    n = fin.readline().split()
    m = int(n[1])
    n = int(n[0])
    for i in range(m):
        a = fin.readline().split()
        print(a)
        data.append((int(a[0]), int(a[1])))

ls_adiacenta = {}

for elem in data:
    if elem[0] in ls_adiacenta.keys():
        ls_adiacenta[elem[0]].append(elem[1])
    else:
        ls_adiacenta[elem[0]] = [elem[1]]

rez = []
print(ls_adiacenta)
print(type(ls_adiacenta[1]))


def df(x, add):
    add[x] = 1
    if x in ls_adiacenta.keys():
        for elem in ls_adiacenta[x]:
            print(f"elem:{elem}")
            df(elem, add)
            if add[elem] == 1:
                add[x] = 0
    if add[x] == 1:
        rez.append(x)


add = [0] * (n+1)

df(1, add)

print(f"rez: {rez}")
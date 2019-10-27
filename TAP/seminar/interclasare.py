v1 = []
v2 = []

with open("vectori.in", 'r') as fin:
    data = next(fin).split()
    for elem in data:
        v1.append(int(elem))
    data = next(fin).split()
    for elem in data:
        v2.append(int(elem))

v1.sort()
v2.sort()
print(v1)
print(v2)


def mediana(v1, v2):
    if len(v1) == 1:
        return (v1[0] + v2[0])/2
    if len(v1) == 2:
        v1 = v1 + v2
        v1.sort()
        return (v1[1] + v1[2])/2
    if len(v1) % 2 == 0:
        mij1 = len(v1)//2
        mij2 = len(v2)//2
        if (v1[mij1] + v1[mij1+1])/2 == (v2[mij2]+v2[mij2+1])/2:
            return (v1[mij1] + v1[mij1+1])/2
        if v1[mij1] > v2[mij2]:
            return mediana(v1[0:mij1+1], v2[mij2-1:-1])
        if v1[mij1] < v2[mij2]:
            return mediana(v1[mij1-1:-1], v2[0:mij2+1])
    else:
        mij1 = len(v1) // 2
        mij2 = len(v2) // 2
        if v1[mij1] == v2[mij2]:
            return v1[mij1]
        if v1[mij1] > v2[mij2]:
            return mediana(v1[0:mij1+1], v2[mij2-1:-1])
        if v1[mij1] < v2[mij2]:
            return mediana(v1[mij1-1:-1], v2[0:mij2+1])


print(mediana(v1, v2))
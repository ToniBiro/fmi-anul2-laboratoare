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


def mediana(vect1, vect2):
    print(vect1, vect2)
    if len(vect1) == 1:
        return (vect1[0] + vect2[0]) / 2
    if len(vect1) == 2:
        vect1 = vect1 + vect2
        vect1.sort()
        return (vect1[1] + vect1[2]) / 2
    if len(vect1) % 2 == 0:
        mij1 = len(vect1) // 2 - 1
        mij2 = len(vect2) // 2 - 1
        if (vect1[mij1] + vect1[mij1 + 1])/2 == (vect2[mij2] + vect2[mij2 + 1])/2:
            return (vect1[mij1] + vect1[mij1 + 1]) / 2
        if vect1[mij1] > vect2[mij2]:
            return mediana(vect1[0:mij1 + 2], vect2[mij2:])
        if vect1[mij1] < vect2[mij2]:
            return mediana(vect1[mij1:], vect2[0:mij2 + 2])
    else:
        mij1 = len(vect1) // 2 - 1
        mij2 = len(vect2) // 2 - 1
        if vect1[mij1] == vect2[mij2]:
            return vect1[mij1]

        if vect1[mij1] > vect2[mij2]:
            return mediana(vect1[0:mij1 + 1], vect2[mij2:])
        if vect1[mij1] < vect2[mij2]:
            return mediana(vect1[mij1:], vect2[0:mij2 + 1])


print(mediana(v1, v2))

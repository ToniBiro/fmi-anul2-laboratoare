# mediana a doi vectori dati sortati cu lungime egala

v1 = []
v2 = []

with open("vectori.in", 'r') as fin:
    data = next(fin).split()
    for elem in data:
        v1.append(int(elem))
    data = next(fin).split()
    for elem in data:
        v2.append(int(elem))

print(v1)
print(v2)


def mediana(vect1, vect2):
    l = len(vect1)
    print(l)
    print(vect1, vect2)
    if l == 1:
        return (vect1[0] + vect2[0]) / 2
    if l == 2:
        vect = vect1 + vect2
        vect.sort()
        return (vect[1] + vect[2]) / 2
    if l % 2 == 1:

        mij1 = vect1[l // 2]
        mij2 = vect2[l // 2]
    else:
        mij1 = (vect1[l // 2 - 1] + vect1[l // 2]) / 2
        mij2 = (vect2[l // 2 - 1] + vect2[l // 2]) / 2

    if mij1 == mij2:
        return mij1
    if mij1 > mij2:
        return mediana(vect1[0:l // 2 + 1], vect2[(l - 1) // 2:l])
    else:
        return mediana(vect1[(l - 1) // 2:l], vect2[0: l // 2 + 1])


print(f"raspuns:{mediana(v1, v2)}")

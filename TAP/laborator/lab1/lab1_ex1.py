
data = list()
with open('lab1_ex1.in', 'r') as fin:
    n = fin.readline()
    n = int(n)
    aux = fin.readline().split()
    for elem in aux:
        data.append(int(elem))
data.sort()


def sum_2(vect, k):
    i = 0
    j = len(vect)-1
    rez = []
    while i < j:
        if vect[i] + vect[j] < k:
            i = i + 1
        else:
            if vect[i] + vect[j] > k:
                j = j - 1
            else:
                if vect[i] + vect[j] == k:
                    rez.append((vect[i], vect[j]))
                    i = i+1
                    j = j-1
    return rez

print(data)

rezultate = set()

for idx, elem in enumerate(data):
    lista_perechi = sum_2(data[idx+1:], -elem)
    for pereche in lista_perechi:
        rezultate.add((elem, pereche[0], pereche[1]))

print(rezultate)

# partition pe mediana

v = []

with open("ponderi.in", 'r') as fin:
    data = next(fin).split()
    datap = next(fin).split()

for i in range(len(data)):
    v.append([float(datap[i]), int(data[i])])

print(v)

def partition(vect):
    pivot = vect[0][1]
    stanga  = list(filter(lambda x: x[1] < pivot, vect))
    dreapta = list(filter(lambda x: x[1] > pivot, vect))
    return stanga + [vect[0]] + dreapta, len(stanga)


def med_p(v, s, f):
    if s == f:
        return v[s][1]
    if f-s == 1:
        if v[s][0] == v[f][0]:
            return (v[s][1] + v[f][1])//2
        if v[s][0] > v[f][0]:
            return v[s][1]
        else:
            return v[f][1]

    v, mij = partition(v)
    print(v)
    sum_s, sum_f = sum([elem[0] for elem in v[s:mij]]), sum([elem[0] for elem in v[mij+1:f]])

    if sum_s < 1/2 and sum_f <= 1/2:
        return v[mij][1]
    if sum_s > sum_f:
        v[mij][0] += sum_f
        return med_p(v, s, mij)
    if sum_f > sum_s:
        v[mij][0] += sum_s
        return med_p(v, mij, f)


print(med_p(v, 0, len(v)))
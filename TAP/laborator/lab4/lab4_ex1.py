# inversiuni
# inversiuni semnificative
# trebuie modificat ->

with open("vector.in", 'r') as fin:
    data = next(fin).split()

v = []
for elem in data:
    v.append(int(elem))
for idx in range(len(v)//2, len(v)):
    v[idx] = 2*v[idx]

print(v)


def inv(st, dr):
    if st == dr:
        return 0
    s = []
    m = (st + dr)//2
    nrs = inv(st, m)
    nrd = inv(m + 1, dr)
    vs = v[st:m+1]
    vd = v[m+1:dr+1]
    nrm = 0
    i, j = 0, 0
    while i < len(vs) and j < len(vd):
        if vs[i] < 2 * vd[j]:
            nrm_s += j
            i += 1
        else:
            s.append(vd[j])
            j += 1
    while i < len(vs):
        nrm_s += j
        i += 1

    while i < len(vs) and j < len(vd):
        if vs[i] < vd[j]:
            s.append(vs[i])
            nrm += j
            i += 1
        else:
            s.append(vd[j])
            j += 1
    while i < len(vs):
        s.append(vs[i])
        nrm += j
        i += 1
    while j < len(vd):
        s.append(vd[j])
        j += 1

    v[st:dr+1] = s
    return nrs + nrd + nrm


print(inv(0, len(v)-1))

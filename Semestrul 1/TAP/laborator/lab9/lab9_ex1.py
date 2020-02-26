
p = []
with open("joculet.in", 'r') as fin:
    n = next(fin).split()
    n = int(n[0])
    data = next(fin).split()

for elem in data:
    p.append(int(elem))

D = []
for i in range(n):
    D.append([0]*n)


def completare(i, j):
    if i == j:
        D[i][j] = p[i]
        return D[i][j]
    if j - i == 1:

        D[i][j] = max(p[i], p[i+1])
        return D[i][j]

    D[i][j] = max(p[i] + min(completare(i+2, j), completare(i+1, j-1)), p[j] + min(completare(i+1, j-1), completare(i, j-2)))
    return D[i][j]

# momorare piese luate
rez = completare(0, n-1)

with open("joculet.out", 'w')as fout:
    print(rez - (sum(p) - rez), file=fout)

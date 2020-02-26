
with open("cladire.in", 'r') as fin:
    n = next(fin).split()
    m = int(n[1])
    n = int(n[0])

d = []

for i in range(n):
    d.append([0]*m)

d[0][0] = 0

for i in range(1, m):
    d[0][i] = 1

for i in range(1, n):
    d[i][0] = 1

for i in range(1, n):
    for j in range(1, m):
        d[i][j] = d[i-1][j] + d[i][j-1]


with open("cladire.out", 'w')as fout:
    print(d[n-1][m-1]%9901, file=fout)
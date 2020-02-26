
v = []
with open("robo.in", 'r') as fin:
    n = next(fin).split()
    m = int(n[1])
    sfinal = int(n[2])
    n = int(n[0])
    for i in range(n):
        data = next(fin).split()
        aux = []
        for elem in data:
            aux.append(int(elem))
        v.append(aux)

print(v)


D = []
S = []

for i in range(n):
    D.append([0] * m)
    S.append([0] * m)

suma = 0
for i in range(m-1, -1, -1):
    suma += v[0][i]
    D[0][i] = suma
    S[0][i] = sfinal-D[0][i]

suma = 0
for i in range(n):
    suma += v[i][m-1]
    D[i][m-1] = suma
    S[i][m-1] = sfinal-D[i][m-1]

for i in range(1, n):
    for j in range(m-2, -1, -1):
        D[i][j] = max(D[i-1][j], D[i][j+1]) + v[i][j]
        S[i][j] = sfinal-D[i][j]

for i in range(n):
    print(D[i])
print()
for i in range(n):
    print(S[i])

print(f"rez: smin= {S[n-1][0]}")



################################################3

def afm(matrix):
    for line in matrix:
        print(line)
    print()


v = []
copie = []
with open('date.in', 'r') as fin:
    a = next(fin).split()
    n = int(a[0])
    m = int(a[1])
    sfinal = int(a[2])
    for i in range(n):
        a = next(fin).split()
        v.append([int(_) for _ in a])
        copie.append([int(_) for _ in a])

v[n-1][0] -= sfinal

prev = [[''] * m for _ in range(n)]
prev[n-1][0] = 'jos'

for j in range(1, m):
    if v[n-1][j] >= 0:
        v[n-1][j] += v[n-1][j-1]
    else:
        v[n-1][j] += min(v[n-1][j-1], 0)
    prev[n-1][j] = 'st'

for i in range(n - 2, -1, -1):
    if v[i][0] >= 0:
        v[i][0] += v[i+1][0]
    else:
        v[i][0] += min(v[i+1][0], 0)
    prev[i][0] = 'jos'


for i in range(n - 2, -1, -1):
    for j in range(1, m):
        if v[i][j - 1] > v[i + 1][j]:
            theChosenOne = v[i][j - 1]
            prev[i][j] = 'st'
        else:
            theChosenOne = v[i + 1][j]
            prev[i][j] = 'jos'

        if v[i][j] >= 0:
            v[i][j] += theChosenOne
        else:
            v[i][j] += min(theChosenOne, 0)

afm(v)
afm(prev)

print(-v[0][n - 1] + 1)
print()
y, x = 0, n-1
while y <= n - 1 and x >= 0:
    print(copie[y][x], end=' ')
    if prev[y][x] == 'st':
        x -= 1
    else:
        y += 1

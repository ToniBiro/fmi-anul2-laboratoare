
with open("edist.in", 'r') as fin:
    data = next(fin).split()
    c1, c2, c3 = int(data[0]), int(data[1]), int(data[2])
    a = next(fin).split()
    b = next(fin).split()

a = a[0]
b = b[0]
n, m = len(a)+1, len(b)+1

M = [[0 for j in range(m)] for i in range(n)]
P = [[0 for j in range(m)] for i in range(n)]

for i in range(m):
    M[0][i] = i*c2

P[0] = [j for j in range(m)]


for i in range(1, n):
    M[i][0] = i*c1
    P[i][0] = i
    for j in range(1, m):
        if a[i-1] == b[j-1]:
            sub_cost = 0
        else:
            sub_cost = c3

        M[i][j] = min(M[i][j-1] + c1, M[i-1][j] + c2, M[i-1][j-1] + sub_cost)
        if M[i][j] == M[i][j-1] + c1:
            P[i][j] = 1 + P[i][j-1]
        else:
            if M[i][j] == M[i-1][j] + c2:
                P[i][j] = 1 + P[i-1][j]
            else:
                if sub_cost == 0:
                    P[i][j] = P[i-1][j-1]
                else:
                    P[i][j] = 1 + P[i-1][j-1]


with open("edist.out", "w") as fout:
    print(P[n-1][m-1]+1, file=fout)
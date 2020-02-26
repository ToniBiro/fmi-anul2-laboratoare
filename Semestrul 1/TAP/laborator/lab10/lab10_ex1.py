# n numere intregi (v)
# k, l apartin N a i n >= k*l
# Sa se alega din vectorul v
# k secvente (pozitii consecutive) de lungime l a. i. suma sa fie maxima
#
N = []
M = []
S = []
with open("intrare.in", 'r') as fin:
    k = next(fin).split()
    l = int(k[1])
    k = int(k[0])
    data = next(fin).split()

v = []
for i in data:
    v.append(int(i))

print(k, l, v)

s = 0
for elem in v:
    S.append(elem + s)
    s += elem


def calc(i, w):
    for i in range(w*l):
        M[i] = 0
    M[w*l] = S[w*l] - S[w*l-l]
    M[i] = max(S[i] - S[i-l], M[i-1])

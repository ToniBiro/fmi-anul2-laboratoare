from math import sqrt
INF = 1000
puncte = []

with open("puncte.in", 'r') as fin:
    n = int(next(fin).split()[0])
    for i in range(n):
        puncte.append([int(elem) for elem in next(fin).split()])

X = [elem[0] for elem in puncte]
Y = [elem[1] for elem in puncte]

X.sort()
Y.sort()

print(X, Y)


def dist(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)


def min_dist(vect, s, f):
    if s >= f:
        return INF
    if f-s == 1:
        return dist(vect[s][0], vect[s][1], vect[f][0], vect[f][1])

    mij = (s + f+1)//2
    print(f"mij:{mij}")
    d_s = min_dist(vect, s, mij-1)
    d_d = min_dist(vect, mij+1, f)
    print(d_s, d_d)

    if d_s < d_d:
        d, D = d_s, d_d
    else:
        d, D = d_d, d_s
    print(d)

    x_sort = [elem for elem in vect[s:f+1] if abs(elem[0] - vect[mij][0]) <= d]
    print(x_sort)


min_dist(puncte, 0, len(puncte)-1)
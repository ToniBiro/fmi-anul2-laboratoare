from math import sqrt
INF = 1000000000
puncte = []

with open("cmap.in", 'r') as fin:
    n = int(next(fin).split()[0])
    for i in range(n):
        puncte.append([int(elem) for elem in next(fin).split()])

X = [elem[0] for elem in puncte]
Y = [elem[1] for elem in puncte]
X.sort()
Y.sort()


def dist(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)


def min_dist(vect, s, f, Y):
    if s >= f:
        return INF
    if f-s == 1:
        return dist(vect[s][0], vect[s][1], vect[f][0], vect[f][1])

    mij = (s + f)//2
    m =X[mij][0]


    d_s = min_dist(vect, s, mij-1, YS)
    d_d = min_dist(vect, mij+1, f),YD

    d = min(d_s, d_d)

    y_sort = [elem for elem in Y[s:f+1] if abs(elem[0] - vect[mij][0]) < d]
    y_sort.sort(key=lambda elem: elem[1], reverse=False)

    for idx, elem in enumerate(y_sort):
        for i in range(1, len(y_sort)-idx):
            index = (idx+i)
            d = min(dist(elem[0], elem[1], y_sort[index][0], y_sort[index][1]), d)

    return d

with open("cmap.out", 'w') as fout:
    print(min_dist(puncte, 0, len(puncte)-1), file=fout)


#print(f"distanta minima rezultata = {min_dist(puncte, 0, len(puncte)-1)}")
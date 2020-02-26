from math import sqrt
INF = 1000000000
puncte = []

with open("cmap.in", 'r') as fin:
    n = int(next(fin).split()[0])
    for i in range(n):
        puncte.append([int(elem) for elem in next(fin).split()])

X = puncte.copy()
Y = puncte.copy()
X.sort()
Y.sort(key = lambda elem: elem[1], reverse=False)
print(Y)


def dist(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)


def min_dist(vect, s, f, Y_):
    if s >= f:
        return INF
    if f-s == 1:
        return dist(vect[s][0], vect[s][1], vect[f][0], vect[f][1])

    mij = (s + f)//2
    m = X[mij][0]

    YS = [elem for elem in Y_ if elem[0] <= m]
    YD = [elem for elem in Y_ if elem[0] > m]
    print(f"mij: {mij}   len(YS) {len(YS)} len(YD) {len(YD)}")
    d_s = min_dist(vect, s, mij-1, YS)
    d_d = min_dist(vect, mij+1, f, YD)

    d = min(d_s, d_d)
    print(f"d:{d}")

    y_sort = [elem for elem in Y_ if m + d >= elem[0] and m - d <= elem[0]]
    print(y_sort)

    for idx, elem in enumerate(y_sort):
        for i in range(1, 8):
            if idx+i < len(y_sort):
                d = min(dist(elem[0], elem[1], y_sort[idx+i][0], y_sort[idx+i][1]), d)

    return d


with open("cmap.out", 'w') as fout:
    print(min_dist(puncte, 0, len(puncte)-1, Y), file=fout)


#print(f"distanta minima rezultata = {min_dist(puncte, 0, len(puncte)-1)}")
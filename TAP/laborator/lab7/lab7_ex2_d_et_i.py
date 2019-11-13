vect = []
with open("munte.in", 'r') as fin:
    n = next(fin).split()
    n = int(n[0])
    data = next(fin).split()
    for i in range(n):
        vect.append(int(data[i]))

print(vect)


def maxim(vect, s, f):
    if s >= f:
        return vect[s]
    if f - s == 1:
        return max(vect[s], vect[f])
    mij = (s + f)//2
    max_s = maxim(vect, s, mij)
    max_l = maxim(vect, mij+1, f)

    return max(max_s, max_l)


print(maxim(vect, 0, len(vect)-1))
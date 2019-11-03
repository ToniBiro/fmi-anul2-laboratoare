
A = []

with open('intrare.in', 'r') as fin:    #citirea punctelor
    for idx, line in enumerate(fin):
        data = line.split()
        A.append((float(data[0]), float(data[1]), idx))

print(A)

# x1 = A[0][0]  y1 = A[0][1]
# x2 = A[1][0]  y2 = A[1][1]

# x3 = A[2][0]  y3 = A[2][1]
# x4 = A[3][0]  y4 = A[3][1]

for idx, elem in enumerate(A):
    print(f"A{idx+1} = {elem}")


a = A[1][1] - A[0][1]          # determinam ecuatia celor doua drepte
b = A[0][0] - A[1][0]
seg1 = (a, b, a*A[0][0] + b*A[0][1])

a = A[3][1] - A[2][1]
b = A[2][0] - A[3][0]
seg2 = (a, b, a*A[2][0] + b*A[2][1])

print(seg1, seg2)

# a1 = seg1[0]  b1 = seg1[1]  c1 = seg1[2]
# a2 = seg2[0]  b2 = seg2[1]  c2 = seg2[2]

det = seg1[0]*seg2[1] - seg2[0]*seg1[1]   # calculam determinantul
if det < 0:
    det = -det
print(det)


def slope(x1, y1, x2, y2):
    if x2-x1 == 0:
        return 0
    return float((y2 - y1) / (x2 - x1))


if det != 0:
    x = ((-seg1[2]) * seg2[1] - (-seg2[2] * seg1[1])) / det    # calculam punctele de intersectie a celor doua drepte
    y = (seg1[0] * (-seg2[2]) - seg2[0] * (-seg1[2])) / det
    print(x, y)

    if max(A[0][0], A[1][0]) >= x >= min(A[0][0], A[1][0]) and max(A[2][0], A[3][0]) >= x >= min(A[2][0], A[3][0]):   # cazul in care avem intersectie de segmente
        if max(A[0][1], A[1][1]) <= y <= min(A[0][1], A[1][1]) and max(A[2][1], A[3][1]) <= y <= min(A[2][1], A[3][1]):
            print(f"[A1, A2] si [A3, A4] se intersecteaza in punctul {x}, {y}")
    else:
        print("Cele 2 segmente nu se intersecteaza!")

if det == 0:
    if slope(A[0][0], A[0][1], A[1][0], A[1][1]) == slope(A[2][0], A[2][1], A[3][0], A[3][1]):
        if A[0][0]*seg2[0] + A[0][1]*seg2[1] == seg2[2]:
            print("Sunt paralele si se afla pe aceasi dreapta!")
            A.sort()
            if (A[0][2] == 0 and A[1][2] != 1 or A[0][2] == 1 and A[1][2] != 0) or (A[0][2] == 2 and A[1][2] != 3 or A[0][2] == 3 and A[1][2] != 2):
                print("Cele doua segmente se intersecteaza!")
            else:
                print("Cele doua segmente nu se intersecteaza!")
        else:
            print("Sunt paralele si nu se afla pe aceeasi dreapta!")
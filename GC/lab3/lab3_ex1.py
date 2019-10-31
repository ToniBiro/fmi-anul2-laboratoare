
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

seg1 = (A[1][0]-A[0][1], A[0][0]-[1][0], A[1][0]*A[0][1] - A[0][0]*A[1][1])
seg2 = (A[3][0]-A[2][1], A[2][0]-[3][0], A[3][0]*A[2][1] - A[2][0]*A[3][1])

print(seg1, seg2)

# a1 = seg1[0]  b1 = seg1[1]  c1 = seg1[2]
# a2 = seg2[0]  b2 = seg2[1]  c2 = seg2[2]

det = seg1[0]*seg2[1] - seg2[0]*seg1[1]
print(det)

if det != 0:

    x = ((-seg1[2]) * seg2[1] - (-seg2[2] * seg1[1])) / det
    y = (seg1[0] * (-seg2[2]) - seg2[0] * (-seg1[2])) / det
    print(x, y)

    if max(A[0][0], A[1][0]) >= x >= min(A[0][0], A[1][0]) and max(A[2][0], A[3][0]) >= x >= min(A[2][0], A[3][0]):
        if max(A[0][1], A[1][1]) <= y <= min(A[0][1], A[1][1]) and max(A[2][1], A[3][1]) <= y <= min(A[2][1], A[3][1]):
            print(f"[A1, A2] si [A3, A4] se intersecteaza in punctul {x}, {y}")

#https://stackoverflow.com/questions/20677795/how-do-i-compute-the-intersection-point-of-two-lines
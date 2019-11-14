# Fie 4 puncte, oricare 3 sunt necoliniare
# a) Sa se verifice daca patrulaterul A1A2A3A4 (in ordinea asta) este convex
# b) in caz afirmativ sa se precizeze pozitia punctului A4 fata de cercul circumscris
# ( A4 este pe cerc ddaca suma unghiului lui A4 cu unghiul A2 este = cu pi altfel daca suma e mai mare decat pi)

import math

A = []
with open('patrulater.in', 'r') as fin:    #citirea punctelor
    for idx, line in enumerate(fin):
        data = line.split()
        A.append((float(data[0]), float(data[1]), idx))


print(A)

# x1 = A[0][0]  y1 = A[0][1]
# x2 = A[1][0]  y2 = A[1][1]

# x3 = A[2][0]  y3 = A[2][1]
# x4 = A[3][0]  y4 = A[3][1]


def slope(x1, y1, x2, y2):
    if x2-x1 == 0:
        return 0
    return float((y2 - y1) / (x2 - x1))


panta1 = slope(A[0][0], A[0][1], A[2][0], A[2][1])
seg1 = (panta1, -1, A[0][1] - panta1*A[0][0])

panta2 = slope(A[1][0], A[1][1], A[3][0], A[3][1])
seg2 = (panta2, -1, A[1][1] - panta2*A[1][0])

print(seg1, seg2)


def get_det(seg_a, seg_b):
    return seg_a[0] * seg_b[1] - seg_b[0] * seg_a[1]  # calculam determinantul


def test_de_orientare(x1, y1, x2, y2, x, y):
    """
    :param A: primul capat al segmentului
    :param B: al doilea capat al segmentului
    :param P: punctul pentru care verificam orientarea fata de segmentul AB
    :return: daca ce returnam < 0 sau > 0 este pe o parte sau alta a segmentului, daca = 0 este pe segment
    """
    return (x - x1) * (y2 - x2) - (y - y1) * (x2 - x1)



def patrulater_convex(seg1, seg2, det):
    if det == 0:
        return False
    if det != 0:
        x = ((-seg1[2]) * seg2[1] - (-seg2[2] * seg1[1])) / det  # calculam punctele de intersectie a celor doua drepte
        y = (seg1[0] * (-seg2[2]) - seg2[0] * (-seg1[2])) / det
        print(f"puncte:{x}, {y}")
    if test_de_orientare(A[0][0], A[0][1], A[1][0], A[1][1], x, y) ==
        test_de_orientare(A[1][0], A[1][1], A[2][0], A[2][1], x, y) ==
        test_de_orientare(A[2][0], A[2][1] A[3][0], A[3][1], x, y) ==
        test_de_orientare(A[3][0], A[3][1], A[0][0], A[0][1], x, y):



def get_vector_puncte(x1, y1, x2, y2):
    return x1-x2, y1-y2


def prod_scalar(a, b, c, d):
    return a * c + d * b


a, b = get_vector_puncte(A[1][0], A[1][1], A[0][0], A[0][1])
c, d = get_vector_puncte(A[1][0], A[1][1], A[2][0], A[2][1])
cos_A2 = prod_scalar(a, b, c, d) / (math.sqrt(prod_scalar(a, b, a, b)) * math.sqrt(prod_scalar(c, d, c, d)))

a, b = get_vector_puncte(A[3][0], A[3][1], A[0][0], A[0][1])
c, d = get_vector_puncte(A[3][0], A[3][1], A[2][0], A[2][1])
cos_A4 = prod_scalar(a, b, c, d) / (math.sqrt(prod_scalar(a, b, a, b)) * math.sqrt(prod_scalar(c, d, c, d)))

unghi_A2 = math.acos(cos_A2)
unghi_A4 = math.acos(cos_A4)

if patrulater_convex(seg1, seg2, get_det(seg1, seg2)):
    print("da")
    if unghi_A2 + unghi_A4 == math.pi:
        print("A4 se afla pe cerc")

    if unghi_A2 + unghi_A4 > math.pi:
        print("A4 se afla in interiorul cercului")
else:
    print("NU")
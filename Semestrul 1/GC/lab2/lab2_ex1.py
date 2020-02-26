
# Sunt date 4 pct in R^2 - sa se determine 2 multimi I J - intersectia sa fie nula si reuniunea sa contina toate punctele
# Conv(A1, A2, A3, A4)
# poate fi un patrulater
# poate fi un triunghi
# poate fi u segment (cand sunt coliniare punctele)

A = []

with open('puncte.in', 'r') as fin:    #citirea punctelor
    for idx, line in enumerate(fin):
        data = line.split()
        A.append((float(data[0]), float(data[1])))


def coliniar(A, B, C):
    """
    :param A: primul punct
    :param B: al doilea punct
    :param C: al treilea punct
    :return: returneaza aria triunghiului format de cele 3 puncte - daca e 0 => coliniaritate
    """
    a = A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1])
    return a


def get_raport(A, B, C):
    """
    :param A: primul punct
    :param B: al doilea punct
    :param C: al treilea punct
    :return: returneaza raportul a, daca sunt coliniare atunci este adevarat ca: C = (1-a)*A + a*B
    """
    if B[0] - A[0] != 0:
        return (C[0] - A[0]) / (B[0] - A[0])
    else:
        return (C[1] - A[1]) / (B[1] - A[1])


def test_de_orientare(A, B, P):
    """
    :param A: primul capat al segmentului
    :param B: al doilea capat al segmentului
    :param P: punctul pentru care verificam orientarea fata de segmentul AB
    :return: daca ce returnam < 0 sau > 0 este pe o parte sau alta a segmentului, daca = 0 este pe segment
    """
    return (P[0] - A[0]) * (B[1] - A[1]) - (P[1] - A[1]) * (B[0] - A[0])


def area(A, B, C):
    return 0.5 * ( (B[0]*C[1] - C[0]*B[1]) - (A[0]*C[1] - C[0]*A[1]) + (A[0]*B[1] - B[0]*A[1]))


patru = False
for idx, elem in enumerate(A):
    print(f"A{idx+1} = {elem}")

if area(A[0], A[1], A[2]) == 0 and area(A[1], A[2], A[3]) == 0:   #verificam coliniaritatea celor 4 puncte
    A.sort()
    print("Dupa sortare:")
    for idx, elem in enumerate(A):
        print(f"A{idx + 1} = {elem}")
    print("Cele 4 puncte sunt coliniare")
    print("I = {A1, A4}  J = {A2, A3}")

ar1 = abs(area(A[0], A[1], A[2]))
ar2 = abs(area(A[1], A[2], A[3]))
ar3 = abs(area(A[0], A[2], A[3]))
ar4 = abs(area(A[0], A[1], A[3]))

ar_max = max(ar1, ar2, ar3, ar4)

if ar_max != 0:
    if ar1 == ar_max:
        if ar2 + ar3 + ar4 == ar_max:
            print("triunghi  I = {A1, A2, A3}  J = {A4}")
        else:
            patru = True
    elif ar2 == ar_max:
        if ar1 + ar3 + ar4 == ar_max:
            print("triunghi I = {A2, A3, A4}  J = {A1}")
        else:
            patru = True
    elif ar3 == ar_max:
        if ar1 + ar2 + ar4 == ar_max:
            print("triunghi I = {A0, A2, A3}  J = {A1}")
        else:
            patru = True
    else:
        if ar1 + ar2 + ar3 == ar_max:
            print("triunghi  I = {A0, A1, A3}  J = {A2}")
        else:
            patru = True

if patru:
    A.sort()
    print("Dupa sortare:")
    for idx, elem in enumerate(A):
        print(f"A{idx + 1} = {elem}")
    if (test_de_orientare(A[0], A[2], A[1]) < 0) == (test_de_orientare(A[0], A[2], A[3]) > 0):
        print("patrulater  I = {A1, A3}  J = {A2, A4}")
    else:
        print("patrulater  I = {A1, A4}  J = {A2, A3}")
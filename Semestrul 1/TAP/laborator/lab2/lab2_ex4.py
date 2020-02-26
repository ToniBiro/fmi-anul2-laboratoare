from random import randint

with open('z.in', 'r') as fin:
    n = int(next(fin))
    data = [int(elem) for elem in fin.readline().split()]

print(data)

sum_par, sum_impar = 0, 0

for idx, elem in enumerate(data):
    if idx % 2 == 0:
        sum_par += elem
    else:
        sum_impar += elem

j_1 = []
j_2 = []
i, j = 0, n-1

if sum_impar > sum_par:
    while i <= j:
        if i % 2 != 0:
            j_1.append(i)
            i += 1
            if randint(0, 1) == 0:
                j_2.append(i)
                i += 1
            else:
                j_2.append(j)
                j -= 1
        else:
            j_1.append(j)
            j -= 1
            if randint(0, 1) == 0:
                j_2.append(i)
                i += 1
            else:
                j_2.append(j)
                j -= 1
else:
    while i <= j:
        if i % 2 == 0:
            j_1.append(i)
            i += 1
            if randint(0, 1) == 0:
                j_2.append(i)
                i += 1
            else:
                j_2.append(j)
                j -= 1
        else:
            j_1.append(j)
            j -= 1
            if randint(0, 1) == 0:
                j_2.append(i)
                i += 1
            else:
                j_2.append(j)
                j -= 1

print(j_1, j_2)
s_1, s_2 = 0, 0
for idx in range(n//2):
    s_1 += data[j_1[idx]]
    s_2 += data[j_2[idx]]

print(s_1, s_2)
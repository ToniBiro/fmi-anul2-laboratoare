# n cuburi
# h[i] - inaltimea max care are la baza cubul i
# nr[i] - nr de turnuri care se pot forma care au la baza cubul i

cub = []
with open("cuburi.in", "r") as fin:
    n = next(fin).split()
    col = int(n[1])
    n = int(n[0])
    for i in range(n):
        data = next(fin).split()
        cub.append([int(data[0]), int(data[1])])

nr = [1] * n
cub.sort(reverse=True)
h = [elem[0] for elem in cub]

for i in range(n - 1, -1, -1):
    print(cub[i])
    for j in range(i, n):
        if cub[i][1] != cub[j][1]:
            if h[j] + cub[i][0] > h[i]:
                h[i] = h[j] + cub[i][0]
    for j in range(i, n):
        if h[i] == h[j] + cub[i][0] and cub[i][1] != cub[j][1]:
            nr[i] += nr[j]

nr_max = sum([nr[idx] for idx, elem in enumerate(h) if elem == max(h)])

print(cub)
print(h)
print(nr)
print(max(h))
print(nr_max)

# n cuburi
sir =[]
with open("cuburi.in", "r") as fin:
    n = next(fin).split()
    col = int(n[1])
    n = int(n[0])
    for i in range(n):
        data = next(fin).split()
        sir.append([int(data[0]), int(data[1])])

sir.sort()
print(sir)
h = [elem[0] for elem in sir]
for i in range(len(h)):
    h[i] = [h[i], n, i]

for i in range(n-1, -1, -1):
    for j in range(i, n):
        if sir[j][0] != sir[i][0] and sir[j][1] != sir[i][1]:
            if h[j][0] + sir[i][0] > h[i][0]:
                h[i][0] = h[j][0] + sir[i][0]
                h[i][1] = j

m = max(h)
print(m)



def rez(ind):
    if ind >= n:
        return
    print(ind)
    return rez(h[ind][1])

rez(m[2])



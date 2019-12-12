import heapq

with open("ghiozdan.in", 'r') as fin:
    G = next(fin).split()
    G = int(G[0])

    data1 = next(fin).split()
    data2 = next(fin).split()

c = []
g = []
for elem in data1:
    c.append(float(elem))
for elem in data2:
    g.append(float(elem))
cu = []

for i in range(len(c)):
    cu.append(c[i]/g[i])

items = []
for i in range(len(c)):
    items.append((cu[i], c[i], g[i]))

items.sort(reverse=True)


def calc(nod, ld, ln, G_curent, cf, cd):
    for i in range(len(g)):
        if items[i] not in ln and items[i] not in ld:
            G_curent += items[i][2]
            cd += items[i][1]
            cf += items[i][1]
            if G_curent > G:
                cd -= items[i][1]
                cf -= items[i][1]
                cf += (items[i][2] - (G_curent - G)) * items[i][0]
                break
            if G_curent == G:
                break
    return ()

ld = [0]
ln = []

calc(ld, ln, 0, 0, 0)


list_ = [(cf, cd, 0, ld, ln)]
heapq.heapify(list_)

print(heapq.heappop(list_))

while list_:
    now = heapq.heappop(list_)
    for i in range(0, 2):

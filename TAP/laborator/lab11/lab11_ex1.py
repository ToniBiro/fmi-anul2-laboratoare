from heapq import heapify, heappop, heappush

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


class Item:
    def __init__(self, cost, wt, cu, idx):
        self.cost = cost
        self.wt = wt
        self.cu = cu
        self.idx = idx

    def __lt__(self, other):
        return self.cu < other.cu


items = []
index = 0
for a, b, c in zip(c, g, cu):
    items.append(Item(a, b, c, index))
    index += 1

items.sort(reverse=True)

for elem in items:
    print(elem.cu, elem.wt)


def greedy(in_items, out_items):
    current_wt = 0
    current_cost = 0
    rez_frac = 0
    rez_disc = 0
    for i in in_items:
        current_wt += items[i].wt
        current_cost += items[i].cost

    if current_wt > G:
        return -1, -1

    for elem in items:
        if elem.idx in in_items or elem.idx in out_items:
            continue

        if current_wt + elem.wt <= G:
            current_wt += elem.wt
            current_cost += elem.cost

            rez_frac = current_cost
            rez_disc = current_cost
        else:
            frac_wt = G - current_wt
            cost_frac_wt = frac_wt * elem.cu
            rez_frac = current_cost + cost_frac_wt

    return rez_frac, rez_disc


class Node:
    def __init__(self, level, in_item, out_item):
        self.level = level
        self.in_item = in_item
        self.out_item = out_item
        self.cf, self.cd = greedy(in_item, out_item)

    def __lt__(self, other):
        return self.cf > other.cf


def tree():
    init_node = Node(0, [], [])

    L = [init_node]
    heapify(L)
    best_disc = init_node.cd
    best_frac = init_node.cf

    print(f"BEST FRACTIONAR: {best_frac}")

    while L:
        current_node = heappop(L)
        print(f"level: {current_node.level}, in_items: {current_node.in_item}, out_items: {current_node.out_item}")
        current_item = current_node.level

        if current_node.cf < best_disc:
            continue

        if current_node.cd > best_disc:
            best_disc = current_node.cd

        if current_node.cd == best_frac:
            return current_node.cd

        if current_item+1 == len(items):
            continue

        current_item += 1

        yes_node = Node(current_item, current_node.in_item + [current_item], current_node.out_item)
        no_node = Node(current_item, current_node.in_item, current_node.out_item + [current_item])

        print(f"yes node--->   in_items: {yes_node.in_item}, out_items: {yes_node.out_item}")
        print(f"no node--->   in_items: {no_node.in_item}, out_items: {no_node.out_item}")

        heappush(L, yes_node)
        heappush(L, no_node)

    return best_disc


rez = tree()
print(rez)

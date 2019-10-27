# problema siruri descrescatoare

import heapq

with open('sir_descrescator.in', 'r') as fin:
    n = int(next(fin))
    data = [int(elem) for elem in fin.readline().split()]

print(data)
rez = []
capete = []

print(len(capete))


def cautare_binara(numar):
    if len(capete) == 0:
        capete.append(numar)
        rez.append([numar])
        return -1
    if numar > capete[len(capete)-1]:
        capete.append(numar)
        rez.append([numar])
        return -1
    i = 0
    j = len(capete)-1
    while i < j:
        med = i + ((j-i)//2)
        if numar > capete[med]:
            i = med + 1
        if numar < capete[med]:
            j = med
    return i


for elem in data:
    idx = cautare_binara(elem)
    if idx != -1:
        rez[idx].append(elem)
        capete[idx] = elem

print(capete)
print(rez)
aux = []
for idx, elem in enumerate(capete):
    aux.append((elem, idx))

heapq.heapify(aux)
print(list(aux))

sortat = []

while aux:
    curent = heapq.heappop(aux)
    print(f"aux: {aux}")
    print(f"curent: {curent}")
    sortat.append(curent[0])
    rez[curent[1]].pop()
    if rez[curent[1]]:
        heapq.heappush(aux, (rez[curent[1]][-1], curent[1]))


print(sortat)
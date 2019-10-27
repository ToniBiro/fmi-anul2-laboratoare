#sortare descrescator dupa profit
#activitatea de la pasul i se i-a cel mai tarziu posibil

data = []

with open("intrare1.in", 'r') as fin:
    n = fin.readline().split()
    n = int(n[0])
    datap = fin.readline().split()
    datat = fin.readline().split()
    for i in range(n):
        data.append((int(datap[i]), int(datat[i]), i+1))

a = [None]*n
print(a)

data.sort(reverse=True)
print(data)

for elem in data:
    for i in reversed(range(elem[1])):
        if a[i] == None:
            a[i] = elem[0]
            break

print(a)


# ----- mai eficient folosind union and find


print(f"Data: {data}")


dads = []
aux = []
h = [0]*(n+1)
rez = [None] * n

for i in range(n+1):
    dads.append(i)

aux = [elem - 1 for elem in dads]

print(dads)


def find_father(a):
    if dads[a] == a:
        return a
    else:
        return find_father(dads[a])


def union(a, b):
    dad_a = find_father(a)
    dad_b = find_father(b)

    if h[dad_a] == h[dad_b]:
        dads[dad_a] = dad_b
        h[dad_b] += 1
        aux[dad_b] = min(aux[dad_a], aux[dad_b])

    if h[dad_a] > h[dad_b]:
        dads[dad_b] = dad_a
        aux[dad_a] = min(aux[dad_a], aux[dad_b])

    if h[dad_a] < h[dad_b]:
        dads[dad_a] = dad_b
        aux[dad_b] = min(aux[dad_a], aux[dad_b])

sum = 0

for elem in data:
    tata = find_father(elem[1])
    if aux[tata] > -1:
        rez[aux[tata]] = elem[2]
        sum += elem[0]
        union(tata, aux[tata])
print(rez)
print(sum)

# + varianta 1 prob 3 lab 2  -  mai eficient prin cautare binara

# la seminar
#cautare binara in sirul meu ordonat descrescator - cea mai mica valoare din sir care e mai mare decat elementul meu curent
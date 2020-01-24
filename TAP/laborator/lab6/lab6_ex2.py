# problema cu perechi de litere

with open("sir_cuv.in", 'r') as fin:
    n = next(fin).split()
    n = int(n[0])
    data = next(fin).split()

print(data)

dict_ = {}

for elem in data:
    dict_[elem[0]] = [1, n]

print(dict_)

h = [1]*n

for i in range(n-1, -1, -1):
    for j in range(i, n):
        if dict(data[i][1])[0] + 1 > h[j]:
            dict(data[i][1])[0] = dict(data[i][1])[0]+1
            dict(data[i][1])[1] = j

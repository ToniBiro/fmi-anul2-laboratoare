
with open('taskuri.in', 'r') as fin:
    n = int(next(fin))
    cuv = [int(elem) for elem in fin.readline().split()]
    f = [int(elem) for elem in fin.readline().split()]

data =[]
for i in range(n):
    data.append((cuv[i]/f[i], f[i], cuv[i]))

data.sort()
print(data)

#timp total de acces

t_a = 0
s = 0
for elem in data:
    s += elem[2]
    t_a += s*elem[1]

print(t_a)
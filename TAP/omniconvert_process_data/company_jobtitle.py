
data = []
with open("intrare.in", 'r') as fin:
    n = next(fin).split()
    n = int(n[0])
    for elem in range(n):
        cuv = next(fin).split("\n")
        data.append(cuv[0])

print(data)
rez = ""
for elem in data:
    rez += elem + " OR "

print(rez)

with open("iesire.out", "w") as fout:
    print(rez, file = fout)
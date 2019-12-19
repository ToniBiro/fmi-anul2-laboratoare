# ni se dau n cuvinte , L = lungimea liniei pe care se vor pune cuvintele
# minimizam suma din L-O[i] unde O[i] = cat s-a completat din linia i

data = []
with open("cuvinte.in", "r") as fin:
    n = next(fin).split()
    L = int(n[1])
    n = int(n[0])
    data = next(fin).split()

lungimi = []
for elem in data:
    lungimi.append(int(elem))

D = []
sl = []

for i in range(len(lungimi)):
    for j in range(len(lungimi)):


    sl.append()

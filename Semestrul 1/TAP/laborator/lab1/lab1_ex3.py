

## de refacut cu dictionare - O(n)

import math

f1 = open('doc1.in', 'r')
f2 = open('doc2.in', 'r')

data1 = f1.read().split()
data2 = f2.read().split()

for idx, elem in enumerate(data1):
    data1[idx] = elem.strip(' ,.\n')
for idx, elem in enumerate(data2):
    data2[idx] = elem.strip(' ,.\n')

data = data1 + data2

cuvinte = set(data)
if '' in cuvinte:
    cuvinte.remove('')
print(cuvinte)

aparitii = []
for cuv in cuvinte:
    aparitii.append((data1.count(cuv), data2.count(cuv)))

print(aparitii)

f1.close()
f2.close()


def cos_dist(perechi):
    sum1 = 0
    v1 = 0
    v2 = 0
    for pereche in perechi:
        sum1 = sum1 + pereche[0]*pereche[1]
        v1 = v1 + pereche[0]*pereche[0]
        v2 = v2 + pereche[1]*pereche[1]
    v1 = math.sqrt(v1)
    v2 = math.sqrt(v2)

    return sum1/(v1*v2)


print(cos_dist(aparitii))

### mai eficient

dict_ = dict()

with open('doc1.in', 'r') as fin:
    data = fin.readline().split()
    for elem in data:
        clean = elem.strip(' ,.\n')
        if clean not in dict_.keys():
            dict_[clean] = [1, 0]
        else:
            dict_[clean][0] = dict_[clean][0] + 1

with open('doc2.in', 'r') as fin:
    data = fin.readline().split()
    for elem in data:
        if elem.strip(' ,.\n') not in dict_.keys():
            dict_[elem.strip(' ,.\n')] = [0, 1]
        else:
            dict_[elem.strip(' ,.\n')][1] += 1

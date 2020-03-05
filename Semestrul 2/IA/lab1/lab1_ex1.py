# ex 2
string = []

for i in range(ord('a'), ord('z')+1):
    string.append(chr(i))

print(string)

# n = int(input())
n = 20
# ex 3
rez = []
for i in range(1, n+1):
    rez.append((-1)**(i%2+1)*i)

print(rez)

# ex 9

sir = 'abcde'

perm = [sir[i+1:] + sir[0:i+1] for i in range(len(sir))]

print(perm)

# sortari, ex 1

l = [3, 2, 6, 9, 11, 0, 41, 112, 211, 35, 25]

rez = sorted(l, key=lambda x: str(x))

rez1 = sorted(l, key=lambda x: str(x)[::-1])

print(rez1)

# gen matrice


def gen_matrice():
    nr_char = ord('z')-ord('a')+1
    mat = [[0] + [chr(i) for i in range(ord('a'), ord('z')+1)]]


    mat.extend([[ chr(i)] + [0]*nr_char for i in range(ord('a'), ord('z')+1)])


    return mat

mat = gen_matrice()

print(mat[0][1])

cuvinte = ["papagal", "pisica","soarece","bolovan","soparla","catel", "pasare"]


def caut_cuv(mat, cuvinte):

    for cuvant in cuvinte:
        for i in range(len(cuvant)-1):
            # print(mat[ord(cuvant[i])-ord('a')+1][ord(cuvant[i+1])-ord('a')+1])
            mat[ord(cuvant[i])-ord('a') + 1][ord(cuvant[i+1])-ord('a')+1] += 1
    for elem in mat:
        print(elem)

    return mat


mat = caut_cuv(mat, cuvinte)


def elim_mat(mat):
    nr_char = ord('z') - ord('a') + 1

    mat2 = mat[:]
    for idx, elem in enumerate(mat):
        if elem[1:] == [0]*(len(elem)-1):
            mat2.remove(mat[idx])

    mat = mat2

    del_list = []

    for j in range(1, nr_char+1):
        del_list.append(j)
        for i in range(1, len(mat)):
            if mat[i][j] != 0:
                del_list.pop()
                break
    print(del_list)
    del_list.sort(reverse=True)

    for j in del_list:
        for i in range(len(mat)):
            mat[i].pop(j)



    return mat2

mat = elim_mat(mat)

print("dupa eliminare")
for elem in mat:
    print(elem)
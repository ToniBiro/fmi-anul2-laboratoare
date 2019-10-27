# D et I problema cu tabala

interogari = []
with open("z.in", 'r') as fin:
    n = next(fin).split()
    n_inte = int(n[1])
    n = int(n[0])
    for i in range(n_inte):
        data = next(fin).split()
        interogari.append((int(data[0]), int(data[1])))

print(interogari)

t_dim_2 = [[1, 2], [3, 4]]


def tabla(dim, i, j):
    total = dim**2
    if dim == 2:
        return t_dim_2[i-1][j-1]
    if i <= dim//2:
        if j <= dim//2:  #cadran I
            return tabla(dim//2, i, j)
        else:           #cadran II
            j -= dim//2
            return total//4 + tabla(dim//2, i, j)
    else:
        if j <= dim//2:  #cadran III
            i -= dim//2
            return total//2 + tabla(dim//2, i, j)
        else:           #cadran IV
            i -= dim//2
            j -= dim//2
            return 3*total//4 + tabla(dim//2, i, j)

with open("z.out", 'w') as fout:
    for interogare in interogari:
        print(tabla(2**n, interogare[0], interogare[1]), file=fout)

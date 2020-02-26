# retinem D[i] - nr min de cuvinte in care se imparte S[i:n]
# unde n este len(S)


with open("cuv_binar.in", 'r') as fin:
    d = next(fin).split()
    S = next(fin)

D = [-1]*(len(S))
print(S)
print(S[1:4])


def recurenta(poz):
    print(f"poz: {poz}, D: {D}")
    if S[poz:len(S)] in d:
        return 1
    if poz == len(S)-1:
        return 1
    if poz == len(S):
        return 0
    mini = len(S) - poz
    for i in range(poz, len(S)):
        if S[poz:i] in d:
            if D[i] == -1:
                D[i] = recurenta(i)
            if mini > 1 + D[i]:
                mini = 1 + D[i]

    print(f"poz: {poz}, D: {D}")
    return mini

print(D)

print(recurenta(0))

print(D)
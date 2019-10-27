import collections

Puncte = collections.namedtuple('Puncte', 'x y z')
puncte = set()
lista = list()

with open("intrare.in", 'r') as fin:
    for idx, line in enumerate(fin):
        data_str = line.split()
        punct = Puncte(x=int(data_str[0]), y=int(data_str[1]), z=int(data_str[2]))
        lista.append(punct)
        puncte.add(punct)


def get_a(lista_puncte):
    if lista_puncte[1].x - lista_puncte[0].x != 0:
        raport = (lista_puncte[2].x - lista_puncte[0].x) / (lista_puncte[1].x - lista_puncte[0].x)
    else:
        if lista_puncte[1].y - lista_puncte[0].y != 0:
            raport = (lista_puncte[2].y - lista_puncte[0].y) / (lista_puncte[1].y - lista_puncte[0].y)
        else:
            raport = (lista_puncte[2].z - lista_puncte[0].z) / (lista_puncte[1].z - lista_puncte[0].z)
    return raport


def verif_coli(lista_puncte, raport):
    if lista_puncte[2].x - lista_puncte[0].x == raport * (lista_puncte[1].x - lista_puncte[0].x):
        if lista_puncte[2].y - lista_puncte[0].y == raport * (lista_puncte[1].y - lista_puncte[0].y):
            if lista_puncte[2].z - lista_puncte[0].z == raport * (lista_puncte[1].z - lista_puncte[0].z):
                return True
    return False


def cauta_pereche(lista_puncte):
    for idx1, punct1 in enumerate(lista_puncte):
        for idx2, punct2 in enumerate(lista_puncte):
            if punct1 == punct2:
                if idx1 != idx2:
                    return idx1, idx2


if len(puncte) == 3:
    a = get_a(lista)
    if verif_coli(lista, a):
        print('Sunt coliniare!')
        print(f'A3 = {1 - a}*A1 + {a}*A2')
    else:
        print("Nu sunt coliniare!")
else:
    if len(puncte) == 2:
        print('Sunt coliniare!')
        prim, sec = cauta_pereche(lista)
        print(f'A{prim+1} = {1}*A{sec+1} + {0}*A{3-(prim+sec)+1}')
    else:
        print('Reprezinta acelasi punct!')

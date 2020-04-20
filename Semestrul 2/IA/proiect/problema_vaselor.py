""" definirea problemei """

import time
from copy import deepcopy

class Nod:

    def __init__(self, info):
        self.info = info
        self.h = self.euristica_1()

    def __str__(self):
        sir = ''
        for idx, vas in enumerate(self.info):
            sir += str(idx) + ': '
            sir += str(vas) + '\n'

        return f"vase:\n{sir}euristica: {self.h}\n"

    def __repr__(self):
        return f"({self.info}, h={self.h})"

    def euristica_1(self):
        # ne uitam in toate culorile curente si daca nu gasim o culoare scop
        # printre ele atunci crestem rez cu 1 deoarece inseamna ca
        # trebuie sa facem cel putin o combinatie pentru a obtine culoarea cautata
        rez = 0
        culori_curente = [vas[2] for vas in self.info]

        for elem in nod_scop:
            if elem[1] not in culori_curente:
                rez = rez + 1

        return rez

    def euristica_3(self):  # inadmisibila

        rez = 0


        return rez


class Problema:
    def __init__(self, combinatii=None, stare_initiala=None):
        if combinatii:
            self.combinatii = combinatii
        else:
            self.combinatii = [['rosu', 'albastru', 'mov'],
                               ['albastru', 'galben', 'verde'],
                               ['mov', 'verde', 'maro']]

        if stare_initiala:
            self.nod_start = Nod(stare_initiala)
        else:
            self.nod_start = Nod([[5, 4, 'rosu'],
                                  [2, 2, 'galben'],
                                  [3, 0, ''],
                                  [7, 3, 'albastru'],
                                  [1, 0, ''],
                                  [4, 3, 'rosu']])  # de tip Nod

""" Sfarsit definire problema """

""" Clase folosite in algoritmul A* """


class NodParcurgere:
    """O clasa care cuprinde informatiile asociate unui nod din listele open/closed
        Cuprinde o referinta catre nodul in sine (din graf)
        dar are ca proprietati si valorile specifice algoritmului A* (f si g).
        Se presupune ca h este proprietate a nodului din graf
    """

    problema = None  # atribut al clasei

    def __init__(self, nod_graf, parinte=None, g=0, f=None):
        self.nod_graf = nod_graf  # obiect de tip Nod
        self.parinte = parinte  # obiect de tip NodParcurgere
        self.g = g  # costul drumului de la radacina pana la nodul curent
        if f is None:
            self.f = self.g + self.nod_graf.h
        else:
            self.f = f

    def drum_arbore(self):
        """
            Functie care calculeaza drumul asociat unui nod din arborele de cautare.
            Functia merge din parinte in parinte pana ajunge la radacina
        """
        nod_c = self
        drum = [nod_c]
        while nod_c.parinte is not None:
            drum = [nod_c.parinte] + drum
            nod_c = nod_c.parinte
        return drum

    def contine_in_drum(self, nod):
        """
            Functie care verifica daca nodul "nod" se afla in drumul dintre radacina si nodul curent (self).
            Verificarea se face mergand din parinte in parinte pana la radacina
            Se coampara doar informtiile nodurilor (proprietatea info)
            Returnati True sau False.

            "nod" este obiect de tip Nod (are atributul "nod.info")
            "self" este obiect de tip NodParcurgere (are "self.nod_graf.info")
        """
        if in_lista(self.drum_arbore(), nod):
            return True
        else:
            return False

    # se modifica in functie de problema

    def expandeaza(self):
        """Pentru nodul curent (self) parinte, trebuie sa gasiti toti succesorii (fiii)
        si sa returnati o lista e tupluri (nod_fiu, cost_muchie_tata_fiu),
        sau lista vida, daca nu exista niciunul.
        (Fiecare tuplu contine un obiect de tip Nod si un numar.)

        Luam toate combinatiile de perechi de vase si amestecam intre ele culorile
        si adaugam configuratia noua in lista rez[] cu costul 1
        """
        rez = []

        vase_curente = self.nod_graf.info

        for a in range(len(vase_curente)):
            for b in range(len(vase_curente)):
                vase_aux = deepcopy(vase_curente)   # copiez configuratia ca sa o pot modifica de fiecare data
                i = vase_aux[a]
                j = vase_aux[b]
                if i[0] > i[1] and j[1] > 0 and i != j:  # daca am unde turna si am ce turna atunci
                    incape = i[0] - i[1]    # vad cat incape
                    i[1] += min(incape, j[1])
                    j[1] -= min(incape, j[1])   # calculez ce se intampla dupa turnare
                    culoare = ''
                    if i[2] == '':   # setez noua culoare
                        culoare = j[2]
                    else:
                        culoare = 'nedefinit'
                    for combinatie in self.problema.combinatii:
                        if i[2] == combinatie[0] and j[2] == combinatie[1] or i[2] == combinatie[1] and j[2] == combinatie[0]:
                            culoare = combinatie[2]
                            break
                    i[2] = culoare
                    if j[1] == 0:
                        j[2] = ''

                rez.append((Nod(vase_aux), 1))

        return rez

    # se modifica in functie de problema
    def test_scop(self):
        """
        Verific daca in cofiguratia curenta apare nodul scop
        :return: True sau False
        """
        vase_curente = self.nod_graf.info
        perechi_curente = [(vas[1], vas[2]) for vas in vase_curente]

        return set(nod_scop).issubset(set(perechi_curente))

    def __str__(self):

        if self.nod_graf == self.problema.nod_start:
            return f"{self.nod_graf}"

        sir = ''
        vase = [0, 0]
        nod_curent = self.nod_graf.info
        parinte = self.parinte if self.parinte is None else self.parinte.nod_graf.info
        if self.parinte:
            for idx, vas in enumerate(self.parinte.nod_graf.info):
                if vas != nod_curent[idx]:
                    if vas[1] < nod_curent[idx][1]:
                        vase[1] = [nod_curent[idx][1]-vas[1], idx]
                    if vas[1] > nod_curent[idx][1]:
                        vase[0] = [vas[1] - nod_curent[idx][1], idx, vas[2]]

        sir += f"Din vasul {vase[0][1]} s-au turnat {vase[0][0]} litri de apa de culoare {vase[0][2]} in vasul {vase[1][1]}"
        return f"{sir}\n{self.nod_graf}"


""" Algoritmul A* """


def str_info_noduri(l):
    """
        o functie folosita strict in afisari - poate fi modificata in functie de problema
    """
    sir = "["
    for x in l:
        sir += str(x) + "  "
    sir += "]"
    return sir


def afis_succesori_cost(l):
    """
        o functie folosita strict in afisari - poate fi modificata in functie de problema
    """
    sir = ""
    for (x, cost) in l:
        sir += "\nnod: " + str(x) + ", cost arc:" + str(cost)

    return sir


def in_lista(l, nod):
    """
    lista "l" contine obiecte de tip NodParcurgere
    "nod" este de tip Nod
    """
    for i in range(len(l)):
        if l[i].nod_graf.info == nod.info:
            return l[i]
    return None


def a_star():
    rad_arbore = NodParcurgere(NodParcurgere.problema.nod_start)
    open = [rad_arbore]  # open va contine elemente de tip NodParcurgere
    closed = []  # closed va contine elemente de tip NodParcurgere

    while open:
        # sorteaza dupa f lista open

        open.sort(key=lambda nod: nod.f)

        nod_curent = open.pop(0)
        closed.append(nod_curent)

        if nod_curent.test_scop():
            print(f"closed: {closed[0]}")
            open.append(nod_curent)
            break
        else:
            succesori = nod_curent.expandeaza()

            for succesor in succesori:
                if nod_curent.contine_in_drum(succesor[0]) is False:

                    is_in_open = in_lista(open, succesor[0])
                    is_in_closed = in_lista(closed, succesor[0])

                    if is_in_open is None and is_in_closed is None:
                        succ_de_parcurs = NodParcurgere(succesor[0], nod_curent, nod_curent.g + succesor[1])
                        open.append(succ_de_parcurs)
                    else:
                        if is_in_open and is_in_open.f > nod_curent.f + succesor[1]:
                            # print(f"is in open {is_in_open}")
                            # print(f"is in closed {is_in_closed}")
                            is_in_open.parinte = nod_curent
                            is_in_open.g = nod_curent.g + succesor[1]
                            is_in_open.f = is_in_open.g + succesor[0].h
                            # print(is_in_open)
                        if is_in_closed and is_in_closed.f > nod_curent.f + succesor[1]:
                            is_in_closed.parinte = nod_curent
                            is_in_closed.g = nod_curent.g + succesor[1]
                            is_in_closed.f = is_in_closed.g + succesor[0].h
                            open.append(is_in_closed)
                            # print(is_in_closed)
                            closed.remove(is_in_closed)

    print("\n------------------ Concluzie -----------------------")
    if (len(open) == 0):
        print("Lista open e vida, nu avem drum de la nodul start la nodul scop")
    else:
        print("Drum de cost minim:\n " + str_info_noduri(nod_curent.drum_arbore()))

nod_scop = [(3, 'mov'),
            (2, 'verde')]

if __name__ == "__main__":
    # citire date din fisier
    inputFile = "input4.txt"

    combinatii = []
    stare_initiala = []
    stare_finala = []
    check = 0

    with open(inputFile, 'r') as file:
        for line in file:
            line = line.strip()
            if 'stare_initiala' in line:
                check = 1
                continue
            if 'stare_finala' in line:
                check = 2
                continue
            if check == 0:
                combinatii.append(line.split(' '))
                continue
            if check == 1:
                aux = line.split(' ')
                if len(aux) == 2:
                    aux.append('')
                aux[0] = int(aux[0])
                aux[1] = int(aux[1])
                stare_initiala.append(aux)
            if check == 2:
                aux = line.split(' ')
                aux[0] = int(aux[0])
                stare_finala.append((aux[0], aux[1]))

    nod_scop = stare_finala
    print(stare_finala)
    print(stare_initiala)
    print(combinatii)

    problema = Problema(combinatii, stare_initiala)
    NodParcurgere.problema = problema
    t_inainte = int(round(time.time() * 1000))
    a_star()
    t_dupa = int(round(time.time() * 1000))
    print("Timp de rulare: " + str(t_dupa - t_inainte) + " milisecunde.")

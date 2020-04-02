# Grupa: 232  Nume:Biro-Balan Antonia

""" definirea problemei """

N = 3
M = 2

# True -> barca se afla pe malul de est
# False -> barca se afla pe malul de vest

nod_scop = [[0, 0], [N, N], False]

class Nod:
    def __init__(self, info):
        self.info = info
        self.h = self.euristica()

    def __str__(self):
        return "({}, h={})".format(self.info, self.h)

    def __repr__(self):
        return f"({self.info}, h={self.h})"

    def euristica(self):
        nr_misionari = self.info[0][0]
        nr_canibali = self.info[0][1]
        return (nr_canibali + nr_misionari)/(M-1)


class Problema:

    def __init__(self):
        self.nod_start = Nod([[3, 3], [0, 0], True]) # de tip Nod


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
        """
        rez = []

        mal = self.nod_graf.info[2]
        mal_curent = 0

        if mal == True:
            mal_curent = 0
        else:
            mal_curent = 1

        mis_curent = self.nod_graf.info[mal_curent][0]
        can_curent = self.nod_graf.info[mal_curent][1]

        o_mis = self.nod_graf.info[(1+mal_curent)%2][0]
        o_can = self.nod_graf.info[(1 + mal_curent) % 2][1]

        for i in range(mis_curent+1):
            for j in range(can_curent+1):
                if i + j + mis_curent-i + can_curent-j + o_mis + o_can == 2*N:
                    if i >= j or i == 0:
                        if mis_curent-i >= can_curent-j or mis_curent-i == 0:
                            if 0 < i + j <= M:
                                if mal_curent == 0:
                                    rez.append((Nod([[mis_curent-i, can_curent-j], [i, j], not mal]), 1))
                                else:
                                    rez.append((Nod([[i, j], [mis_curent-i, can_curent-j], not mal]), 1))

        return rez

    # se modifica in functie de problema
    def test_scop(self):
        return self.nod_graf.info == nod_scop

    def __str__(self):
        parinte = self.parinte if self.parinte is None else self.parinte.nod_graf.info
        return f"({self.nod_graf}, parinte={parinte}, f={self.f}, g={self.g})"


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
                            print(f"is in open {is_in_open}")
                            print(f"is in closed {is_in_closed}")
                            is_in_open.parinte = nod_curent
                            is_in_open.g = nod_curent.g + succesor[1]
                            is_in_open.f = is_in_open.g + succesor[0].h
                            print(is_in_open)
                        if is_in_closed and is_in_closed.f > nod_curent.f + succesor[1]:
                            is_in_closed.parinte = nod_curent
                            is_in_closed.g = nod_curent.g + succesor[1]
                            is_in_closed.f = is_in_closed.g + succesor[0].h
                            open.append(is_in_closed)
                            print(is_in_closed)
                            closed.remove(is_in_closed)

    print("\n------------------ Concluzie -----------------------")
    if (len(open) == 0):
        print("Lista open e vida, nu avem drum de la nodul start la nodul scop")
    else:
        print("Drum de cost minim: " + str_info_noduri(nod_curent.drum_arbore()))


if __name__ == "__main__":
    problema = Problema()
    NodParcurgere.problema = problema
    a_star()

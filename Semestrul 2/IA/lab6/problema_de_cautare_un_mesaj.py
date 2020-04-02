""" definirea problemei """

nod_scop = ['dragos', 3, 5]

class Nod:

    def __init__(self, info):
        self.info = info
        self.h = self.euristica()

    def __str__(self):
        return "({}, h={})".format(self.info, self.h)

    def __repr__(self):
        return f"({self.info}, h={self.h})"

    def euristica(self):

        nume_curent = self.info

        return abs(nume_curent[1] - nod_scop[1]) + abs(nume_curent[2] - nod_scop[2])

class Problema:
    def __init__(self):
        self.matrix = [['ionel', 'alina', 'teo', 'eliza', 'carmen', 'monica'],
                       ['george', 'diana', 'bob', 'liber', 'nadia', 'mihai'],
                       ['liber', 'costin', 'anda', 'bogdan', 'dora', 'marin'],
                       ['luiza', 'simona', 'dana', 'cristian', 'tamara', 'dragos'],
                       ['mihnea', 'razvan', 'radu', 'patricia', 'gigel', 'elena'],
                       ['liber', 'andrei', 'oana', 'victor', 'liber', 'dorel'],
                       ['viorel', 'alex', 'ela', 'nicoleta', 'maria', 'gabi']]

        self.suparati = [['george', 'ionel'],
                         ['ela', 'nicoleta'],
                         ['victor', 'oana'],
                         ['teo', 'eliza'],
                         ['teo', 'luiza'],
                         ['elena', 'dragos'],
                         ['alina', 'dragos']]

        self.nod_start = Nod(['ionel', 0, 0]) # de tip Nod

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
        copil = self.nod_graf.info[0]
        rand = self.nod_graf.info[1]
        coloana = self.nod_graf.info[2]

        rez = []

        if rand != 0: # ma uit sus
            coleg = self.problema.matrix[rand - 1][coloana]
            if coleg != 'liber':
                if [copil, coleg] not in self.problema.suparati:
                    if [coleg, copil] not in self.problema.suparati:
                        rez.append((Nod([coleg, rand - 1, coloana]), 1))


        if rand != len(self.problema.matrix)-1: # ma uit jos
            coleg = self.problema.matrix[rand + 1][coloana]
            if coleg != 'liber':
                if [copil, coleg] not in self.problema.suparati:
                    if [coleg, copil] not in self.problema.suparati:
                        rez.append((Nod([coleg, rand + 1, coloana]), 1))

        if coloana != 0: # ma uit in stanga
            coleg = self.problema.matrix[rand][coloana - 1]
            if coleg != 'liber':
                if [copil, coleg] not in self.problema.suparati:
                    if [coleg, copil] not in self.problema.suparati:
                        if coloana != 2 and coloana != 4:
                            rez.append((Nod([coleg, rand, coloana - 1]), 1))
                        else:
                            if rand >= len(self.problema.matrix)-2:
                                rez.append((Nod([coleg, rand, coloana - 1]), 1))

        if coloana != 5: # ma uit in dreapta
            coleg = self.problema.matrix[rand][coloana + 1]
            if coleg != 'liber':
                if [copil, coleg] not in self.problema.suparati:
                    if [coleg, copil] not in self.problema.suparati:
                        if coloana != 1 and coloana != 3:
                            rez.append((Nod([coleg, rand, coloana + 1]), 1))
                        else:
                            if rand >= len(self.problema.matrix) - 2:
                                rez.append((Nod([coleg, rand, coloana + 1]), 1))

        return rez

    # se modifica in functie de problema
    def test_scop(self):
        return self.nod_graf.info == nod_scop

    def __str__(self):

        if self.nod_graf == self.problema.nod_start:
            return f"{self.nod_graf.info[0]}"

        parinte = self.parinte if self.parinte is None else self.parinte.nod_graf.info
        semn_parinte = ''
        if parinte[1] < self.nod_graf.info[1]:
            semn_parinte = 'v'
        else:
            if parinte[1] > self.nod_graf.info[1]:
                semn_parinte = '^'
            else:
                if parinte[2] > self.nod_graf.info[2]:
                    if parinte[2] == 2 or parinte[2] == 4:
                        semn_parinte = '<<'
                    else:
                        semn_parinte = '<'
                else:
                    if parinte[2] == 1 or parinte[2] == 3:
                        semn_parinte = '>>'
                    else:
                        semn_parinte = '>'

        return f" {semn_parinte} {self.nod_graf.info[0]}"


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

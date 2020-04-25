# 232 Biro Balan Antonia

import time
from copy import deepcopy


class Joc:
    """
    Clasa care defineste jocul. Se va schimba de la un joc la altul.
    """
    NR_COLOANE = 8
    NR_LINII = 8
    SIMBOLURI_JUC = ['N', 'A']
    JMIN = None
    JMAX = None
    GOL = '#'

    def __init__(self, tabla):
        self.matr = tabla

    def multi_hop(self, i, j, culoare, jucator, l_mutari, tabla):

        juc_opus = Joc.JMIN if jucator == Joc.JMAX else Joc.JMAX
        a = i + (-1 * culoare)
        b = j + (-1 * culoare)
        c = j + (+1 * culoare)

        exista_mutari = (tabla[a][b] == juc_opus and tabla[a + (-1*culoare)][b + (-1*culoare)] == Joc.GOL) or\
                        (tabla[a][c] == juc_opus and tabla[a + (-1*culoare)][c + (+1*culoare)] == Joc.GOL)

        if not exista_mutari:
            if i == 1 or i == Joc.NR_LINII:  # verificam daca trebuie sa il facem rege
                tabla[i][j] = jucator.upper()
            else:
                tabla[i][j] = jucator
            l_mutari.append(Joc(tabla))

        # mutari la stanga
        if tabla[a][b].upper() == juc_opus.upper() and tabla[a + (-1*culoare)][b + (-1*culoare)] == Joc.GOL:
            copie_tabla = deepcopy(tabla)
            copie_tabla[a][b] = Joc.GOL
            copie_tabla[i][j] = Joc.GOL
            self.multi_hop(a + (-1*culoare), b + (-1*culoare), culoare, jucator, l_mutari, copie_tabla)

        # mutari la dreapta
        if tabla[a][c].upper() == juc_opus.upper() and tabla[a + (-1*culoare)][c + (+1*culoare)] == Joc.GOL:
            copie_tabla = deepcopy(tabla)
            copie_tabla[a][c] = Joc.GOL
            copie_tabla[i][j] = Joc.GOL
            self.multi_hop(a + (-1*culoare), c + (+1*culoare), culoare, jucator, l_mutari, copie_tabla)

    def multi_hop_rege(self, i, j, culoare, jucator, l_mutari, tabla):

        juc_opus = Joc.JMIN if jucator == Joc.JMAX else Joc.JMAX
        a = i + (-1 * culoare)
        b = i + (+1 * culoare)
        c = j + (-1 * culoare)
        d = j + (+1 * culoare)

        # a,c - stanga sus  a,d - dreapta sus
        # b,c - stanga jos  b,d - dreapta jos

        exista_mutari = (tabla[a][c].upper() == juc_opus.upper() and tabla[a + (-1*culoare)][c + (-1*culoare)] == Joc.GOL) or\
                        (tabla[a][d].upper() == juc_opus.upper() and tabla[a + (-1*culoare)][d + (+1*culoare)] == Joc.GOL) or\
                        (tabla[b][c].upper() == juc_opus.upper() and tabla[b + (+1*culoare)][c + (-1*culoare)] == Joc.GOL) or\
                        (tabla[b][d].upper() == juc_opus.upper() and tabla[b + (+1*culoare)][d + (+1*culoare)] == Joc.GOL)

        if not exista_mutari:   # conditie de iesire din recursie - nu mai avem pozitii in care sa sarim
            if i == 1 or i == Joc.NR_LINII:  # verificam daca trebuie sa il facem rege
                tabla[i][j] = jucator.upper()
            else:
                tabla[i][j] = jucator.upper()
            l_mutari.append(Joc(tabla))

        # mutari la stanga sus
        if tabla[a][c].upper() == juc_opus.upper() and tabla[a + (-1*culoare)][c + (-1*culoare)] == Joc.GOL:
            copie_tabla = deepcopy(tabla)
            copie_tabla[a][c] = Joc.GOL
            copie_tabla[i][j] = Joc.GOL
            self.multi_hop(a + (-1*culoare), c + (-1*culoare), culoare, jucator, l_mutari, copie_tabla)

        # mutari la dreapta sus
        if tabla[a][d].upper() == juc_opus.upper() and tabla[a + (-1*culoare)][d + (+1*culoare)] == Joc.GOL:
            copie_tabla = deepcopy(tabla)
            copie_tabla[a][d] = Joc.GOL
            copie_tabla[i][j] = Joc.GOL
            self.multi_hop(a + (-1*culoare), d + (+1*culoare), culoare, jucator, l_mutari, copie_tabla)

        # mutari la stanga jos
        if tabla[b][c].upper() == juc_opus.upper() and tabla[b + (+1 * culoare)][c + (-1 * culoare)] == Joc.GOL:
            copie_tabla = deepcopy(tabla)
            copie_tabla[b][c] = Joc.GOL
            copie_tabla[i][j] = Joc.GOL
            self.multi_hop(b + (+1 * culoare), c + (-1 * culoare), culoare, jucator, l_mutari, copie_tabla)

        # mutari la dreapta jos
        if tabla[b][d].upper() == juc_opus.upper() and tabla[b + (+1 * culoare)][d + (+1 * culoare)] == Joc.GOL:
            copie_tabla = deepcopy(tabla)
            copie_tabla[b][d] = Joc.GOL
            copie_tabla[i][j] = Joc.GOL
            self.multi_hop(b + (-1 * culoare), d + (+1 * culoare), culoare, jucator, l_mutari, copie_tabla)

    def verifica_mutare_rege(self, i, j, culoare, jucator, l_mutari):
        juc_opus = Joc.JMIN if jucator == Joc.JMAX else Joc.JMAX

        # stanga sus Gol
        a = i + (-1 * culoare)
        b = j + (-1 * culoare)
        if self.matr[a][b] == Joc.GOL:
            copie_tabla = deepcopy(self.matr)
            copie_tabla[i][j] = Joc.GOL
            copie_tabla[a][b] = jucator.upper()
            l_mutari.append(Joc(copie_tabla))

        # dreapta sus Gol
        a = i + (-1 * culoare)
        b = j + (+1 * culoare)
        if self.matr[a][b] == Joc.GOL:
            copie_tabla = deepcopy(self.matr)
            copie_tabla[i][j] = Joc.GOL
            copie_tabla[a][b] = jucator.upper()
            l_mutari.append(Joc(copie_tabla))

        # stanga jos Gol
        a = i + (+1 * culoare)
        b = j + (-1 * culoare)
        if self.matr[a][b] == Joc.GOL:
            copie_tabla = deepcopy(self.matr)
            copie_tabla[i][j] = Joc.GOL
            copie_tabla[a][b] = jucator.upper()
            l_mutari.append(Joc(copie_tabla))

        #dreapta jos Gol
        a = i + (+1 * culoare)
        b = j + (+1 * culoare)
        if self.matr[a][b] == Joc.GOL:
            copie_tabla = deepcopy(self.matr)
            copie_tabla[i][j] = Joc.GOL
            copie_tabla[a][b] = jucator.upper()
            l_mutari.append(Joc(copie_tabla))

        # stanga sau dreapta, sus sau jos Jucator opus
        a = i + (-1 * culoare)
        b = i + (+1 * culoare)
        c = j + (-1 * culoare)
        d = j + (+1 * culoare)

        exista_mutari = (self.matr[a][c].upper() == juc_opus.upper() and self.matr[a + (-1*culoare)][c + (-1*culoare)] == Joc.GOL) or \
                        (self.matr[a][d].upper() == juc_opus.upper() and self.matr[a + (-1*culoare)][d + (+1*culoare)] == Joc.GOL) or \
                        (self.matr[b][c].upper() == juc_opus.upper() and self.matr[b + (+1*culoare)][c + (-1*culoare)] == Joc.GOL) or \
                        (self.matr[b][d].upper() == juc_opus.upper() and self.matr[b + (+1*culoare)][d + (+1*culoare)] == Joc.GOL)

        if exista_mutari:
            copie_tabla = deepcopy(self.matr)
            self.multi_hop_rege(i, j, culoare, jucator, l_mutari, copie_tabla)

    def verifica_mutare(self, i, j, culoare, jucator, l_mutari):
        juc_opus = Joc.JMIN if jucator == Joc.JMAX else Joc.JMAX

        # stanga Gol
        a = i + (-1 * culoare)
        b = j + (-1 * culoare)

        if self.matr[a][b] == Joc.GOL:
            copie_tabla = deepcopy(self.matr)
            copie_tabla[i][j] = Joc.GOL
            if a == 1 or a == Joc.NR_LINII:  # devine rege
                copie_tabla[a][b] = jucator.upper()
            else:
                copie_tabla[a][b] = jucator
            l_mutari.append(Joc(copie_tabla))

        # dreapta Gol
        a = i + (-1 * culoare)
        b = j + (+1 * culoare)
        if self.matr[a][b] == Joc.GOL:
            copie_tabla = deepcopy(self.matr)
            copie_tabla[i][j] = Joc.GOL
            if a == 1 or a == Joc.NR_LINII:  # devine rege
                copie_tabla[a][b] = jucator.upper()
            else:
                copie_tabla[a][b] = jucator
            l_mutari.append(Joc(copie_tabla))

        # stanga sau dreapta Jucator opus
        a = i + (-1 * culoare)
        b = j + (-1 * culoare)
        c = j + (+1 * culoare)

        exista_mutari = (self.matr[a][b].upper() == juc_opus.upper() and self.matr[a + (-1*culoare)][b + (-1*culoare)] == Joc.GOL) or\
                        (self.matr[a][c].upper() == juc_opus.upper() and self.matr[a + (-1*culoare)][c + (+1*culoare)] == Joc.GOL)

        if exista_mutari:
            copie_tabla = deepcopy(self.matr)
            self.multi_hop(i, j, culoare, jucator, l_mutari, copie_tabla)

    def mutari(self, jucator):
        l_mutari = []

        # TO DO..........
        # returneaza o lista cu toate mutarile posibile (obiecte de tip tabla_joc)

        culoare = -1 if jucator.upper() == 'N' else 1

        for i in range(1, Joc.NR_LINII+1):
            for j in range(1, Joc.NR_COLOANE+1):
                if self.matr[i][j] == jucator:  # pozitie pe tabla unde se afla o piesa a jucatorului curent
                    self.verifica_mutare(i, j, culoare, jucator, l_mutari)
                if self.matr[i][j] == jucator.upper():   # verificam daca e rege
                    self.verifica_mutare_rege(i, j, culoare, jucator, l_mutari)

        return l_mutari

    def get_positions(self, jucator):
        mutari = self.mutari(jucator)

        l_pozitii = []

        for tabla in mutari:

            for i in range(1, Joc.NR_LINII+1):
                for j in range(1, Joc.NR_COLOANE+1):
                    if self.matr[i][j] != tabla.matr[i][j] and tabla.matr[i][j].upper() == jucator.upper():
                        l_pozitii.append(([i, j], tabla))

        return l_pozitii

    def nr_piese_pe_tabla(self, jucator):
        # ne uitam cate piese sunt din culoarea jucatorului
        rez = 0

        for i in range(1, Joc.NR_LINII+1):
            for j in range(1, Joc.NR_COLOANE+1):
                if self.matr[i][j].upper() == jucator.upper():
                    rez += 1
        return rez

    def nr_regi_pe_tabla(self, jucator):
        # ne uitam cati regi ale jucatorului curent sunt pe tabla
        rez = 0

        for i in range(1, Joc.NR_LINII + 1):
            for j in range(1, Joc.NR_COLOANE + 1):
                if self.matr[i][j] == jucator.upper():
                    rez += 1
        return rez

    def final(self):
        # returnam simbolul jucatorului castigator sau 'False' daca nu s-a terminat jocul
        # daca un jucator a luat toate piesele celuilalt jucator acesta castiga
        # daca un jucator ramane fara mutari (este blocat) pierde
        # daca nici un jucator nu mai are mutari valide -> remiza

        mutari_max = self.get_positions(Joc.JMAX)
        mutari_min = self.get_positions(Joc.JMIN)

        if self.nr_piese_pe_tabla(Joc.JMAX) == 0 or len(mutari_max) == 0:
            return Joc.JMIN

        if self.nr_piese_pe_tabla(Joc.JMIN) == 0 or len(mutari_min) == 0:
            return Joc.JMAX

        if len(mutari_min) == 0 and len(mutari_max) == 0:
            if self.nr_piese_pe_tabla(Joc.JMIN) > self.nr_piese_pe_tabla(Joc.JMAX):
                return Joc.MIN
            elif self.nr_piese_pe_tabla(Joc.JMIN) < self.nr_piese_pe_tabla(Joc.JMAX):
                return Joc.MAX
            else:
                return 'remiza'


        return False

    def fct_euristica1(self):
        # diferenta dintre nr de piese negre si cele albe de pe tabla in configuratia curenta
        return self.nr_piese_pe_tabla(Joc.JMAX) - self.nr_piese_pe_tabla(Joc.JMIN)

    def fct_euristica2(self):
        # diferenta dintre nr de piese negre si cele albe de pe tabla in configuratia curenta
        # la care adaugam in plus nr de regi pentru fiecare culoare

        estimare_min = self.nr_piese_pe_tabla(Joc.JMIN) + self.nr_regi_pe_tabla(Joc.JMIN)
        estimare_max = self.nr_piese_pe_tabla(Joc.JMAX) + self.nr_regi_pe_tabla(Joc.JMAX)

        return estimare_max - estimare_min

    def estimeaza_scor(self, adancime):
        t_final = self.final()
        if t_final == Joc.JMAX:
            return (999 + adancime)
        elif t_final == Joc.JMIN:
            return (-999 - adancime)
        elif t_final == 'remiza':
            return 0
        else:
            return self.fct_euristica2()

    def __str__(self):
        sir = '    a b c d e f g h\n    --------------\n'

        for i in range(1, Joc.NR_LINII+1):
            sir += str(i) + ': '
            for j in range(1, Joc.NR_COLOANE+1):
                sir = sir + self.matr[i][j] + ' '
            sir += "\n"

        return sir


class Stare:
    """
    Clasa folosita de algoritmii minimax si alpha-beta
    Are ca proprietate tabla de joc
    Functioneaza cu conditia ca in cadrul clasei Joc sa fie definiti JMIN si JMAX (cei doi jucatori posibili)
    De asemenea cere ca in clasa Joc sa fie definita si o metoda numita mutari() care ofera lista cu
    configuratiile posibile in urma mutarii unui jucator
    """

    ADANCIME_MAX = None

    def __init__(self, tabla_joc, j_curent, adancime, parinte=None, scor=None):
        self.tabla_joc = tabla_joc
        self.j_curent = j_curent

        # adancimea in arborele de stari
        self.adancime = adancime

        # scorul starii (daca e finala) sau al celei mai bune stari-fiice (pentru jucatorul curent)
        self.scor = scor

        # lista de mutari posibile din starea curenta
        self.mutari_posibile = []

        # cea mai buna mutare din lista de mutari posibile pentru jucatorul curent
        self.stare_aleasa = None

    def jucator_opus(self):
        if self.j_curent == Joc.JMIN:
            return Joc.JMAX
        else:
            return Joc.JMIN

    def mutari(self):
        l_mutari = self.tabla_joc.mutari(self.j_curent)
        juc_opus = self.jucator_opus()
        l_stari_mutari = [Stare(mutare, juc_opus, self.adancime - 1, parinte=self) for mutare in l_mutari]

        return l_stari_mutari

    def __str__(self):
        sir = str(self.tabla_joc) + "(Jucator curent: " + self.j_curent + ")\n"
        return sir


""" Algoritmul MinMax """


def min_max(stare):
    if stare.adancime == 0 or stare.tabla_joc.final():
        stare.scor = stare.tabla_joc.estimeaza_scor(stare.adancime)
        return stare

    # calculez toate mutarile posibile din starea curenta
    stare.mutari_posibile = stare.mutari()

    # aplic algoritmul minimax pe toate mutarile posibile (calculand astfel subarborii lor)
    mutari_scor = [min_max(mutare) for mutare in stare.mutari_posibile]

    if stare.j_curent == Joc.JMAX:
        # daca jucatorul e JMAX aleg starea-fiica cu scorul maxim
        stare.stare_aleasa = max(mutari_scor, key=lambda x: x.scor)
    else:
        # daca jucatorul e JMIN aleg starea-fiica cu scorul minim
        stare.stare_aleasa = min(mutari_scor, key=lambda x: x.scor)

    stare.scor = stare.stare_aleasa.scor
    return stare


def alpha_beta(alpha, beta, stare):
    if stare.adancime == 0 or stare.tabla_joc.final():
        stare.scor = stare.tabla_joc.estimeaza_scor(stare.adancime)
        return stare

    if alpha >= beta:
        return stare  # este intr-un interval invalid deci nu o mai procesez

    stare.mutari_posibile = stare.mutari()

    if stare.j_curent.lower() == Joc.JMAX.lower():
        scor_curent = float('-inf')

        for mutare in stare.mutari_posibile:
            # calculeaza scorul
            stare_noua = alpha_beta(alpha, beta, mutare)

            if (scor_curent < stare_noua.scor):
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor
            if (alpha < stare_noua.scor):
                alpha = stare_noua.scor
                if alpha >= beta:
                    break

    elif stare.j_curent.lower() == Joc.JMIN.lower():
        scor_curent = float('inf')

        for mutare in stare.mutari_posibile:
            stare_noua = alpha_beta(alpha, beta, mutare)

            if (scor_curent > stare_noua.scor):
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor

            if (beta > stare_noua.scor):
                beta = stare_noua.scor
                if alpha >= beta:
                    break

    stare.scor = stare.stare_aleasa.scor

    return stare


def afis_daca_final(stare_curenta):
    final = stare_curenta.tabla_joc.final()
    if (final):
        if (final == "remiza"):
            print("Remiza!")
        else:
            print("A castigat " + final)

        # afisare scor jucatori la sfarsitul jocului
        print(f"Scor jucator uman: {stare_curenta.tabla_joc.nr_piese_pe_tabla(Joc.JMIN)}")
        print(f"Scor calculator: {stare_curenta.tabla_joc.nr_piese_pe_tabla(Joc.JMAX)}")

        return True

    return False


def main(nr_mutari_jucatori):
    # initializare algoritm
    raspuns_valid = False
    while not raspuns_valid:
        tip_algoritm = input("Algorimul folosit? (raspundeti cu 1 sau 2)\n 1.Minimax\n 2.Alpha-beta\n ")
        if tip_algoritm in ['1', '2']:
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")

    # initializare ADANCIME_MAX
    raspuns_valid = False
    nivele = ['incepator', 'mediu', 'avansat']
    while not raspuns_valid:
        n = input("Nivelul de dificultate (incepator, mediu, avansat): ")
        if n in nivele:
            Stare.ADANCIME_MAX = nivele.index(n)+1
            raspuns_valid = True
        else:
            print("Trebuie sa introduceti un numar natural nenul.")

    # initializare jucatori
    [s1, s2] = Joc.SIMBOLURI_JUC.copy()  # lista de simboluri posibile
    raspuns_valid = False
    while not raspuns_valid:
        Joc.JMIN = str(input("Doriti sa jucati cu {} sau cu {}? ".format(s1, s2))).upper()
        if (Joc.JMIN in Joc.SIMBOLURI_JUC):
            raspuns_valid = True
            print("raspuns bun!")
        else:
            print("Raspunsul trebuie sa fie {} sau {}.".format(s1, s2))
    Joc.JMAX = s1 if Joc.JMIN == s2 else s2
    Joc.JMAX = Joc.JMAX.lower()
    Joc.JMIN = Joc.JMIN.lower()

    # initializare tabla
    # bordare cu spatii

    tabla = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', '#', 'n', '#', 'n', '#', 'n', '#', 'n', ' '],
             [' ', 'n', '#', 'n', '#', 'n', '#', 'n', '#', ' '],
             [' ', '#', 'n', '#', 'n', '#', 'n', '#', 'n', ' '],
             [' ', '#', '#', '#', '#', '#', '#', '#', '#', ' '],
             [' ', '#', '#', '#', '#', '#', '#', '#', '#', ' '],
             [' ', 'a', '#', 'a', '#', 'a', '#', 'a', '#', ' '],
             [' ', '#', 'a', '#', 'a', '#', 'a', '#', 'a', ' '],
             [' ', 'a', '#', 'a', '#', 'a', '#', 'a', '#', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    tabla_curenta = Joc(tabla)
    print("Tabla initiala")
    print(str(tabla_curenta))

    # creare stare initiala
    stare_curenta = Stare(tabla_curenta, 'n', Stare.ADANCIME_MAX)

    while True:
        if (stare_curenta.j_curent == Joc.JMIN):
            # muta jucatorul
            raspuns_valid = False
            tabla_noua = None

            t_inainte = int(round(time.time() * 1000))
            while not raspuns_valid:
                try:

                    mutari_pos = stare_curenta.tabla_joc.get_positions(stare_curenta.j_curent)
                    pozitii = [(idx, elem[0]) for idx, elem in enumerate(mutari_pos)]
                    print(f"Mutari posibile: {pozitii}")

                    input_ = input("pozitie aleasa din lista = ")
                    if input_ == 'exit':
                        print(f"Scor jucator uman: {stare_curenta.tabla_joc.nr_piese_pe_tabla(Joc.JMIN)}")
                        print(f"Scor calculator: {stare_curenta.tabla_joc.nr_piese_pe_tabla(Joc.JMAX)}")
                        return False
                    pozitie_aleasa = int(input_)

                    # de verificat daca "coloana" si "linie" sunt in intervalul corect,
                    # si daca e valida pozitia

                    if pozitie_aleasa in range(len(pozitii)):
                        print(f"Alegerea ta: {pozitii[pozitie_aleasa]}")
                        tabla_noua = mutari_pos[pozitie_aleasa][1]
                        raspuns_valid = True
                    else:
                        print(f"Indice pozitie invalid (trebuie sa fie un numar intre 0 si {len(pozitii)}")

                except ValueError:
                    print("Indice pozitie trebuie sa fie un numere intreg.")

            # dupa iesirea din while sigur am valida coloana
            # deci pot plasa simbolul pe "tabla de joc"
            stare_curenta.tabla_joc = tabla_noua

            t_dupa = int(round(time.time() * 1000))
            print("Jucatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.")

            # afisarea starii jocului in urma mutarii utilizatorului
            print("\nTabla dupa mutarea jucatorului")
            print(str(stare_curenta))

            nr_mutari_jucatori[0] += 1

            # testez daca jocul a ajuns intr-o stare finala
            # si afisez un mesaj corespunzator in caz ca da
            if (afis_daca_final(stare_curenta)):
                break

            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = stare_curenta.jucator_opus()

        # --------------------------------
        else:  # jucatorul e JMAX (calculatorul)
            # Mutare calculator

            # preiau timpul in milisecunde de dinainte de mutare
            t_inainte = int(round(time.time() * 1000))
            if tip_algoritm == '1':
                stare_actualizata = min_max(stare_curenta)
            else:  # tip_algoritm==2
                stare_actualizata = alpha_beta(-5000, 5000, stare_curenta)

            stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc
            print("Tabla dupa mutarea calculatorului")
            print(str(stare_curenta))

            # preiau timpul in milisecunde de dupa mutare
            t_dupa = int(round(time.time() * 1000))
            print("Calculatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.")

            nr_mutari_jucatori[1] += 1

            if (afis_daca_final(stare_curenta)):
                break

            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = stare_curenta.jucator_opus()


if __name__ == "__main__":
    t_inainte = int(round(time.time() * 1000))


    # nr_mutari_jucatori[0] -> mutari ale Joc.MIN
    # nr_mutari_jucatori[1] -> mutari ale Joc.Max
    nr_mutari_jucatori = [0, 0]

    main(nr_mutari_jucatori)


    t_dupa = int(round(time.time() * 1000))
    print("Jocul a rulat timp de " + str(t_dupa - t_inainte) + " milisecunde.")

    print(f"Jucatorul uman a facut {nr_mutari_jucatori[0]} mutari")
    print(f"Calculatorul a facut {nr_mutari_jucatori[1]} mutari")
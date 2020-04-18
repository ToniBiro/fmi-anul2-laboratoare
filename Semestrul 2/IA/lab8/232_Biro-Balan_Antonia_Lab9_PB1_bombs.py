import time
from copy import deepcopy

class Joc:
    """
    Clasa care defineste jocul. Se va schimba de la un joc la altul.
    """
    NR_COLOANE = 22
    NR_LINII = 13
    SIMBOLURI_JUC = ['1', '2']  # ['G', 'R'] sau ['X', '0']
    JMIN = None
    JMAX = None
    GOL = ' '
    SCUT = 'p'

    def __init__(self, tabla, viata_min=1, viata_max=1, c_min=(1, 1), c_max=(11, 20),
                 bomba_min=0, bomba_max=0, c_bomba_min=None, c_bomba_max=None, b_activa_min=0, b_activa_max=0):
        self.matr = tabla
        self.viata_min = viata_min
        self.viata_max = viata_max
        self.c_min = c_min
        self.c_max = c_max
        self.bomba_min = bomba_min
        self.bomba_max = bomba_max
        self.c_bomba_min = c_bomba_min
        self.c_bomba_max = c_bomba_max
        self.b_activa_min = b_activa_min
        self.b_activa_max = b_activa_max

    def final(self):
        # returnam simbolul jucatorului inca viu
        # sau 'False' daca nu s-a terminat jocul

        if self.viata_min == 0:
            return Joc.JMIN

        if self.viata_max == 0:
            return Joc.JMAX
            
        return False

    def adauga_mutari(self, ii, jj, i, j, jucator):
        l_mutari = []

        # initializare variabile curente
        bomba = 0
        bomba_activa = 0
        cord_b_l = 0
        cord_b_c = 0
        protectie = 0
        bomba_mea = 0
        bomba_mea_activa = 0
        if jucator == Joc.JMAX:
            bomba_mea = self.bomba_max
            if bomba_mea == 1:
                bomba_mea_activa = self.b_activa_max
            bomba = self.bomba_min
            bomba_activa = self.b_activa_min
            protectie = self.viata_max - 1
            if bomba == 1 and bomba_activa == 1:
                cord_b_l = self.c_bomba_min[0]
                cord_b_c = self.c_bomba_min[1]

        if jucator == Joc.JMIN:
            bomba_mea = self.bomba_min
            if bomba_mea == 1:
                bomba_mea_activa = self.b_activa_min
            bomba = self.bomba_max
            bomba_activa = self.b_activa_max
            protectie = self.viata_min - 1
            if bomba == 1 and bomba_activa == 1:
                cord_b_l = self.c_bomba_max[0]
                cord_b_c = self.c_bomba_max[1]

        # cazuri posibile de mutari
        matr_aux = deepcopy(self.matr)
        if bomba_activa == 1 and (cord_b_l == i or cord_b_c == j):
            if protectie > 0 and matr_aux[i][j] == ' ' or protectie == 0 and matr_aux[i][j] == 'p':
                matr_aux[ii][jj] = ' '
                matr_aux[i][j] = jucator
                matr_aux[cord_b_l][cord_b_c] = ' '
                if jucator == Joc.JMAX:
                    l_mutari.append(Joc(matr_aux, c_max=(i, j), viata_max=self.viata_max-1, b_activa_min=0, bomba_min=0))
                else:
                    l_mutari.append(Joc(matr_aux, c_min=(i, j), viata_min=self.viata_min-1, b_activa_max=0, bomba_max=0))

                if bomba_mea == 0:
                    matr_aux[ii][jj] = 'b'
                    if jucator == Joc.JMAX:
                        l_mutari.append(
                            Joc(matr_aux, viata_max=self.viata_max-1, bomba_max=1, c_bomba_max=(ii, jj), b_activa_max=0, c_max=(i, j), b_activa_min=0, bomba_min=0))
                    else:
                        l_mutari.append(
                            Joc(matr_aux, viata_min=self.viata_min-1, bomba_min=1, c_bomba_min=(ii, jj), b_activa_min=0, c_min=(i, j), b_activa_max=0, bomba_max=0))
                if bomba_mea == 1 and bomba_mea_activa == 0:
                    if jucator == Joc.JMAX:
                        l_mutari.append(Joc(matr_aux, c_max=(i, j), b_activa_max=1, c_bomba_max=(ii, jj), b_activa_min=0, bomba_min=0))
                    if jucator == Joc.JMIN:
                        l_mutari.append(Joc(matr_aux, c_min=(i, j), b_activa_min=1, c_bomba_min=(ii, jj), b_activa_max=0, bomba_max=0))
            else:
                matr_aux[ii][jj] = ' '
                matr_aux[i][j] = ' '
                matr_aux[cord_b_l][cord_b_c] = ' '
                if jucator == Joc.JMAX:
                    l_mutari.append(Joc(matr_aux, viata_max=0, c_max=(i, j)))
                else:
                    l_mutari.append(Joc(matr_aux, viata_min=0, c_min=(i, j)))
        elif matr_aux[i][j] == ' ':
            matr_aux[ii][jj] = ' '
            matr_aux[i][j] = jucator
            if jucator == Joc.JMAX:
                l_mutari.append(Joc(matr_aux, c_max=(i, j)))
            else:
                l_mutari.append(Joc(matr_aux, c_min=(i, j)))

            if bomba_mea == 0:
                matr_aux[ii][jj] = 'b'
                if jucator == Joc.JMAX:
                    l_mutari.append(Joc(matr_aux, bomba_max=1, c_bomba_max=(ii, jj), b_activa_max=0, c_max=(i, j)))
                if jucator == Joc.JMIN:
                    l_mutari.append(Joc(matr_aux, bomba_min=1, c_bomba_min=(ii, jj), b_activa_min=0, c_min=(i, j)))
            if bomba_mea == 1 and bomba_mea_activa == 0:
                if jucator == Joc.JMAX:
                    l_mutari.append(Joc(matr_aux, b_activa_max=1, c_max=(i, j)))
                if jucator == Joc.JMIN:
                    l_mutari.append(Joc(matr_aux, b_activa_min=1, c_min=(i, j)))
        elif matr_aux[i][j] == 'p':
            matr_aux[ii][jj] = ' '
            matr_aux[i][j] = jucator
            if jucator == Joc.JMAX:
                l_mutari.append(Joc(matr_aux, c_max=(i, j), viata_max=self.viata_max+1))
            else:
                l_mutari.append(Joc(matr_aux, c_min=(i, j), viata_min=self.viata_min+1))

            if bomba_mea == 0:
                matr_aux[ii][jj] = 'b'
                if jucator == Joc.JMAX:
                    l_mutari.append(Joc(matr_aux, bomba_max=1, c_bomba_max=(ii, jj), b_activa_max=0, c_max=(i, j), viata_max=self.viata_max+1))
                if jucator == Joc.JMIN:
                    l_mutari.append(Joc(matr_aux, bomba_min=1, c_bomba_min=(ii, jj), b_activa_min=0, c_min=(i, j), viata_min=self.viata_min+1))
            if bomba_mea == 1 and bomba_mea_activa == 0:
                if jucator == Joc.JMAX:
                    l_mutari.append(Joc(matr_aux, b_activa_max=1, viata_max=self.viata_max+1, c_max=(i, j)))
                if jucator == Joc.JMIN:
                    l_mutari.append(Joc(matr_aux, b_activa_min=1, viata_min=self.viata_min+1, c_min=(i, j)))

        return l_mutari

    def mutari(self, jucator):
        l_mutari = []

        # lista de configuratii a tablei posibile
        # ma uit sus jos stanga dreapta din pozitia jucatorului

        # initializare
        cord_l = ''
        cord_c = ''
        if jucator == Joc.JMAX:
            cord_l = self.c_max[0]
            cord_c = self.c_max[1]
        if jucator == Joc.JMIN:
            cord_l = self.c_min[0]
            cord_c = self.c_min[1]

        # cazuri pas sus
        l_mutari += self.adauga_mutari(cord_l, cord_c, cord_l-1, cord_c, jucator)

        # cazuri pas drepata
        l_mutari += self.adauga_mutari(cord_l, cord_c, cord_l, cord_c+1, jucator)

        # cazuri pas jos
        l_mutari += self.adauga_mutari(cord_l, cord_c, cord_l+1, cord_c, jucator)

        # cazuri pas stanga
        l_mutari += self.adauga_mutari(cord_l, cord_c, cord_l, cord_c-1, jucator)

        return l_mutari

    def nr_scor(self, jucator):
        # poz libera 0 puncte
        # daca iau protectie +3 puncte
        # pun bomba 2 punct
        # activez bomba 1 punct
        # daca merg in dreptul unei bombe inamice scad 2

        rez = 0

        if jucator == Joc.JMAX:
            if self.viata_max > 1:
                rez += 3
            if self.bomba_max == 1:
                rez += 2
            if self.b_activa_max == 1:
                rez += 1
            if self.c_bomba_min == self.c_max:
                rez -= 2
        else:
            if self.viata_min > 1:
                rez += 3
            if self.bomba_min == 1:
                rez += 2
            if self.b_activa_min == 1:
                rez += 1
            if self.c_bomba_max == self.c_min:
                rez -= 2

        return rez

    def fct_euristica(self):
        return self.nr_scor(Joc.JMAX) - self.nr_scor(Joc.JMIN)

    def estimeaza_scor(self, adancime):
        t_final = self.final()
        if t_final == Joc.JMAX:
            return (999 + adancime)
        elif t_final == Joc.JMIN:
            return (-999 - adancime)
        elif t_final == 'remiza':
            return 0
        else:
            return self.fct_euristica()

    def __str__(self):
        sir = ''

        for i in range(Joc.NR_LINII):
            for j in range(Joc.NR_COLOANE):
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
        sir = str(self.tabla_joc) + "(Juc curent: " + self.j_curent + ")\n"
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

    if stare.j_curent == Joc.JMAX:
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

    elif stare.j_curent == Joc.JMIN:
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

        return True

    return False


def main():
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
    while not raspuns_valid:
        n = input("Adancime maxima a arborelui: ")
        if n.isdigit():
            Stare.ADANCIME_MAX = int(n)
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
        else:
            print("Raspunsul trebuie sa fie {} sau {}.".format(s1, s2))
    Joc.JMAX = s1 if Joc.JMIN == s2 else s2

    tabla = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
             ['#', '1', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
             ['#', ' ', '#', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#'],
             ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
             ['#', ' ', ' ', ' ', ' ', 'p', ' ', '#', ' ', ' ', 'p', ' ', ' ', '#', ' ', ' ', '#', '#', '#', ' ', '#', '#'],
             ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
             ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', ' ', '#', '#'],
             ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
             ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', '#'],
             ['#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', 'p', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
             ['#', ' ', '#', '#', '#', '#', ' ', '#', ' ', ' ', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', ' ', ' ', '#'],
             ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '2', '#'],
             ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

    # initializare tabla
    tabla_curenta = Joc(tabla, )
    print("Tabla initiala")
    print(str(tabla_curenta))

    # creare stare initiala
    stare_curenta = Stare(tabla_curenta, Joc.SIMBOLURI_JUC[0], Stare.ADANCIME_MAX)

    while True:
        if stare_curenta.j_curent == Joc.JMIN:
            # Mutare calculator1
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

            if afis_daca_final(stare_curenta):
                break

            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = stare_curenta.jucator_opus()


        else:  # jucatorul e JMAX (calculatorul)
            # Mutare calculator2

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

            if afis_daca_final(stare_curenta):
                break

            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = stare_curenta.jucator_opus()


if __name__ == "__main__":
    main()
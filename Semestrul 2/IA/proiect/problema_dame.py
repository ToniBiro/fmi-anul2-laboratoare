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
            if i == 0 or i == Joc.NR_LINII-1:  # verificam daca trebuie sa il facem rege
                tabla[i][j] = jucator.upper()
            else:
                tabla[i][j] = jucator
            l_mutari.append(Joc(tabla))

        # mutari la stanga
        if tabla[a][b] == juc_opus and tabla[a + (-1*culoare)][b + (-1*culoare)] == Joc.GOL:
            copie_tabla = deepcopy(tabla)
            copie_tabla[a][b] = Joc.GOL
            copie_tabla[i][j] = Joc.GOL
            self.multi_hop(a + (-1*culoare), b + (-1*culoare), culoare, jucator, l_mutari, copie_tabla)

        # mutari la dreapta
        if tabla[a][c] == juc_opus and tabla[a + (-1*culoare)][c + (+1*culoare)] == Joc.GOL:
            copie_tabla = deepcopy(tabla)
            copie_tabla[a][c] = Joc.GOL
            copie_tabla[i][j] = Joc.GOL
            self.multi_hop(a + (-1*culoare), c + (+1*culoare), culoare, jucator, l_mutari, copie_tabla)


    # def verifica_mutare_rege(self, i, j, culoare, l_mutari):


    def verifica_mutare(self, i, j, culoare, jucator, l_mutari):

        juc_opus = Joc.JMIN if jucator == Joc.JMAX else Joc.JMAX

        # stanga Gol
        a = i + (-1 * culoare)
        b = j + (-1 * culoare)

        if self.matr[a][b] == Joc.GOL:
            copie_tabla = deepcopy(self.matr)
            copie_tabla[i][j] = Joc.GOL
            if a == 0 or a == Joc.NR_LINII-1:  # devine rege
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
            if a == 0 or a == Joc.NR_LINII-1:  # devine rege
                copie_tabla[a][b] = jucator.upper()
            else:
                copie_tabla[a][b] = jucator
            l_mutari.append(copie_tabla)

        # stanga sau dreapta Jucator opus
        a = i + (-1 * culoare)
        b = j + (-1 * culoare)
        c = j + (+1 * culoare)

        exista_mutari = (self.matr[a][b] == juc_opus and self.matr[a + (-1 * culoare)][b + (-1 * culoare)] == Joc.GOL) or \
                        (self.matr[a][c] == juc_opus and self.matr[a + (-1 * culoare)][c + (+1 * culoare)] == Joc.GOL)

        if exista_mutari:
            copie_tabla = deepcopy(self.matr)
            self.multi_hop(i, j, culoare, jucator, l_mutari, copie_tabla)


    def mutari(self, jucator):
        l_mutari = []

        # TO DO..........
        # returneaza o lista cu toate mutarile posibile (obiecte de tip tabla_joc)

        culoare = -1 if jucator.upper() == 'N' else 1

        for i in range(Joc.NR_LINII):
            for j in range(Joc.NR_COLOANE):
                if self.matr[i][j] == jucator:  # pozitie pe tabla unde se afla o piesa a jucatorului curent
                    if self.matr[i][j] != jucator.upper():   # verificam sa nu fie rege
                        self.verifica_mutare(i, j, culoare, jucator, l_mutari)


        return l_mutari

    def get_positions(self, jucator):
        mutari = self.mutari(jucator)

        l_pozitii = []

        for tabla in mutari:
            for i in range(Joc.NR_LINII):
                for j in range(Joc.NR_COLOANE):
                    if self.matr[i][j] != tabla[i][j] and tabla[i][j] == jucator:
                        l_pozitii.append(([i, j], tabla))

        return l_pozitii

    def nr_piese_pe_tabla(self, jucator):
        # ne uitam cate piese sunt din culoarea jucatorului
        rez = 0

        for i in range(Joc.NR_LINII):
            for j in range(Joc.NR_COLOANE):
                if self.matr[i][j] == jucator:
                    rez += 1

        return rez

    def final(self):
        # returnam simbolul jucatorului castigator sau 'False' daca nu s-a terminat jocul
        #



        return False

    def fct_euristica(self):
        # diferenta dintre nr de piese negre si cele albe de pe tabla in configuratia curenta
        return self.nr_piese_pe_tabla(Joc.JMAX) - self.nr_piese_pe_tabla(Joc.JMIN)

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
        sir = '     a b c d e f g h\n     --------------\n'

        for i in range(1, Joc.NR_LINII+1):
            sir += str(i-1) + ': '
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
    print(f"in afis final: {final}")
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
            print("raspuns bun!")
        else:
            print("Raspunsul trebuie sa fie {} sau {}.".format(s1, s2))
    Joc.JMAX = s1 if Joc.JMIN == s2 else s2

    # initializare tabla
    # bordare cu spatii

    tabla = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', 'n', '#', 'n', '#', 'n', '#', 'n', '#', ' '],
             [' ', '#', 'n', '#', 'n', '#', 'n', '#', 'n', ' '],
             [' ', 'n', '#', 'n', '#', 'n', '#', 'n', '#', ' '],
             [' ', '#', '#', '#', '#', '#', '#', '#', '#', ' '],
             [' ', '#', '#', '#', '#', '#', '#', '#', '#', ' '],
             [' ', 'a', '#', 'a', '#', 'a', '#', 'a', '#', ' '],
             [' ', '#', 'a', '#', 'a', '#', 'a', '#', 'a', ' '],
             [' ', 'a', '#', 'a', '#', 'a', '#', 'a', '#', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    print("Init tabla joc")
    tabla_curenta = Joc(tabla)
    print("Tabla initiala")
    print(str(tabla_curenta))

    # creare stare initiala
    stare_curenta = Stare(tabla_curenta, 'n', Stare.ADANCIME_MAX)
    print(type(stare_curenta))

    while True:
        if (stare_curenta.j_curent == Joc.JMIN):
            # muta jucatorul
            raspuns_valid = False
            tabla_noua = None
            while not raspuns_valid:
                try:

                    mutari_pos = stare_curenta.tabla_joc.get_positions(stare_curenta.j_curent)
                    print(f"Mutari posibile: {mutari_pos}")
                    pozitii = [elem[0] for elem in mutari_pos]


                    linie = int(input("numar = "))
                    coloana = str(input("litera = "))
                    litere = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

                    # de verificat daca "coloana" si "linie" sunt in intervalul corect,
                    # si daca e valida pozitia


                    if linie in range(0, Joc.NR_LINII):
                        if coloana in litere:
                            if [linie, litere.index(coloana)] in pozitii:
                                tabla_noua = mutari_pos.index([linie, coloana])[1]
                                raspuns_valid = True
                    else:
                        print(
                            "Coloana sau linie invalida (trebuie sa fie un numar intre 0 si {} si pe o pozitie valida).".format(
                                Joc.NR_COLOANE - 1))

                except ValueError:
                    print("Coloana si linia trebuie sa fie un numere intregi.")

            # dupa iesirea din while sigur am valida coloana
            # deci pot plasa simbolul pe "tabla de joc"
            stare_curenta.tabla_joc = tabla_noua

            # afisarea starii jocului in urma mutarii utilizatorului
            print("\nTabla dupa mutarea jucatorului")
            print(str(stare_curenta))

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
            print(f"stare actualiazta: {type(stare_actualizata.stare_aleasa)}")
            stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc
            print("Tabla dupa mutarea calculatorului")
            print(str(stare_curenta))

            # preiau timpul in milisecunde de dupa mutare
            t_dupa = int(round(time.time() * 1000))
            print("Calculatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.")

            if (afis_daca_final(stare_curenta)):
                break

            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = stare_curenta.jucator_opus()


if __name__ == "__main__":
    main()
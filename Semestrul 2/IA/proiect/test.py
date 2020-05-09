
tabla = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', 'n', '#', 'n', '#', 'n', '#', 'n', '#', ' '],
         [' ', '#', 'n', '#', 'n', '#', 'n', '#', 'n', ' '],
         [' ', 'n', '#', 'n', '#', 'n', '#', 'n', '#', ' '],
         [' ', '#', '#', '#', '#', '#', '#', '#', '#', ' '],
         [' ', '#', 'n', '#', '#', '#', '#', '#', '#', ' '],
         [' ', 'a', '#', 'a', '#', 'a', '#', 'a', '#', ' '],
         [' ', '#', 'a', '#', 'a', '#', 'a', '#', 'a', ' '],
         [' ', 'a', '#', 'a', '#', 'a', '#', 'a', '#', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]


def multi_hop(i, j, culoare, jucator, tabla):

    juc_opus = 'a' if jucator == 'n' else 'n'
    a = i + (-1 * culoare)
    b = j + (-1 * culoare)
    c = j + (+1 * culoare)

    verif = (tabla[a][b] == juc_opus and tabla[a + (- 1 *culoare)][b + (- 1 *culoare)] == '#') or \
            (tabla[a][c] == juc_opus and tabla[a + (- 1 *culoare)][c + (- 1 *culoare)] == '#')

    return verif


print(multi_hop(6, 3, 1, 'a', tabla))
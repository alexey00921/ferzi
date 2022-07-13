import sys


def empty_chessboard(size):
    return [[0 for _ in range(size)] for _ in range(size)]


def print_chesboard(chessboard):
    for i in chessboard:
        print(i)


def line_sum(chessboard):
    for line in chessboard:
        if sum(line) > 1:
            print('NO')
            return False
    return True



def rhombus(chessboard):
    new_chessboard = empty_chessboard(15)
    for x, line in enumerate(chessboard):
        for y, i in enumerate(line):
            new_chessboard[x + y][y] = i
    return new_chessboard



def rotation(chessboard):
    new_chessboard = empty_chessboard(8)
    for x, line in enumerate(chessboard):
        for y, i in enumerate(line):
            new_chessboard[y][7 - x] = i
    return new_chessboard



def main(*args):
    chessboard = empty_chessboard(8)


    for i in args:
        chessboard[i[0] - 1][i[1] - 1] = 1

    print_chesboard(chessboard)

    for _ in range(2):
        if not line_sum(chessboard):
            print('NO')
            sys.exit('Больше одного ферзя на строке или столбце')

        if not line_sum(rhombus(chessboard)):
            print('NO')
            sys.exit('Больше одного ферьзя по диагонали')

        chessboard = rotation(chessboard)

    print('YES')



a1 = (1, 2)
a2 = (2, 4)
a3 = (3, 6)
a4 = (4, 8)
a5 = (5, 3)
a6 = (6, 1)
a7 = (7, 7)
a8 = (8, 5)


main(a1, a2, a3, a4, a5, a6, a7, a8)
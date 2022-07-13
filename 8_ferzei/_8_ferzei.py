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




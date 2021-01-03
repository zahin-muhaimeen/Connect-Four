import random as rand

BOARD_WIDTH = 7
BOARD_HEIGHT = 6
WINNING_LENGTH = 4

board = []

for i in range(BOARD_HEIGHT):
    board.append([])

for i in board:
    for j in range(BOARD_WIDTH):
        i.append(" ")


def printing_board():
    for row in board:
        print("|\t", end="")
        print("\t|\t".join(row), end="\t|\n")


def get_int(prompt: str) -> int:
    user_in = input(prompt)
    while not user_in.isnumeric():
        user_in = input(prompt)
    return int(user_in)


def choosing(prompt: int, letter: str):
    while True:
        num = get_int(prompt)
        if num in range(BOARD_WIDTH):
            if board[0][num] == " ":
                for row in board[::-1]:
                    if row[num] == " ":
                        row[num] = letter
                        return None
            else:
                print("Please pick another column, as this one is full")
        else:
            print("Please choose a column that is on the board")

        printing_board()


def consecutive(x: list, letter: str) -> int:
    consecutives = []
    consec = 0
    for i in x:
        if i == letter:
            consec += 1
        else:
            consecutives.append(consec)
            consec = 0
    consecutives.append(consec)
    consecutives.sort()
    return max(consecutives)


def checking():
    check_list = [None] * BOARD_WIDTH

    for row in board[::-1]:
        if consecutive(row, "X") >= 4:
            return "You Win!"
        elif consecutive(row, "O") >= 4:
            return "You Lost!"

    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            check_list[y] = board[y][x]
        if consecutive(check_list, "X") >= 4:
            return "You Win!"
        elif consecutive(check_list, "O") >= 4:
            return "You Lost!"

    check_list = [None] * BOARD_WIDTH

    for x in range(4):
        for y in range(3):
            check_list[y] = board[y][x]
            check_list[y+1] = board[y+1][x+1]
            check_list[y+2] = board[y+2][x+2]
            check_list[y+3] = board[y+3][x+3]
            if consecutive(check_list, "X") >= 4:
                return "You Win!"
            elif consecutive(check_list, "O") >= 4:
                return "You Lost!"

    check_list = [None] * BOARD_WIDTH

    for x in range(4):
        for y in range(3, BOARD_HEIGHT):
            check_list[y] = board[y][x]
            check_list[y-1] = board[y-1][x+1]
            check_list[y-2] = board[y-2][x+2]
            check_list[y-3] = board[y-3][x+3]
            if consecutive(check_list, "X") >= 4:
                return "You Win!"
            elif consecutive(check_list, "O") >= 4:
                return "You Lost!"


def main():
    while True:
        printing_board()

        choosing(": ", "X")
        # checking if anyone won or lost 
        if checking() is not None:
            print(checking())
            break

        printing_board()

        choosing(": ", "O")
        # checking if anyone won or lost 
        if checking() is not None:
            print(checking())
            break

    printing_board()


if __name__ == "__main__":
    main()

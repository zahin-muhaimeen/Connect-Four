import random as rand

board = []

for i in range(6):
    board.append([])

for i in board:
    for j in range(7):
        i.append(" ")


def printing_board():
    for row in board:
        print("|\t", end="")
        print("\t|\t".join(row), end="\t|\n")


def choosing(num: int, letter: str):
    for row in board[::-1]:
        if row[num - 1] == " ":
            row[num - 1] = letter
            break


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


def reset_check_list():
    check_list = []
    for i in range(7):
        check_list.append(None)

    return check_list


def checking():
    check_list = reset_check_list()

    for row in board[::-1]:
        if consecutive(row, "X") >= 4:
            return "You Win!"
        elif consecutive(row, "O") >= 4:
            return "You Lost!"

    for x in range(7):
        for y in range(6):
            check_list[y] = board[y][x]
        if consecutive(check_list, "X") >= 4:
            return "You Win!"
        elif consecutive(check_list, "O") >= 4:
            return "You Lost!"

    check_list = reset_check_list()

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

    check_list = reset_check_list()

    for x in range(4):
        for y in range(3, 6):
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

        # input from player
        in_player = input(": ")
        while ((not in_player.isnumeric())
               or (1 > int(in_player) or int(in_player) > 7)
               or (board[0][int(in_player) - 1] != " ")):
            in_player = input(": ")
        choosing(int(in_player), "X")

        # checking if anyone won or lost 
        if checking() is not None:
            print(checking())
            break

        # input from computer
        in_computer = rand.randint(1, len(board))
        while board[0][in_computer - 1] != " ":
            in_computer = rand.randint(1, len(board))
        choosing(in_computer, "O")

        # checking if anyone won or lost 
        if checking() is not None:
            print(checking())
            break

    printing_board()


if __name__ == "__main__":
    main()

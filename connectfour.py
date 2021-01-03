import random as rand

# Game Constants
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
WINNING_LENGTH = 4

# Initializing the Board
board = []

for i in range(BOARD_HEIGHT):
    board.append([])

for i in board:
    for j in range(BOARD_WIDTH):
        i.append(" ")


# Prints the Board
def printing_board() -> None:
    """
    Prints all the rows in the board that can be looked at without disgust
    """
    for row in board:
        print("|\t", end="")
        print("\t|\t".join(row), end="\t|\n")


# Correct Input
def get_int(prompt: str) -> int:
    """
    Forces the user to enter a numeric string

    :param prompt: The input on the screen.
    :return: The `int` the user was forced to enter.
    """
    user_in = input(prompt)
    while not user_in.isnumeric():
        user_in = input(prompt)
    return int(user_in)


# Positioning
def choosing(prompt: int, letter: str) -> None:
    """
    Forces the user to enter a valid position on the board

    :param prompt: The input on the screen. Used with the `get_int` function.
    :param letter: The `str` that will replace the board position with.
    """
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


# Consecutive
def consecutive(list_str: list, letter: str) -> int:
    """
    Finds the highest consecutive of `letter` in `list_str`

    :param list_str: A list of strings to look through
    :param letter: The item to find the highest consecutive of
    :return: The highest consecutive of `letter` in `list_str`
    """
    consecutives = []
    consec = 0
    for i in list_str:
        if i == letter:
            consec += 1
        else:
            consecutives.append(consec)
            consec = 0
    consecutives.append(consec)
    consecutives.sort()
    return max(consecutives)


# Win or Loss?
def checking():
    """
    Checks if the previous move was a win or a loss for player `X`
    """
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


# The Game
def main():
    """
    The Game of Connect Four
    """
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

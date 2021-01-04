# Game
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
WINNING_LENGTH = 4
turn_count = 0

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
def choosing(prompt: str, letter: str) -> tuple[int, int]:
    """
    Forces the user to enter a valid position on the board

    :param prompt: The input on the screen. Used with the `get_int` function.
    :param letter: The `str` that will replace the board position with.
    :return: Coordinates (`x`, `y`)
    """
    global turn_count

    while True:
        num = get_int(prompt)
        if num in range(BOARD_WIDTH):
            if board[0][num] == " ":
                for index, row in enumerate(board[::-1]):
                    if row[num] == " ":
                        row[num] = letter
                        turn_count += 1
                        return num, BOARD_HEIGHT - 1 - index
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


# Is it on the board?
def on_board(x: int, y: int) -> bool:
    """
    Checks if position x and y are located on the board

    :param x: The `int` for position x
    :param y: The `int` for position y
    :return: Whether or not x and y are available on the board
    """
    if x in range(BOARD_WIDTH) and y in range(BOARD_HEIGHT):
        return True
    return False


# Win or Loss?
def checking(x: int, y: int, letter: int) -> str or None:
    """
    Checks if the previous move was a win or a loss for player `X`

    :param x: The `int` for position x
    :param y: The `int` for position y
    :param letter: The move played by
    :return: If `letter` has won, it returns a `str` stating that.
        If it was a draw, the `str` "Draw!" will be returned.
        Otherwise, nothing will be returned.
    """
    # Check Lists
    cl_row = [None] * BOARD_WIDTH
    cl_col = [None] * BOARD_WIDTH
    cl_pdia = [None] * BOARD_WIDTH
    cl_ndia = [None] * BOARD_WIDTH

    # Starting Positions for Extracting Positions
    starting_x = x - (WINNING_LENGTH - 1)
    starting_y = y + (WINNING_LENGTH - 1)

    # Negative Diagonal Starting Positions
    n_start_x = x + (WINNING_LENGTH - 1)
    n_start_y = y + (WINNING_LENGTH - 1)

    # Extracting Positions to the Check Lists
    for change in range(WINNING_LENGTH * 2 - 1):
        # Row
        if on_board(starting_x + change, y):
            cl_row[change] = board[y][starting_x + change]
        # Column
        if on_board(x, starting_y - change):
            cl_col[change] = board[starting_y - change][x]
        # Positive Diagonal
        if on_board(starting_x + change, starting_y - change):
            cl_pdia[change] = board[starting_y - change][starting_x + change]
        # Negative Diagonal
        if on_board(n_start_x - change, n_start_y - change):
            cl_ndia[change] = board[n_start_y - change][n_start_x - change]

    # Checking If There was any Winning Statements in the Check Lists
    if consecutive(cl_row, letter) >= WINNING_LENGTH:
        return f"{letter} Won!"
    if consecutive(cl_col, letter) >= WINNING_LENGTH:
        return f"{letter} Won!"
    if consecutive(cl_pdia, letter) >= WINNING_LENGTH:
        return f"{letter} Won!"
    if consecutive(cl_ndia, letter) >= WINNING_LENGTH:
        return f"{letter} Won!"
    if turn_count == BOARD_WIDTH * BOARD_HEIGHT:
        return "Draw!"


# The Game
def main() -> None:
    """
    The Game of Connect Four
    """
    while True:
        printing_board()

        coordinates = choosing(": ", "X")
        # checking if anyone won or lost 
        outcome = checking(coordinates[0], coordinates[1], "X")
        if outcome is not None:
            print(outcome)
            break

        printing_board()

        coordinates = choosing(": ", "O")
        # checking if anyone won or lost 
        outcome = checking(coordinates[0], coordinates[1], "O")
        if outcome is not None:
            print(outcome)
            break

    printing_board()


if __name__ == "__main__":
    main()

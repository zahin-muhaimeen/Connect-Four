from tkinter import *
from tkinter import messagebox

# Initialzing TKinter
root = Tk()
root.title("Connect Four")

# Game Constants, Things to keep track
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
WINNING_LENGTH = 4
red_turn = True
turn_count = 0

# Board
board = []

for i in range(BOARD_HEIGHT):
    board.append([])

for y, i in enumerate(board):
    for x in range(BOARD_WIDTH):
        i.append(Label(root, bg="black", width=12, height=6))
        i[x].grid(row=y + 1, column=x)


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


# Consecutive?
def consecutive(colours: list, colour: str) -> int:
    """
    Finds the highest consecutive `str` in `list`

    :param colours: The `list` to look through
    :param colour: The `str` to find the consecutive of in the `list`
    :return: The highest consecutive of `str` in `list`
    """
    high_consec = 0
    consec = 0
    for col in colours:
        if col == colour:
            consec += 1
            if consec > high_consec:
                high_consec = consec
        else:
            consec = 0
    return high_consec


# Win or Loss?
def checking(x: int, y: int, colour: str) -> str or None:
    """
    Checks if the previous move was a win or a loss for player `X`

    :param x: The `int` for position x
    :param y: The `int` for position y
    :param colour: The move played by
    :return: If `letter` has won, it returns a `str` stating that.
        If it was a draw, the `str` "Draw!" will be returned.
        Otherwise, nothing will be returned.
    """
    # Check Lists
    cl_row = [None] * (WINNING_LENGTH * 2 - 1)
    cl_col = [None] * (WINNING_LENGTH * 2 - 1)
    cl_pdia = [None] * (WINNING_LENGTH * 2 - 1)
    cl_ndia = [None] * (WINNING_LENGTH * 2 - 1)

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
            cl_row[change] = board[y][starting_x + change]["bg"]
        # Column
        if on_board(x, starting_y - change):
            cl_col[change] = board[starting_y - change][x]["bg"]
        # Positive Diagonal
        if on_board(starting_x + change, starting_y - change):
            cl_pdia[change] = board[starting_y - change][starting_x + change]["bg"]
        # Negative Diagonal
        if on_board(n_start_x - change, n_start_y - change):
            cl_ndia[change] = board[n_start_y - change][n_start_x - change]["bg"]

    # Checking If There was any Winning Statements in the Check Lists
    if consecutive(cl_row, colour) >= WINNING_LENGTH:
        return f"{colour} Won!"
    if consecutive(cl_col, colour) >= WINNING_LENGTH:
        return f"{colour} Won!"
    if consecutive(cl_pdia, colour) >= WINNING_LENGTH:
        return f"{colour} Won!"
    if consecutive(cl_ndia, colour) >= WINNING_LENGTH:
        return f"{colour} Won!"
    if turn_count == BOARD_HEIGHT * BOARD_WIDTH:
        return "Draw!"


# Reset
def game_reset():
    """
    Resets all things used variables used in the game
    """
    global red_turn, turn_count

    red_turn = True
    turn_count = 0
    for row in board:
        for lab in row:
            lab["bg"] = "black"


# Button Functionality
def button_click(button: Button) -> None:
    """
    Allows Tic Tac Toe button functionaly when it is pressed
    This is technecially the `main` function but is runned
    everytime the player presses a button.

    :param button: The button pressed
    """
    global red_turn, turn_count

    button_coordinates = button.grid_info()
    button_x = int(button_coordinates["column"])

    if board[0][button_x]["bg"] == "black":
        for y, row in enumerate(board[::-1]):
            if row[button_x]["bg"] == "black":
                if red_turn:
                    row[button_x]["bg"] = "red"
                    red_turn = False
                    turn_count += 1
                    outcome = checking(button_x, BOARD_HEIGHT - 1 - y, "red")
                    if outcome is not None:
                        messagebox.showinfo("Connect Four", outcome)
                        game_reset()
                    break
                else:
                    row[button_x]["bg"] = "blue"
                    red_turn = True
                    turn_count += 1
                    outcome = checking(button_x, BOARD_HEIGHT - 1 - y, "blue")
                    if outcome is not None:
                        messagebox.showinfo("Connect Four", outcome)
                        game_reset()
                    break
    else:
        messagebox.showerror("Connect Four", "This Column is Full!"
                                             " Please choose a another Column")


# Buttons
b1 = Button(root, text="1", width=12, height=6, command=lambda: button_click(b1))
b2 = Button(root, text="2", width=12, height=6, command=lambda: button_click(b2))
b3 = Button(root, text="3", width=12, height=6, command=lambda: button_click(b3))
b4 = Button(root, text="4", width=12, height=6, command=lambda: button_click(b4))
b5 = Button(root, text="5", width=12, height=6, command=lambda: button_click(b5))
b6 = Button(root, text="6", width=12, height=6, command=lambda: button_click(b6))
b7 = Button(root, text="7", width=12, height=6, command=lambda: button_click(b7))
buttons = [b1, b2, b3, b4, b5, b6, b7]

for column, but in enumerate(buttons):
    but.grid(row=0, column=column)

root.mainloop()

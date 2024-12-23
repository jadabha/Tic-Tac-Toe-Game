import tkinter

def set_tile(row, column):
    global curr_player, game_over

    if board[row][column]["text"] != "" or game_over:
        return

    board[row][column]["text"] = curr_player

    # Alternate player turns
    if curr_player == playerO:
        curr_player = playerX
    else:
        curr_player = playerO

    label["text"] = curr_player + "'s turn"
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    # Check rows
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
                and board[row][0]["text"] != ""):
            declare_winner(board[row][0]["text"])
            return

    # Check columns
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
                and board[0][column]["text"] != ""):
            declare_winner(board[0][column]["text"])
            return

    # Check diagonals
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
            and board[0][0]["text"] != ""):
        declare_winner(board[0][0]["text"])
        return

    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
            and board[0][2]["text"] != ""):
        declare_winner(board[0][2]["text"])
        return

    # Check for draw
    if turns == 9:
        label.config(text="It's a draw!", foreground="white")
        game_over = True

def declare_winner(player):
    global game_over
    label.config(text=player + " is the winner!", foreground=color_yellow)
    for row in board:
        for button in row:
            button.config(foreground=color_yellow, background=color_gray)
    game_over = True

def new_game():
    global turns, game_over, curr_player
    turns = 0
    game_over = False
    curr_player = playerX
    label.config(text=curr_player + "'s turn", foreground="white")
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", background=color_gray, foreground=color_blue)

# Game variables
playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"

turns = 0
game_over = False

# Create the main window
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

# Create a frame for the game
frame = tkinter.Frame(window)
frame.pack()

# Label for status
label = tkinter.Label(frame, text=curr_player + "'s turn", font=("Consolas", 20),
                      background=color_gray, foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

# Create the game board
for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background=color_gray, foreground=color_blue,
                                            width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row + 1, column=column)

# Restart button
button = tkinter.Button(frame, text="Restart", font=("Consolas", 20),
                        background=color_gray, foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")

# Run the game loop
window.mainloop()

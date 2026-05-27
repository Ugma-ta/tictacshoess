import tkinter as tk
from tkinter import messagebox

# Create window
root = tk.Tk()
root.title(" XO Game")
root.geometry("300x350")

# Variables
current_player = "X"
board = [""] * 9

# Check winner
def check_winner():
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]

    for combo in win_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c] != "":
            return board[a]

    if "" not in board:
        return "Tie"

    return None

# Button click
def button_click(index):
    global current_player

    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player)

        winner = check_winner()

        if winner == "X" or winner == "O":
            messagebox.showinfo("Winner", f"Player {winner} wins!")
            reset_game()

        elif winner == "Tie":
            messagebox.showinfo("Tie", "It's a tie!")
            reset_game()

        else:
            current_player = "O" if current_player == "X" else "X"

# Reset game
def reset_game():
    global current_player, board

    current_player = "X"
    board = [""] * 9

    for button in buttons:
        button.config(text="")

# Create buttons
buttons = []

for i in range(9):
    button = tk.Button(
        root,
        text="",
        font=("Arial", 24),
        width=5,
        height=2,
        command=lambda i=i: button_click(i)
    )

    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Reset button
reset_btn = tk.Button(
    root,
    text="Reset Game",
    font=("Arial", 14),
    command=reset_game
)

reset_btn.grid(row=3, column=0, columnspan=3, pady=20)

# Run app
root.mainloop()
tk.tk
from tkinter import Tk, Button, messagebox, font
from random import choice

class TicTacToe:
    def __init__(self):
        self.window = Tk()
        self.window.title("Tic Tac Toe")
        self.window.configure(bg="#2c3e50")

        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[Button(self.window, width=8, height=4, font=font.Font(family="Arial", size=20, weight="bold"), bg="#34495e", fg="#ffffff", command=lambda i=i, j=j: self.make_move(i, j)) for j in range(3)] for i in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

        self.current_player = choice(["X", "O"])

        if self.current_player == "O":
            self.computer_move()

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = "X"
            self.buttons[row][col].config(text="X", state="disabled", bg="#2980b9")
            if self.check_winner("X"):
                self.end_game("X wins!")
            elif self.is_board_full():
                self.end_game("It's a tie!")
            else:
                self.computer_move()

    def computer_move(self):
        best_score = -float("inf")
        best_move = None

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = "O"
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = ""

                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        row, col = best_move
        self.board[row][col] = "O"
        self.buttons[row][col].config(text="O", state="disabled", bg="#e74c3c")

        if self.check_winner("O"):
            self.end_game("O wins!")
        elif self.is_board_full():
            self.end_game("It's a tie!")

    def minimax(self, board, depth, is_maximizing):
        scores = {
            "X": -1,
            "O": 1,
            "tie": 0
        }

        if self.check_winner("X"):
            return scores["X"]
        elif self.check_winner("O"):
            return scores["O"]
        elif self.is_board_full():
            return scores["tie"]

        if is_maximizing:
            best_score = -float("inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "O"
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = ""
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "X"
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = ""
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            if "" in row:
                return False
        return True

    def end_game(self, message):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state="disabled")

        messagebox.showinfo("Game Over", message)
        self.window.destroy()


if __name__ == "__main__":
    game = TicTacToe()
    game.window.mainloop()
    
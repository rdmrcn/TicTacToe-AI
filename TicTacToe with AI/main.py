import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.master.configure(bg='lightblue')
        self.master.geometry('400x450')
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.master, text=' ', font=('Arial', 36), width=5, height=2, bg='white',
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)
        self.restart_button = tk.Button(self.master, text='Restart', font=('Arial', 16), bg='lightgreen',
                                        command=self.restart_game)
        self.restart_button.grid(row=3, column=0, columnspan=3, pady=10)

    def on_click(self, row, col):
        if self.board[row * 3 + col] == ' ' and self.current_winner is None:
            self.board[row * 3 + col] = 'X'
            self.update_buttons()
            if self.check_winner('X'):
                self.current_winner = 'X'
                messagebox.showinfo("Tic-Tac-Toe", "You win!")
                return
            if ' ' not in self.board:
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                return
            self.ai_move()
            self.update_buttons()
            if self.check_winner('O'):
                self.current_winner = 'O'
                messagebox.showinfo("Tic-Tac-Toe", "AI wins!")
            elif ' ' not in self.board:
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")

    def ai_move(self):
        best_score = -float('inf')
        best_move = None
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                score = self.minimax(self.board, 0, False)
                self.board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i
        self.board[best_move] = 'O'

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner('O'):
            return 1
        elif self.check_winner('X'):
            return -1
        elif ' ' not in board:
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'O'
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ' '
                    best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'X'
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ' '
                    best_score = min(best_score, score)
            return best_score

    def check_winner(self, player):
        win_conditions = [
            [self.board[0], self.board[1], self.board[2]],
            [self.board[3], self.board[4], self.board[5]],
            [self.board[6], self.board[7], self.board[8]],
            [self.board[0], self.board[3], self.board[6]],
            [self.board[1], self.board[4], self.board[7]],
            [self.board[2], self.board[5], self.board[8]],
            [self.board[0], self.board[4], self.board[8]],
            [self.board[2], self.board[4], self.board[6]],
        ]
        return [player, player, player] in win_conditions

    def update_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=self.board[i * 3 + j])
                if self.board[i * 3 + j] == 'X':
                    self.buttons[i][j].config(fg='blue')
                elif self.board[i * 3 + j] == 'O':
                    self.buttons[i][j].config(fg='red')

    def restart_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        self.update_buttons()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

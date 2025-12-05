import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None  # keep track of the winner!

    def print_board(self):
        # we will print the board after every move
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |
')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter  # assign winner
            return True
        return False

    def winner(self, square, letter):
        # check the rows, columns and diagonals
        row_ind = square // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        col = [self.board[i] for i in range(square % 3, 9, 3)]
        if all([spot == letter for spot in col]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

    def play_game(self):
        letter = 'X'  # starting letter
        while self.empty_squares():
            if self.current_winner:
                print(f'{letter} wins!')
                return
            if letter == 'X':
                square = int(input(f'{letter} turn. Input move (0-8): '))
            else:
                square = random.choice(self.available_moves())  # random move for computer
            if self.make_move(square, letter):
                self.print_board()
                letter = 'O' if letter == 'X' else 'X'  # switch letter
        print('It’s a tie!')

if __name__ == '__main__':
    game = TicTacToe()
    game.play_game()
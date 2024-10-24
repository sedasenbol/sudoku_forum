# sudoku_generator.py

import random

class SudokuGenerator:
    def __init__(self, size=9, subgrid_size=3):
        self.size = size
        self.subgrid_size = subgrid_size

    def generate(self, num_remove=50):
        board = self._generate_full_board()
        self._remove_numbers(board, num_remove)
        return board

    def _generate_full_board(self):
        board = [[0] * self.size for _ in range(self.size)]
        self._fill_values(board)
        return board

    def _fill_values(self, board):
        for i in range(self.size):
            for j in range(self.size):
                if board[i][j] == 0:
                    numbers = list(range(1, self.size + 1))
                    random.shuffle(numbers)
                    for number in numbers:
                        if self._is_safe(board, i, j, number):
                            board[i][j] = number
                            if self._fill_values(board):
                                return True
                            board[i][j] = 0  # backtrack
                    return False
        return True

    def _is_safe(self, board, row, col, number):
        for x in range(self.size):
            if board[row][x] == number or board[x][col] == number:
                return False

        start_row = row - row % self.subgrid_size
        start_col = col - col % self.subgrid_size
        for i in range(self.subgrid_size):
            for j in range(self.subgrid_size):
                if board[i + start_row][j + start_col] == number:
                    return False
        return True

    def _remove_numbers(self, board, num_remove):
        count = num_remove
        while count != 0:
            i = random.randint(0, self.size - 1)
            j = random.randint(0, self.size - 1)
            if board[i][j] != 0:
                board[i][j] = 0
                count -= 1

class Solution:
    col_size = 9  # len(self.board)
    row_size = 9  # len(self.board[0])
    block_col_size = 3
    block_row_size = 3
    digits = '123456789'
    empty_symbol = '.'

    # def solveSudoku(self, board: List[List[str]]) -> None:
    def solveSudoku(self, board):
        self.init(board)
        self.solve()

    def init(self, board):
        self.board = board

        # list all empty cells. a `cell` is a tuple `(row_index, col_index)`
        self.empty_cells = set([(ri, ci) for ri in range(self.row_size) for ci in range(self.col_size) if self.board[ri][ci] == self.empty_symbol])

        # find candidates of each cell
        self.candidates = [[set(self.digits) for ci in range(self.col_size)] for ri in range(self.row_size)]
        for ri in range(self.row_size):
            for ci in range(self.col_size):
                digit = self.board[ri][ci]
                if digit != self.empty_symbol:
                    self.candidates[ri][ci] = set()
                    self.update_candidates((ri, ci), digit)

    def solve(self):
        # if there are no empty cells, it's solved
        if not self.empty_cells:
            return True

        # get the cell with fewest candidates
        cell = min(self.empty_cells, key=lambda cell: len(self.candidates[cell[0]][cell[1]]))

        # try filling the cell with one of the candidates, and solve recursively
        ri, ci = cell
        for digit in list(self.candidates[ri][ci]):
            candidate_updated_cells = self.fill_cell(cell, digit)
            solved = self.solve()
            if solved:
                return True
            self.unfill_cell(cell, digit, candidate_updated_cells)

        # if no solution found, go back and try the next candidates
        return False

    def fill_cell(self, cell, digit):
        # fill the cell with the digit
        ri, ci = cell
        self.board[ri][ci] = digit

        # remove the cell from empty_cells
        self.empty_cells.remove(cell)

        # update the candidates of other cells
        # keep a list of updated cells. will be used when unfilling cells
        candidate_updated_cells = self.update_candidates(cell, digit)

        return candidate_updated_cells

    def unfill_cell(self, cell, digit, candidate_updated_cells):
        # unfill cell
        ri, ci = cell
        self.board[ri][ci] = self.empty_symbol

        # add the cell back to empty_cells
        self.empty_cells.add(cell)

        # add back candidates of other cells
        for ri, ci in candidate_updated_cells:
            self.candidates[ri][ci].add(digit)

    def update_candidates(self, filled_cell, digit):
        candidate_updated_cells = []
        for ri, ci in self.related_cells(filled_cell):
            if (self.board[ri][ci] == self.empty_symbol) and (digit in self.candidates[ri][ci]):
                self.candidates[ri][ci].remove(digit)
                candidate_updated_cells.append((ri, ci))
        return candidate_updated_cells

    def related_cells(self, cell):
        return list(set(self.cells_in_same_row(cell) + self.cells_in_same_col(cell) + self.cells_in_same_block(cell)))

    def cells_in_same_row(self, cell):
        return [(cell[0], ci) for ci in range(self.col_size)]

    def cells_in_same_col(self, cell):
        return [(ri, cell[1]) for ri in range(self.row_size)]

    def cells_in_same_block(self, cell):
        block_first_cell_ri = (cell[0] // self.block_row_size) * self.block_row_size
        block_first_cell_ci = (cell[1] // self.block_col_size) * self.block_col_size
        return [
            (block_first_cell_ri + in_block_ri, block_first_cell_ci + in_block_ci)
            for in_block_ri in range(self.block_row_size)
            for in_block_ci in range(self.block_col_size)
        ]

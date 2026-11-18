from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colums = defaultdict(set)
        grid_sections = defaultdict(set)
        row, colum = 0, 0

        for row in range(len(board)):
            current_colum = set()

            for colum in range(len(board)):
                
                if board[row][colum] != ".":
                    section = (row // 3, colum // 3)
                    c_val = board[row][colum]

                    if c_val in current_colum or c_val in colums[colum] or c_val in grid_sections[section]:
                        return False

                    current_colum.add(c_val)
                    colums[colum].add(c_val)
                    grid_sections[section].add(c_val)

        return True
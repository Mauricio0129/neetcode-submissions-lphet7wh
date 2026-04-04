class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        x, y = 0, 0

        colums = [set () for i in range(len(board))]
        sub_boxes = {}
        current_row = set()
        
        while y < len(board):
             
            while x < len(board[y]):
                if board[y][x] != ".":
                    if board[y][x] in current_row or board[y][x] in colums[x]:
                        return False
                    current_row.add(board[y][x])

                    colums[x].add(board[y][x])
                    key = (x // 3,  y // 3)
                    if key not in sub_boxes:
                        sub_boxes[key] = set(board[y][x])
                    elif key in sub_boxes and board[y][x] not in sub_boxes[key]:
                        sub_boxes[key].add(board[y][x])
                    else:
                        return False
                x += 1

            current_row = set()
            x = 0 
            y += 1
        return True 
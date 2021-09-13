# 36. Valid Sudoku

# 96 ms solution
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        new = set()
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != '.':
                    ele = board[i][j]
                    if (i, ele) in new or (ele, j) in new or (i//3, j//3, ele) in new:
                        return False
                    new.add((i, ele))
                    new.add((ele, j))
                    new.add((i//3, j//3, ele))

        return True


# # sample 72 ms submission
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#
#         row = [set() for _ in board]
#         column = [set() for _ in board]
#         square = [set() for _ in board]
#
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#
#                 if board[i][j] == '.':
#                     continue
#
#                 if board[i][j] in row[i]:
#                     return False
#                 row[i].add(board[i][j])
#
#                 if board[i][j] in column[j]:
#                     return False
#                 column[j].add(board[i][j])
#
#                 curr_row = i // 3
#                 curr = curr_row * 3 + j // 3
#
#                 if board[i][j] in square[curr]:
#                     return False
#                 square[curr].add(board[i][j])
#         return True

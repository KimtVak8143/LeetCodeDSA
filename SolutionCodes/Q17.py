# 240. Search a 2D Matrix II

# 250 ms
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        i = 0
        j = cols - 1
        while i < rows and j >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False


# # sample 140 ms submission
# class Solution:
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         if len(matrix) == 0 or len(matrix[0]) == 0:
#             return False
#
#         row = -1
#
#         for i in range(len(matrix)):
#             if matrix[i][0] == target:
#                 return True
#             if matrix[i][0] > target:
#                 row = i
#                 break
#         if row == -1:
#             row = len(matrix) - 1
#
#         col = 1
#         while row >= 0 and col < len(matrix[row]):
#             if matrix[row][col] == target:
#                 return True
#             if matrix[row][col] > target:
#                 row -= 1
#             else:
#                 col += 1
#         return False

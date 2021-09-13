# 74. Search a 2D matrix
# 44ms solution
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


#
# # sample 20 ms submission
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         if not matrix or len(matrix[0]) == 0:
#             return False
#         m, n = len(matrix), len(matrix[0])
#         left, right =  0, m*n-1
#         while left <= right:
#             mid = (left + right)//2
#             r, c = mid // n, mid % n
#             if matrix[r][c] == target:
#                 return True
#             elif matrix[r][c] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return False

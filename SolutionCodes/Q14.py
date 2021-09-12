# 566. Reshape the Matrix

# 88 ms solution
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        new = []
        temp = []

        for i in mat:
            for j in i:
                temp.append(j)

        if len(temp) != r * c:
            return mat
        else:
            for k in range(0, len(temp), c):
                new.append(temp[k:k + c])
            return new



# # sample 72 ms submission
# class Solution:
#     def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
#         m = len(mat) # number of rows
#         n = len(mat[0]) # number of columns
#         newMat = [[None]*c]
#         for i in range(r-1):
#             newMat.append([None]*c)
#         if m*n != r*c:
#             newMat = mat
#         else:
#             k = 0 # row ind
#             l = 0 # col ind
#             for i in range(m):
#                 for j in range(n):
#                     if l < c:
#                         newMat[k][l] = mat[i][j]
#                         l+=1
#                     else:
#                         l=0
#                         k+=1
#                         newMat[k][l] = mat[i][j]
#                         l+=1
#         return newMat

# 118. Pascal's Triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(1, numRows):
            res += [list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1]))]

        return res[:numRows]


# # sample 12 ms submission

# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#
#         dp = [[1]]
#         for i in range(numRow s -1):
#             temp = [1]
#             for j in range(len(dp[i] ) -1):
#                 temp.append(dp[i][j ] +dp[i][ j +1])
#             temp.append(1)
#             dp.append(temp)
#
#         return (dp)

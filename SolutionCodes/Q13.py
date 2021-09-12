# 119. Pascal's Triangle II

# 42 ms solution
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]

        for i in range(1, rowIndex + 1):
            res += [list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1]))]

        return res[rowIndex]


# # sample 12 ms submission
# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         last = [1]
#         res = [1]
#         for r in range(1, rowIndex+1):
#             res = [1]
#             for index in range(len(last)-1):
#                 res.append(last[index] + last[index+1])
#             res.append(1)
#             last = res
#         return res

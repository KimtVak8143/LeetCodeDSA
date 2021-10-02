# 1252. Cells with Odd Values in a Matrix

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        d1 = [0] * m
        d2 = [0] * n

        for r, c in indices:
            d1[r] += 1
            d2[c] += 1

        return sum([(r + c) % 2 for r in d1 for c in d2])

# sample 24 ms submission
# class Solution:
#     def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
#         d = {"r":defaultdict(lambda : 0),"c":defaultdict(lambda : 0)}
#         for i,j in indices:
#             d["r"][i]+=1
#             d["c"][j]+=1
#         c=0
#         for i in range(m):
#             for j in range(n):
#                 c = c+1 if (d["r"][i]+d["c"][j])%2!=0 else c
#         return c

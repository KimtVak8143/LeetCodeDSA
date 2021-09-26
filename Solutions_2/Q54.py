# 1528. Shuffle String

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res =['']*len(s)
        for i in range(0,len(s)):
            res[indices[i]]=s[i]
        return "".join(res)


# sample 36 ms submission
# class Solution:
#     def restoreString(self, s: str, indices: List[int]) -> str:
#         ans = ['' for i in range(len(s))]
#         for a,b in zip(s,indices):
#             ans[b] = a
#         return ''.join(ans)


# sample 42 ms submission
# class Solution:
#     def restoreString(self, s: str, indices: List[int]) -> str:
#         splittedString = list(s)
#         newString = list(range(0,len(indices)))
#         counter = 0
#         for ind in indices:
#             newString[ind]=s[counter]
#             counter += 1
#         return "".join(newString)

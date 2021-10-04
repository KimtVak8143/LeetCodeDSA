# 14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return -1

        new = min(strs, key=len)

        for x, y in enumerate(new):
            for z in strs:
                if z[x] != y:
                    return new[:x]
        return new


# sample 12 ms submission
#
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#         if len(strs) == 1: return strs[0]
#
#         strs.sort()
#         p = ""
#         for x, y in zip(strs[0], strs[-1]):
#             if x == y:
#                 p += x
#             else:
#                 break
#         return p

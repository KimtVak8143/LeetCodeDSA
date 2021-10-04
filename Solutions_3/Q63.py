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

# sample 16 ms submission

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#
#         # initialize the longest prefix
#         prefix = strs[0]
#
#         # loop through remaining string
#         for string in strs[1:]:
#
#             # if the current string is shorter than the prefix, swap the current prefix with the string
#             if len(string) < len(prefix):
#                 temp = string
#                 string = prefix
#                 prefix = temp
#
#             # compare the prefix with the string until an unequality and then cut the prefix and break out
#             for i in range(len(prefix)):
#                 if prefix[i] != string[i]:
#                     if i > 0:
#                         prefix = prefix[0:i]  # cut prefix
#                         break
#                     else:
#                         return ""  # if the very first character does not match, then there is no common prefix
#         return prefix


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

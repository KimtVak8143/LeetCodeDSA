# 242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for x in set(s):
            if s.count(x) != t.count(x):
                return False
        return True


# sample 20 ms submission
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         map1=collections.Counter(s)
#         map2=collections.Counter(t)
#         return map1==map2


# sample 44 ms submission
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         chDict = {}
#         for ch in s:
#             if ch not in chDict:
#                 chDict[ch] = 1
#             else:
#                 chDict[ch] += 1
#
#         for ch in t:
#             if ch not in chDict:
#                 return False
#
#             if ch in chDict:
#                 chDict[ch] -= 1
#
#         for val in chDict.values():
#             if val != 0:
#                 return False
#         return True

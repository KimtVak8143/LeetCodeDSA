# 1662. Check If Two String Arrays are Equivalent

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        c1, c2 = "", ""
        for i in word1:
            c1 = c1 + i

        for j in word2:
            c2 = c2 + j

        return c1 == c2


# sample 12 ms submission
# class Solution:
#     def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
#         str1 = ''.join(word1)
#         str2 = ''.join(word2)
#         if str1 == str2:
#             return True
#         else:
#             return False

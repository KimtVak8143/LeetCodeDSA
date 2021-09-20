# 389. Find the Difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        str1 = list(s)
        str2 = list(t)
        new = {}
        for i in str1:
            new[i] = new.get(i, 0) + 1

        for j in str2:
            if new.get(j, 0) == 0:
                return j
            else:
                new[j] -= 1


# # sample 16 ms submission
#
# class Solution:
#
#     # O(n) time / O(1) space or memory
#     # where n is the length of both strings
#     def findTheDifference(self, s: str, t: str) -> str:
#         # Idea: Use an integer to store the ASCII value of each character in t
#         # then iterate in s and subtract the ASCII value of each character encountered
#         # the remaining value will be the ASCII value of the letter added to t
#
#         ascii_code = 0
#
#         for num in t:
#             ascii_code += ord(num)
#
#         for num in s:
#             ascii_code -= ord(num)
#
#         return chr(ascii_code)

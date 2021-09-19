# 12. Integer to Roman

class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        chars = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        final = ""
        i = 0

        while num:
            final += (num // nums[i]) * chars[i]
            num %= nums[i]
            i += 1
        return final


# # sample 24 ms submission
#
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         s = ""
#         m = [(1000, "M"), (900, "CM"),(500, "D"), (400, "CD"),(100, "C"), (90, "XC"), (50, "L"),
#         (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
#
#         for val, symbol in m:
#             while num >= val:
#                 num -= val
#                 s += symbol
#
#         return s

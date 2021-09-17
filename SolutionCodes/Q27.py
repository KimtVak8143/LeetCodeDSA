# 258. Add Digits

class Solution:
    def addDigits(self, num: int) -> int:
        new = 0
        while num > 9:
            new = num % 10
            num = num // 10
            num = new

        return num

# # sample 16 ms submission

# class Solution:
#     def addDigits(self, num: int) -> int:
#         while num > 9:
#             temp = 0
#             while num > 0:
#                 temp += num % 10
#                 num = num // 10
#             num = temp
#         return num

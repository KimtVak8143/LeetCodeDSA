# 9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        new = str(x)
        if x == int(new[::-1]):
            return True
        else:
            return False


# # sample 36 ms submission
#
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         elif x < 10:
#             return True
#         else:
#             rev = 0
#             dig = x
#             while (x != 0):
#                 rem = x % 10
#                 rev = (rev * 10) + rem
#                 x = x // 10
#             if rev == dig:
#                 return True
#             else:
#                 return False

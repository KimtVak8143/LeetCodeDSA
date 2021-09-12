# 7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        if x < 0:
            n = x*-1
            while n > 0:
                rem = n % 10
                rev = rev*10+rem
                n = n//10
            rev = rev*-1
        else:
            while x > 0:
                rem = x % 10
                rev = rev*10+rem
                x = x//10
        if rev >= 2**31-1 or rev <= -2**31:
            return 0
        else:
            return rev


# sample 8 ms submission
#
# class Solution:
#     def reverse(self, x: int) -> int:
#         strX = str(x)
#         signed = False
#
#         if '-' in strX:
#             signed = True
#             strX = strX[1:]
#
#         lenX = len(strX)
#
#         revNum = 0
#         for i in reversed(range(lenX)):
#             revNum += (int(strX[i]) * pow(10, i))
#
#         if signed:
#             revNum = -revNum
#
#         if ((revNum > 2147483647) or (revNum < -2147483648)):
#             return 0
#
#         return revNum


# sample 32 ms submission
#
# class Solution:
#     def reverse(self, x: int) -> int:
#         if x>0:
#             rev = int(str(x)[::-1])
#             if rev <= 2**31-1:
#                 return int(str(x)[::-1])
#             else:
#                 return 0
#         elif x<0:
#             rev = int('-'+str(x)[1:][::-1])
#             if rev >= -2**31:
#                 return int('-'+str(x)[1:][::-1])
#             else:
#                 return 0
#         else:
#             return 0

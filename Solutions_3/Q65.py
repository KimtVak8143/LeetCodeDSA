# 415. Add Strings

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        new = int(num1)+int(num2)
        return str(new)


# sample 12 ms submission
# class Solution:
#     def addStrings(self, num1: str, num2: str) -> str:
#         a=num1
#         b=num2
#         c=int(a)+int(b)
#         return str(c)

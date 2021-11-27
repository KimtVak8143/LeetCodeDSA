# 326. Power of Three

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        d = int(log2(n)/log2(3))
        return pow(3, d) == n

# # sample 48 ms submission
# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         if n <= 0:
#             return False
#         while n > 1:
#             if n % 3 == 0:
#                 n = n/3
#             else:
#                 return False
#         return True
#
# # sample 40 ms submission
#
# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         return n > 0 and 3**20 % n == 0

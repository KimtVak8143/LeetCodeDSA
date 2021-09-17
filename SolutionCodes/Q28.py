# 202. Happy Number

# 57 ms solution
class Solution:
    def isHappy(self, n: int) -> bool:
        new = set()
        while n != 1:
            n = sum(int(i) ** 2 for i in str(n))
            if n in new:
                return False
            else:
                new.add(n)
        else:
            return True


#         def calc(n):
#             sum = 0
#             while n>0:
#                 n,dig = divmod(n,10)
#                 sum+=dig**2
#             return sum

#         new = set()
#         while n!=1 and n not in new:
#             new.add(n)
#             n = calc(n)
#         return n==1


# # sample 12 ms submission
#     def isHappy(self, n: int) -> bool:
#         past_n = set()
#
#         while n not in past_n:
#             if n == 1:
#                 return True
#
#             past_n.add(n)
#             total = 0
#
#             while n > 0:
#                 total += (n % 10) ** 2
#                 n //= 10
#             n = total
#         return False

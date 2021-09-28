# 1688. Count of Matches in Tournament


class Solution:
    def numberOfMatches(self, n: int) -> int:
        totalmatches = 0
        while n!=1:
            if n%2==0:
                totalmatches+=n//2
                n=n//2
            else:
                totalmatches+=(n-1)//2
                n = (n-1)//2 +1
        return totalmatches


# sample 12 ms submission
# class Solution:
#     def numberOfMatches(self, n: int) -> int:
#         total=0
#         while n>1:
#             total+=(n//2)
#             n=(n//2)+(n%2)
#         return total

# 1431. Kids With the Greatest Number of Candies

# 40 ms solution
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        new = []
        maxum = max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies >=maxum:
                new.append(True)
            else:
                new.append(False)
        return new


# # sample 20 ms submission
#
# class Solution:
#     def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
#         max_number = max(candies)
#         ans = [True for _ in range(len(candies))]
#
#         for i in range(len(candies)):
#             if candies[i] + extraCandies < max_number:
#                 ans[i] = False
#
#         return ans

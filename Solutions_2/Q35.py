# 287. Find the Duplicate Number

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        new = {}
        for i in nums:
            try:
                new[i] += 1
            except:
                new[i] = 1
        for j in new:
            if new[j] > 1:
                return j


# # sample 544 ms submission
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         dict = {}
#
#         for i, n in enumerate(nums):
#             if n in dict:
#                 return(n)
#             else:
#                 dict[n] = i

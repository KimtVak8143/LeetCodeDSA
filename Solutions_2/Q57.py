# 2006. Count Number of Pairs With Absolute Difference K

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if abs(nums[i]-nums[j])==k and i!=j:
                    count+=1
        return count//2


# sample 51 ms submission
# from collections import defaultdict
# class Solution:
#     def countKDifference(self, nums: List[int], k: int) -> int:
#         new = defaultdict(int)
#         for i in nums:
#             new[i] += 1
#         pairs = 0
#         for j in set(new):
#             if j + k in new:
#                 pairs += new[j] * new[j + k]
#
#         return pairs

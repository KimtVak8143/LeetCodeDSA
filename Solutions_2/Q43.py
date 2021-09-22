# 1920. Build Array from Permutation

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        new = []
        for i in nums:
            new.append(nums[i])

        return new


# sample 100 ms submission

# class Solution:
#     def buildArray(self, nums: List[int]) -> List[int]:
#         ans= [0]*len(nums)
#         for i,j in enumerate(nums):
#             ans[i] = nums[nums[i]]
#         return ans

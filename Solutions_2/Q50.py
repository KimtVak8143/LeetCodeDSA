# 1913. Maximum Product Difference Between Two Pairs

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        maxum1 = max(nums)
        nums.remove(maxum1)
        minum1 = min(nums)
        nums.remove(minum1)
        maxum2 = max(nums)
        minum2 = min(nums)
        return maxum1*maxum2 - minum1*minum2


# sample 148 ms submission

# class Solution:
#     def maxProductDifference(self, nums: List[int]) -> int:
#         nums.sort()
#         ans = nums[-1]*nums[-2]-nums[0]*nums[1]
#         return ans

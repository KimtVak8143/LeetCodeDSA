# 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        maxum = nums[0]

        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            maxum = max(maxum, current)

        return maxum

# 1480. Running Sum of 1d Array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        new = []
        for i in nums:
            sum += i
            new.append(sum)

        return new


# # sample 18 ms submission
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         for i in range(1, len(nums)):
#             nums[i] += nums[i-1]
#         return nums

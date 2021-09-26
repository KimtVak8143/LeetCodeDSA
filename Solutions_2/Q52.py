# 169. Majority Element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]


# sample 136 ms submission
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         return sorted(nums)[len(nums) // 2]

# sample 150 ms submission
# Using count/collection method
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count = collections.Counter(nums)
#         ls = sorted(count.items(), key=lambda x: (-x[1]))
#         return ls[0][0]

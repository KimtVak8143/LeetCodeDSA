# 137. Single Number II

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        new = {}
        if len(nums) < 2:
            return nums[0]

        for x in nums:
            try:
                new[x] += 1
            except:
                new[x] = 1
        for i in new:
            if new[i] < 3:
                return i

# 260. Single Number III
# 56ms solution
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        new = {}
        if len(nums) < 2:
            return nums[0]
        res = []
        for x in nums:
            try:
                new[x] += 1
            except:
                new[x] = 1
        for i in new:
            if new[i] < 2:
                res.append(i)

        return res


# # sample 48 ms submission
# class Solution:
#     from collections import Counter
#     def singleNumber(self, nums: List[int]) -> List[int]:
#         c = Counter(nums)
#         return [x for x in c if c[x] == 1]

# 136. Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
        return res


#         new = {}
#         if len(nums)<2:
#             return nums[0]

#         for x in nums:
#             try:
#                 new[x]+=1
#             except:
#                 new[x]=1
#         for i in new:
#             if new[i]<2:
#                 return i

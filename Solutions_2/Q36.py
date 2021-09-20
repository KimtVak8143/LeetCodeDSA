# 645. Set Mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l = len(nums)
        new = {}
        sum = 0
        flag = []
        target = 0
        for i in nums:
            try:
                new[i] += 1
                sum += i
            except:
                new[i] = 1
                sum += i

        target = int((l * (l + 1)) / 2)

        for k in new:
            if new[k] > 1:
                x = k
                flag.append(k)

        diff = int(target) - sum + x
        flag.append(diff)
        return flag

# # sample 160 ms submission
# class Solution(object):
#     def findErrorNums(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         n = len(nums)
#         s = n*(n+1)//2
#         miss = s - sum(set(nums))
#         duplicate = sum(nums) + miss - s
#         return [duplicate, miss]

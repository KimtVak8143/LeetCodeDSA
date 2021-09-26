# 1512. Number of Good Pairs

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]==nums[j] and i<j:
                    count+=1
        return count
        # new = {}
        # count=0
        # for i in nums:
        #     try:
        #         new[i]+=1
        #     except:
        #         new[i]=1
        # for j in new:
        #     freq = new[j]
        #     for x in range(freq):
        #         count+=x
        # return count


# sample 12 ms submission
#
# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         ans = 0
#         seen = {}
#         # count of each number and for each num, number of pairs can be formed is n(n-1)/2
#         for i in nums:
#             seen[i] = seen[i] + 1 if i in seen else 1
#
#         for i in seen:
#             ans += (seen[i] * (seen[i] - 1)) // 2
#         return ans

# 75. Sort Colors

# 36 ms solution
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        new = {0: 0, 1: 0, 2: 0}
        for i in nums:
            try:
                new[i] += 1
            except:
                new[i] = 1
        nums.clear()
        for x in new:
            v = new[x]
            for j in range(v):
                nums.append(x)

# 44 ms solution
# def sortColors(self, nums):
#     i = j = 0
#     for k in xrange(len(nums)):
#         v = nums[k]
#         nums[k] = 2
#         if v < 2:
#             nums[j] = 1
#             j += 1
#         if v == 0:
#             nums[i] = 0
#             i += 1


# sample 12 ms submission
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         low=0
#         mid=0
#         n=len(nums)
#         high=n-1
#         while(mid<=high):
#             if(nums[mid]==0):
#                 nums[low],nums[mid]=nums[mid],nums[low]
#                 low+=1
#                 mid+=1
#             elif(nums[mid]==1):
#                 mid+=1
#             else:
#                 nums[mid],nums[high]=nums[high],nums[mid]
#                 high-=1

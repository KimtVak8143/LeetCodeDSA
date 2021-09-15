# 26. Remove Duplicates from Sorted Array
# 84 ms solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new = {}
        for x in nums:
            try:
                new[x] += 1
            except:
                new[x] = 1
        # print(new)
        sumex = []
        # flag =0
        for y in new:
            if y not in sumex:
                sumex.append(y)
            # if new[y]>1:
            #     flag+=1

        nums.clear()
        nums.extend(sumex)
        print(nums)


# # sample 60 ms submission
#
#
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         j = 0
#         for i in range(1, len(nums)):
#             if nums[i - 1] != nums[i]:
#                 nums[j] = nums[i - 1]
#                 j += 1
#
#         if len(nums):
#             nums[j] = nums[len(nums) - 1]
#             j += 1
#
#         if not j:
#             j = 1
#
#         return j

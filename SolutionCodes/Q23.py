# 283. Move Zeroes

# 52 ms solution
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new = []
        flag = 0
        for x in nums:
            if x != 0:
                new.append(x)
            if x == 0:
                flag += 1

        for i in range(flag):
            new.append(0)

        nums.clear()
        nums.extend(new)
        print(nums)


# # Sample 35 ms submission
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         nonzero_idx = 0
#         for num in nums:
#             if num != 0:
#                 nums[nonzero_idx] = num
#                 nonzero_idx += 1
#         for idx in range(nonzero_idx, len(nums)):
#             nums[idx] = 0


# # sample 28 ms submission
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         count = 0
#         for i, ele in enumerate(nums):
#             if ele != 0:
#                 nums[i] = 0
#                 nums[count] = ele
#                 count = count + 1

# 27. Remove Element

# 36ms solution
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new = []
        for x in nums:
            if x !=val:
                new.append(x)
        nums.clear()
        nums.extend(new)
        print(nums)


# # sample 16 ms submission
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         for i in range(len(nums)-1,-1,-1):
#             if nums[i]==val:
#                 del nums[i]
#         return len(nums)

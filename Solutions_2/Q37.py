# 268. Missing Number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumax = sum(nums)
        l = len(nums)
        target = l*(l+1)//2
        diff = target-sumax
        return diff


# # sample 104 ms submission
# class Solution:
#     def missingNumber(self, arr: List[int]) -> int:
#         return ((len(arr))*(len(arr)+1))//2 - sum(arr)

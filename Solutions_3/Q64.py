# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return False
        prod = 1
        new = [1] * len(nums)
        for x in range(len(nums)):
            new[x] *= prod
            prod *= nums[x]
        prod = 1
        for x in range(len(nums) - 1, -1, -1):
            new[x] *= prod
            prod *= nums[x]

        return new


# sample 200 ms submission

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         output = [1] * len(nums)
#         L = len(output)
#         for i in range(1,L):
#             output[i] = output[i-1] * nums[i-1]
#         r = 1
#         for i in reversed(range(L)):
#             output[i] = output[i] * r
#             r = r * nums[i]
#         return output

# 1929. Concatenation of Array

# 84 ms solution
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l=len(nums)
        for i in range(0,l):
            nums.append(nums[i])
        return nums


# # sample 60 ms submission
# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         ans = nums
#         ans.extend(nums)
#         return ans

# 1470. Shuffle the Array

# 60ms solution
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new = []
        for i in range(0, n):
            new.append(nums[i])
            new.append(nums[i + n])

        return new

# # sample 40 ms submission
# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         res=[]
#         for i in range(n):
#             res.extend([nums[i],nums[i+n]])
#         return


# sample 44 ms submission
# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         arr_one = nums[:n]
#         arr_two = nums[n:]
#         result = []
#         for i in range(n):
#             result.append(arr_one[i])
#             result.append(arr_two[i])
#
#         return result

# 1365. How Many Numbers Are Smaller Than the Current Number

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new = []
        for i in nums:
            flag = i
            count = 0
            for j in nums:
                if flag > j and j != i:
                    count += 1
            new.append(count)

        return new


# # sample 36 ms submission
#
# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#
#         s_nums = sorted(nums)
#         less_cnt = dict()
#
#         for i, val in enumerate(s_nums):
#
#             if val not in less_cnt:
#                 less_cnt[val] = i
#
#         ret = []
#
#         for val in nums:
#             ret.append(less_cnt[val])
#
#         return ret


# # sample 40 ms submission

# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         bucket = [0] * 102
#         for num in nums:
#             bucket[num + 1] += 1
#         for i in range(1, len(bucket)):
#             bucket[i] += bucket[i - 1]
#         result = [0] * len(nums)
#         for i in range(len(nums)):
#             result[i] = bucket[nums[i]]
#         return result

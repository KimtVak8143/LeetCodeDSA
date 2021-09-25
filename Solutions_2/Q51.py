# 1313. Decompress Run-Length Encoded List

# 84 ms solution
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        new = []
        for i in range(len(nums)//2):
            freq, val = nums[2*i],nums[2*i+1]
            for x in range(freq):
                new.append(val)
        return new


# sample 24 ms submission
#
# class Solution:
#     def decompressRLElist(self, nums: List[int]) -> List[int]:
#         decompressed_list = []
#
#         for i in range(0, len(nums), 2):
#             freq = nums[i]
#             val = nums[i + 1]
#             temp = str(val) + ","
#             decompressed_list.append((temp * freq)[:-1])
#
#         return decompressed_list

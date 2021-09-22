# 4. Median of Two Sorted Arrays
# 92 ms solution

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        new = []
        for i in nums1:
            new.append(i)
        for j in nums2:
            new.append(j)

        new.sort()
        if (m + n) % 2 == 0:
            med = (new[len(new) // 2] + new[(len(new) // 2) - 1]) / 2
        else:
            med = new[len(new) // 2]
        return med


# # sample 68 ms submission
#
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         nums3 = nums1 + nums2
#         nums3.sort()
#         x = len(nums3)
#         if (x % 2 == 0):
#             return (nums3[(x // 2) - 1] + nums3[x // 2]) / 2
#         else:
#             return nums3[x // 2]

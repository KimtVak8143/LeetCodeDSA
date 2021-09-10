# 88. Merge Sorted Array

# Follow up: Can you come up with an algorithm that runs in O(m + n) time?

# hint 1 :
# You can easily solve this problem if you simply think about two elements
# at a time rather than two arrays. We know that each of the individual arrays is sorted.
# What we dont know is how they will intertwine. Can we take a local decision
# and arrive at an optimal solution?

# Hint 2:
# If you simply consider one element each at a time from the two arrays and make a decision
# and proceed accordingly, you will arrive at the optimal solution.


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new = [None] * (m + n)
        i, j, k = 0, 0, 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                new[k] = nums1[i]
                k += 1
                i += 1
            else:
                new[k] = nums2[j]
                k += 1
                j += 1

        while i < m:
            new[k] = nums1[i]
            k += 1
            i += 1
        while j < n:
            new[k] = nums2[j]
            k += 1
            j += 1

        nums1.clear()
        nums1.extend(new)
        # nums1=new.copy()
        return nums1

# 278. First Bad Version

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n - 1

        while (left <= right):
            mid = left + (right - left) // 2
            if isBadVersion(mid) == False:
                left = mid + 1
            else:
                right = mid - 1
        return left


# sample 12 ms submission
#
# class Solution:
#     def firstBadVersion(self, n):
#         l = 0
#         r = n
#
#         while l < r:
#             mid = l + ( r -l )/ /2
#
#             if isBadVersion(mid):
#                 r = mid
#             else:
#                 l = mid + 1
#         return l

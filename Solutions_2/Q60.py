# 374. Guess Number Higher or Lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while(left<=right):
            mid = left + (right - left)//2
            result = guess(mid)
            if result==0:
                return mid
            elif result<0:
                right = mid-1
            else:
                left = mid+1
        return -1

# sample 12 ms submission
#
# class Solution:
#     def guessNumber(self, n: int) -> int:
#         start, end = 1, n
#         while True:
#             mid = start + (end - start) // 2
#             if guess(mid) == 1:
#                 start = mid + 1
#             elif guess(mid) == -1:
#                 end = mid - 1
#             else:
#                 return mid

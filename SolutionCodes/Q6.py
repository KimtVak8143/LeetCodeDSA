# 977. Squares of a Sorted Array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        k = 0
        l = len(nums)
        for k in range(l):
            if nums[k] >= 0:  # the breakpoint of -ve and +ve
                break
        i = k - 1  # for -ve
        j = k  # for +ve
        index = 0
        new = [0] * l  # the result list

        while i >= 0 and j < l:
            if nums[i] * nums[i] < nums[j] * nums[j]:  # sort comparison
                new[index] = nums[i] * nums[i]
                i -= 1
                index += 1
            else:
                new[index] = nums[j] * nums[j]
                j += 1
                index += 1

        while i >= 0:  # Rest elements of -ve
            new[index] = nums[i] * nums[i]
            i -= 1
            index += 1
        while j < l:  # Rest element sof +ve
            new[index] = nums[j] * nums[j]
            j += 1
            index += 1

        return new  # Resultant List

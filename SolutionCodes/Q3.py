# 1. two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashnew = dict()  # Creates a dictionary to store integers
        pair = []  # list to store index of 2 sum integers
        found = False  # Found flag
        i = 0
        while i < len(nums):
            hashnew[nums[i]] = i  # Initial Dictionary storage
            i += 1

        i = 0

        while i < len(nums) and not found:
            new = target - nums[i]  # the other number

            if new in hashnew:  # IF found, check if index aren't equal, else check next Int
                if i != hashnew[new]:
                    pair.append(i)  # Append first fixed integer
                    pair.append(hashnew[new])  # Append the other combo
                    found = True  # Change Flag
            i += 1  # IF not founf, check next integer

        return pair  # Retunr the resulting list

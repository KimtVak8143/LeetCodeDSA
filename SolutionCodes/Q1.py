# 217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Frequency counting technique
        new = {}
        flag = 0
        for a in nums:
            try:
                new[a] += 1
            except:
                new[a] = 1
        for a in new:
            if new[a]>1:
                return True
        else:
            return False

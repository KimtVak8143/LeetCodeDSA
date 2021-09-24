# 1672. Richest Customer Wealth

# 52 ms solution
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxum = 0
        for i in range(len(accounts)):
            each = sum(accounts[i])
            maxum = max(each, maxum)
        return maxum

# sample 32 ms submission
# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         mny = 0
#         mx = 0
#         for i in accounts:
#             mny = sum(i)
#             if mny > mx:
#                 mx = mny
#         return mx

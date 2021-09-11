# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # The most efficient approach
        if len(prices) < 2:
            return 0
        high = prices[0]
        low = prices[0]
        maxr = 0
        for x in prices:
            if x > high:
                high = x
                maxr = max(maxr, high - low)
            if x < low:         # To avoid negative profit possibility
                high = x
                low = x
        return maxr

# Another Approach
#         minr,maxr =prices[0],float('-inf')
#         if len(prices)<2:
#             return 0
#         for x in prices:
#             maxr = max(maxr, x-minr)
#             minr = min(minr, x)
#         return maxr


# Another Approach
# minr = prices[0]
# maxr=0
# if not prices:
#     return 0
# for i in range(1, len(prices)):
#     if prices[i]<minr:
#         minr= prices[i]
#     maxr = max(maxr, prices[i]-minr)
# return maxr

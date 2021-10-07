# 1629. Slowest Key

# 44ms solution
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        long = 0
        start = 0
        res = ''
        for i, time in enumerate(releaseTimes):
            total = time - start

            if total > long:
                long = total
                res = keysPressed[i]

            if total == long:
                cur = keysPressed[i]
                if ord(cur) > ord(res):
                    res = cur
            start = time
        return res

# sample 36 ms submission

# class Solution:
#     def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
#         ans,l = keysPressed[0],releaseTimes[0]
#         for i in range(1,len(releaseTimes)):
#             k = releaseTimes[i]-releaseTimes[i-1]
#             if k>l or k==l and ans<keysPressed[i]:
#                 ans,l = keysPressed[i],k
#         return ans

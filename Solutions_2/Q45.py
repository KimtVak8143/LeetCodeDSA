# 2011. Final Value of Variable After Performing Operations

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in operations:
            if '++' in i:
                x+=1
            elif '--' in i:
                x-=1
        return x


# # sample 32 ms submission
# class Solution:
#     def finalValueAfterOperations(self, operations: List[str]) -> int:
#         x = 0
#         for op in operations:
#             if op in ["X++", "++X"]:
#                 x += 1
#             else:
#                 x -= 1
#         return x

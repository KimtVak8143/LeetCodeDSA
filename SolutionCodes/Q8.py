# 349. Intersection of Two Arrays

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        new = {}
        nl = []
        for a in nums1:
            # try:
            #     new[a]+=1
            # except:
            new[a] = 1

        for b in nums2:
            if b in nums1:
                new[b] += 1

        for x in new:
            if new[x] > 1:
                nl.append(x)

        return nl

#         new = set()
#         nl=[]
#         i,j =0,0
#         a,b = len(nums1),len(nums2)
#         for i in range(0,a):
#             new.add(nums1[i])

#         for j in range(0,b):
#             if nums2[j] in new:
#                 nl.append(nums2[j])

#         return nl

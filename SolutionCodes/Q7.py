class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        new = []
        nl = {}

        for i in nums1:
            if i in nl:
                nl[i] += 1
            else:
                nl[i] = 1
        for j in nums2:
            if j in nl:
                new.append(j)
                nl[j] -= 1
                if nl[j] == 0:
                    del nl[j]

        return new


# Another Approach - Failed
#         new = set()
#         nl=[]
#         i,j =0,0
#         a,b = len(nums1),len(nums2)
#         for i in range(0,a):
#             new.add(nums1[i])

#         for j in range(0,b):
#             if nums2[j] in new and nums2[j] not in nl:
#                 nl.append(nums2[j])
#         return nl


# Another Approach - Failed
# i,j =0,0
# a,b = len(nums1),len(nums2)
# nl=[]
# while i<a and j<b:
#     if nums1[i]>nums2[j]:
#         j+=1
#     else:
#         if nums1[i]<nums2[j]:
#             i+=1
#         else:
#             nl.append(nums1[i])
#             i+=1
#             j+=1
# return nl


# Another Approach - Failed
#         new ={}

#         for a in nums1:
#             # try:
#             #     new[a]+=1
#             # except:
#             new[a]=1

#         for b in nums2:
#             try:
#                 new[b]+=1
#             except:
#                 new[b]=1
#         nl=[]
#         for x in new:
#             if new[x]>1:
#                 nl.append(x)

#         return nl

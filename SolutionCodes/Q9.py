# 1813. Sentence Similarity III

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        l1 = sentence1.split()
        l2 = sentence2.split()

        #         if m > n:
        #             l1, l2 = l2, l1

        while l1 and l2 and l1[-1] == l2[-1]:
            l2.pop()
            l1.pop()
        l1.reverse()
        l2.reverse()
        while l1 and l2 and l1[-1] == l2[-1]:
            l1.pop()
            l2.pop()

        return not l1 or not l2


# Fastest Solution
# class Solution:
#     def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
#
#         l1 = sentence1.split(' ')
#         l2 = sentence2.split(' ')
#         m = len(l1)
#         n = len(l2)
#         if m == n:
#             if sentence1 == sentence2:        # Direct Conclusion
#                 return True
#             else:
#                 return False
#         elif n > m:
#             l2, l1 = l1, l2                   # l1 is larger
#
#         len_min = n
#
#         i = 0
#         while i < n and l1[i] == l2[i]:
#             len_min -= 1
#             i += 1
#
#         j = 0
#         while j < n - i and l1[-j - 1] == l2[-j - 1]:
#             len_min -= 1
#             j += 1
#
#         if len_min == 0:
#             return True
#         else:
#             return False

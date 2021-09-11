# 1813. Sentence Similarity III

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        l1 = sentence1.split()
        l2 = sentence2.split()

        #         if len(l1) > len(l2):
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

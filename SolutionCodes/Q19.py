# 387. First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        new = {}
        for i in range(len(s)):
            try:
                new[s[i]] += 1
            except:
                new[s[i]] = 1

        for j in range(len(s)):
            if new[s[j]] == 1:
                return j

        return -1


# sample 28 ms submission

#
# class Solution:
#     # O(N) time, O(1) space
#     def firstUniqChar1(self, s: str) -> int:
#         '''
#         {'a': (count, lastSeenIndex)}
#         '''
#         freq = dict()
#         # O(N) time
#         for i, char in enumerate(s):
#             if char in freq:
#                 freq[char][0] += 1
#                 freq[char][1] = i
#             else:
#                 freq[char] = [1, i]
#
#         # O(26) time
#         for key, value in freq.items():
#             if value[0] == 1:
#                 return value[1]
#
#         return -1
#
#     # s.index(char) => O(N)
#     # s.count(char)  => O(N)
#     # O(N) time, O(1) space
#     def firstUniqChar(self, s: str) -> int:
#         alphabets = string.ascii_lowercase
#         indexes = [s.index(char) for char in alphabets if s.count(char) == 1]
#         return min(indexes) if indexes else -1




#
# sample 20 ms submission
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         a = 1e5
#         for c in string.ascii_lowercase:
#             l = s.find(c)
#             r = s.rfind(c)
#             if l == r != -1:
#                 a = min(a, l)
#         return a if a < 1e5 else -1


# Another approach using enumerate
# for i,val in enumerate(s):
#             if s.count(val)==1:
#                 return i
#         return -1

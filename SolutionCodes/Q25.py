# 821. Shortest Distance to a Character
# 63 ms solution

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        old = []
        for k, v in enumerate(s):
            if v == c:
                old.append(k)

        new = []
        i = 0
        for k, v in enumerate(s):
            if v == c:
                new.append(0)
                i += 1
            elif k < old[0]:
                new.append(old[0] - k)
            elif k > old[-1]:
                new.append(k - old[-1])
            else:
                new.append(min(old[i] - k, k - old[i - 1]))

        return new


# # sample 24 ms submission

# class Solution:
#     def shortestToChar(self, s: str, c: str) -> List[int]:
#         pre_index = post_index = s.index(c)
#         n_list = []
#         k = 0
#         while s:
#             n_list.append(min(abs(k-pre_index), abs(k-post_index)))
#             s = s[1:]
#             if k == post_index:
#                 pre_index = 0
#                 try:
#                     post_index = s.index(c) + 1
#                 except:
#                     post_index = 10**4
#                 k = 0
#             k += 1
#         return n_list


# def shortestToChar(self, S, C):
#     n = len(S)
#     res = [n] * n
#     pos = -n
#     for i in list(range(n)) + list(range(n)[::-1]):
#         if (S[i] == C):  pos = i
#         res[i] = min(res[i], abs(i - pos))
#     return res


# sample 28 ms submission
# class Solution:
#     def shortestToChar(self, s: str, c: str) -> List[int]:
#         n = len(s)
#         first = s.find(c)
#         answer = [0]*n
#         for i in range(n):
#             if s[i]==c:
#                 first = i
#                 answer[i]=0
#             else:
#                 answer[i]=abs(first-i)
#
#         for i in range(n-1,-1,-1):
#
#             if s[i]==c:
#                 first = i
#             answer[i] = min(answer[i],abs(first-i))
#         return answer

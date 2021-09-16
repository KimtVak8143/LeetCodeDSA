# 1945. Sum of Digits of String After Convert

# 36ms solution
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # for i in range(len(s)-1):
        #     s = "".join(str(ord(s[i])-96))
        s = "".join(str(ord(ch) - 96) for ch in s)

        for _ in range(k):
            x = sum(int(a) for a in s)
            s = str(x)

        return s


# # sample 16 ms submission
#
#
# class Solution:
#     def getLucky(self, s: str, k: int) -> int:
#         res = "".join(str(ord(x) - ord("a") + 1) for x in s)
#
#         while k > 0 and len(res) > 1:
#             res = str(sum(map(int, res)))
#             k -= 1
#         return res

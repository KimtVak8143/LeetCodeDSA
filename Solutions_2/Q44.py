# 844. Backspace String Compare

# 32 ms solution
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def check(s):
            new = []
            for ch in s:
                if ch!='#':
                    new.append(ch)
                elif new:
                    new.pop()
            res = "".join(new)
            return res
        return check(s)==check(t)


# sample 8 ms submission
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        s_pound = 0
        t_pound = 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == "#":
                    s_pound += 1
                    i -= 1
                elif s_pound > 0:
                    s_pound -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if t[j] == "#":
                    t_pound += 1
                    j -= 1
                elif t_pound > 0:
                    t_pound -= 1
                    j -= 1
                else:
                    break
            if (i >= 0) != (j >= 0):
                return False
            if i >=0 and j >= 0 and s[i] != t[j]:
                return False
            i -= 1
            j -= 1
        return True
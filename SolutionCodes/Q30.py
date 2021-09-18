# 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        rev = s[::-1]
        new = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        last = 0
        total = 0

        for x in rev:
            now = new[x]
            if last > now:
                total -= now
            else:
                total += now
            last = now

        return total


# # sample 20 ms submission
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         convert = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X' : 10, 'V': 5, 'I': 1}
#         prevChar = 'I'
#         answer = 0
#         for char in s[::-1]:
#             if convert[char] >= convert[prevChar]:
#                 answer += convert[char]
#                 prevChar = char
#             else:
#                 answer -= convert[char]
#         return answer

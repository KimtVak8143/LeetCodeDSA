class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # 16 ms solution
        if len(magazine) < len(ransomNote):
            return False

        for x in set(ransomNote):
            if ransomNote.count(x) > magazine.count(x):
                return False
        return True

        # 36 ms solution
        # for i in ransomNote:
        #     if i in magazine:
        #         magazine = magazine.replace(i,"", 1)
        #     else:
        #         return False
        # return True


# # sample 14000 KB submission
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         frequency ={}
#         for i in magazine:
#             if i not in frequency:
#                 frequency[i ] =0
#             frequency[i ]+ =1
#
#         for j in ransomNote:
#             if j not in frequency:
#                 return False
#             frequency[j ]- =1
#             if frequency[j ] <0:
#                 return False
#         return True

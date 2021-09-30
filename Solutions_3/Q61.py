# 1773. Count Items Matching a Rule

class Solution:
    new = {'type':0, 'color':1, 'name':2}
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # new = {'type':0, 'color':1, 'name':2}
        sum=0
        i = self.new[ruleKey]
        for x in items:
            if x[i]==ruleValue:
                sum+=1
        return sum


# sample 212 ms submission
# class Solution:
#     def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
#             d = {
#                 'color':1,
#                 'type':0,
#                 'name':2
#             }
#
#             indx = d.get(ruleKey)
#
#             count = 0
#
#             for item in items:
#                 if item[indx] == ruleValue:
#                     count += 1
#
#             return count

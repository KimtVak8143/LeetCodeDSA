# 481. Magical String

# 180 ms solution
class Solution:
    def magicalString(self, n: int) -> int:
        new = [1, 2, 2]
        # i = 2
        for i in range(2, n):
            new += new[i] * [3 - new[-1]]
            # i+=1
            # print(new)

        return new[:n].count(1)


# Another Efficient approach
# class Solution:
#     def magicalString(self, n: int) -> int:
#         opposite = {'1': '2', '2': '1'}
#         s = "122"
#         i = 2
#         while len(s) < n:
#             s += int(s[i]) * opposite[s[-1]]
#             i += 1
#         return s[:n].count('1')


# # sample 52 ms submission
# s = [1,2,2]
# index = 2
# while len(s) < 100000:
# 	# according to the last element, we decide the value of 'val'
# 	val = 3 - s[-1]
# 	s.extend([val]*s[index])
# 	index += 1
#
# class Solution(object):
#     def magicalString(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         return s[:n].count(1)

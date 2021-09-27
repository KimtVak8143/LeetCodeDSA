# 706. Design HashMap

class MyHashMap:

    def __init__(self):
        self.new = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        self.new[key] = value

    def get(self, key: int) -> int:
        check = self.new[key]
        return check if check !=None else -1

    def remove(self, key: int) -> None:
        self.new[key] = None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# sample 176 ms submission
# class MyHashMap:
#
#     def __init__(self):
#         self.hashMap = dict()
#
#     def put(self, key: int, value: int) -> None:
#         self.hashMap[key] = value
#
#     def get(self, key: int) -> int:
#         return self.hashMap[key] if key in self.hashMap else -1
#
#     def remove(self, key: int) -> None:
#         if key in self.hashMap:
#             del self.hashMap[key]

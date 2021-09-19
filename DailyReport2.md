# Daily Progress Set #2

## 19 September 2021

- Single Number - 136
  - naive thinking - create a dictionary, increment counts of each element
  - as the result is unique in list, hence its count will be less than 2, hence return that element
  - Efficient Solution : Using XOR(^), basically any number XORed with itself is 0, 
  - so each duplicate number will "cancel out" itself, except for the number that only exists once in the list
  - that is our result, return that element.

- Single Number II - 137
  - C++ : First time number appear -> save it in "ones"
  - Second time -> clear "ones" but save it in "twos" for later check
  - Third time -> try to save in "ones" but value saved in "twos" clear it.
  - Python: using map approach

- Single Number III - 260
  - same technique as in for 137 & 136, simply appended the result in a new list and return list
  - OR using counter function



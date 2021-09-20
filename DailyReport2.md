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
  
- Find the Duplicate Number - 287
  - using same technique of map hashing, and returning element having count>1
  - OR
  - simply running duplicate check technique
  - OR using enumerate/counter methods

## 20 September 2021

- Set Mismatch - 645
  - calculate the sum of n integers from 1 to n,i.e. target
  - then calculating sum of elements of nums list
  - now finding the duplicate element
  - at last, using relation we get, result = target-(sum-k),
  - now appending the result and k into a list and return them.
  
- Missing Number - 268
  - simple method of using summation of 1 to n and then subtracting the summation of nums list elements.
  - return the result

- Find the Difference - 389
  - naive thinking: create a dictionary, now increment count of each element for 1st string
  - then iterate in 2nd string, now decrement counts, unless the count is already 0, then return that character
  - Efficient thinking: store the sum of ascii integers of all characters in string 1 and 2
  - then calculate the difference between the two, the resultant is the ascii of extra character
  - convert ascii into char, return that char
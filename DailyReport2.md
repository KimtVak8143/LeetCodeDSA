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

## 21 September 2021

- How Many Numbers Are Smaller Than the Current Number - 1365
  - Brute force method : iterate through nums, keep one element fixed and compare the entire list, 
  - increment count if less than fixed int, then append the count in a new list
  - return list

- Running Sum of 1d Array - 1480
  - simple method

- Concatenation of Array - 1929
  - naive thinking, return nums+nums
  - efficient : store len(nums) in n, then append nums[i] in nums as
  - nums.append(nums[i]) for i in range(0,n)
  - return nums

## 22 September 2021

- Median of Two Sorted Arrays - 4
  - create a new list, store nums1,nums2 in it
  - then use .sort(), then check for even length, then return that element.

- Build Array from Permutation - 1920
  - simply create a new list, then iterate through nums1 and store elements as
  - new.append(nums[i])
  - return new

- Backspace String Compare - 844
  - using an extra function, which pops element if ch=='#', else append the char
  - and return check(s)==check(t)


## 23 September 2021
- Final Value of Variable After Performing Operations - 2011
  - simple string check for '++'&& '--' in list item, increment/decrement accordingly
  - return var
  
- Kids With the Greatest Number of Candies - 1431
  - define maxum = max(list)
  - for each element check if candies[i]+extra>=maxum, append true in list, else false
  - return list

- Shuffle the Array - 1470
  - create a new list, simple append nums[i] and nums[i+n], for n times
  - return new list
  - OR, 
  - break nums into 2 list, as [:n] and [n:], 
  - now in a loop, append both into result list, return result

## 24 September 2021

- Richest Customer Wealth - 1672
  - get into each list row, and use sum(), to get sum of each secondary list
  - then take max of all-time maximum and current sum
  - return maxum

- Check If Two String Arrays are Equivalent - 1661
  - create 2 empty strings, now store all list strings, then return s1==s2
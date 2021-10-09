# Daily Progress Set #3

## 30 September 2021
- Count Items Matching a Rule - 1773
  - create a dictionary with type, color, name initialised to 0,1,2
  - then store corresponding value of rulekey in i
  - then iterate through each item
  - and match for i index with rulevalue, increment sum by 1
  - return sum

- Cells with Odd Values in a Matrix - 1252
  - Firstly Initiate the rows and cols list with 0 for m and n values
  - then read values of r and c from indices list matrix
  - then increment the respective row/col with 1
  - finally, take count/sum of odd numbers as
  - sum([(r+c)%2 for r in l1 for c in l2])
  - return sum

## 4 October 2021

- Longest Common Prefix - 14
  - pre-check for empty given list, return ""
  - then create a string and store the minimum string among the strs list. 
  - now using numerate function, store values of string and the frequency
  - now check for each string, perform their frequency validation
  - upon failing return the string updated till now !!

## 5 October 2021

- Product of Array Except Self - 238
  - first store product of list
  - then store product in reverse order
  - finally, return result

## 6 October 2021

- Add Strings - 415
  - store sum of int of both nums in new, then return str(new) 

## 7 October 2021

- Slowest Key - 1629
  - using enumerate function, iterate through values of realeaseTimes
  - then check for difference, and compare with long and update accordingly
  - if long>time, then store char in result
  - In case the values of releasetimes are same, then check for highest ASCII value using ord()
  - finally, update start time, then return res char in the end
  
## 8 October 2021

- Multiply Strings - 43
  - using one-to-one multiplication
  - reverse both strings, then take each digit and apply a few optimizations to simulate the final string result

## 9 October 2021

- 
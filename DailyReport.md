# Daily Progress Set #1

## 9 september 2021

- Contains Duplicate - 217
  - Frequency count technique

- Maximum Subarray - 53 
  - Kadane's Algorithm

## 10 September 2021

- Two Sum - 1
  - Hashmap technique - create dictionary(key- integer, value- index)
  - then subtract fixed integer from target and search in dictionary
  - then append the index of Int and compliment

- Two Sum - 167 
  - Hashmap technique - create dictionary(key- integer, value- index)
  - then subtract fixed integer from target and search in dictionary
  - then append the index of Int and compliment
  
- Merge Sorted Array - 88
  - Create a new list of size (m+n),
  - in loop append the smallest element by comparing the 2 lists
  - then add remaining elements of both lists after sorting is done.
  - then clear the 1st list, and extend that list with new list
  
- Squares of a Sorted Array - 977
  - naive approach - square each element, then sort
  - efficient approach - divide the list into -ve and +ve list
  - iterate through elements, and store square of -ve in reverse order
  - and squares of +ves normally in a new list

## 11 september 2021

- Intersection of Two Arrays II - 350
  - hash table approach - first create a dict
  - then store 1st list elements, if duplicate increment count
  - then check with 2nd list elements, if found, append the result list
  - reduce the count by 1, for duplicate check, if count is 0,
  - then delete the key finally return result list

- Intersection of Two Arrays - 349
  - hash table approach, first create a dictionary
  - then store all elements of 1st list, ignore duplicates
  - then iterate through 2nd list, if element in 1st list also, 
  - then append in result, finally return result list
  - Naive Approach - create 2 sets, for each list
  - then use intersection function and print result as
  - return list(l1 & l2)

- Sentence Similarity III - 1813
  - Common prefix/suffix technique
  - store the strings as a list, then Compare first and last element of list,
  - then pop them out, until size of any list == 0, 
  - if any of the list is empty, then it satisfies the condition, 
  - hence, return True
  - Or
  - compare the last elements only, and reverse after popping them
  - then pop them out, until size of any list == 0, 
  - if any of the list is empty, then it satisfies the condition, 
  - hence, return True

- Best Time to Buy and Sell Stock - 121
  - create 2 markers - high and low, and set on prices[0]
  - now iterate through each element, if ele>high => update value of high, 
  - while low will be same, now store maximum of (high-low, original)
  - now move forward, if ele<low => update low and high as well, to avoid 
  - negative profit possibility

## 12 September

- Reverse Integer - 7
  - Naive solution - divide and remainder logic, check for outbound too, 
  - -2**\31-1 and 2**31 and multiply with - for negative numbers, then apply method
  - Efficient Approach - Convert into string, then check for '-', if true, 
  - remove it then apply revNum += (int(strX[i]) * pow(10, i)), 
  - finally, check for outbound condition, and if signed, then add '-' at beginning of string
  - then return result integer 
  - Another approach - store as string, check for '-' in it, 
  - if true, then res = int(str(x)[1:][::-1]) and then add '-' at last to res
  - return res

- Pascal's Triangle - 118
  - Any row can be constructed using the offset sum of the previous row
  - res = [[1]] -> the initial row, for further calculation
  - like 1210+0121 =1331-> next row, similarly, 13310+01331 =14641 -> next row
  - simply append it into the result list

- Pascal's Triangle -II - 119
  - Any row can be constructed using the offset sum of the previous row
  - res = [[1]] -> the initial row, for further calculation up till RowIndex+1
  - like 1210+0121 =1331-> next row, similarly, 13310+01331 =14641 -> next row
  - simply append it into the result list, 
  - now return result[rowindex]

- Reshape the Matrix - 566
  - Naive approach - create a linear list, now store all the elements of matrix
  - in the linear list, now check if len(new) = r*c, if false, return the original matrix
  - otherwise, now in a loop, append all elements of new in result matrix 
  - from k to k+c, up till len(new), with increment of c, to avoid overflow

## 13 september 2021

- Valid Sudoku - 36
  - CPP - create a row[9][9], col[9][9] and block[3][3][9] with each element =0
  - since the input is in strings, so [number][string] logic is used
  - rows[5][0] means whether number 1('0'+1) in row 5 has appeared
  - cols[3][8] means whether number 9('8'+1) in col 3 has appeared
  - blocks[0][2][5] means whether number '6' in block 0,2 (row 0~2,col 6~8) has appeared
  - now iterating through each element of board, skip all those with '.'
  - calculate the number's index(board's number minus 1)
  - if the number has already appeared once, return false
  - else return True
  - Python3 - 
  - create a set, now iterate through each board element, if element!='.', then proceed
  - if (i, ele) or (ele, j) or (i//3, j//3, ele) are in set already, 
  - this means, it's a repetition, hence return false
  - otherwise, add all these elements (i, ele),(ele, j),(i//3, j//3, ele)
  - in the set and proceed
  - Finally, return True

- Search a 2D Matrix - 74
  - Decreasing the search scope Technique, with help of lower and upper bound
  - LB- first element of row, UB- last element of row
  - if target > UB, row++ or if target < UB, col--
  - hence, minimizing teh search area, and if target==matrix[i][j], return True
  - Linear sorting was present in matrix, hence runtime was efficient
  
- Search a 2D Matrix II - 240
  - Same method used as above, but this was quite complex, because of 
  - different sorting in rows and columns, i.e. not linear sorting, hence runtime increased significantly

## 14 September 2021

- Ransom Note - 383
  - Python - using count(), for each element if count of ransom is less than magazine, return False, else proceed, finally return True
  - or, iterate through each element in ransom, if found in magazine also,
  - then replace(i,"",1) and proceed, if all are found, return True, otherwise False
  - or, simply create a dictionary (hash table) and mark frequency of each character in magazine, 
  - then check for presence of ransom elements in dict, 
  - then decrement the frequency by 1
  - then if frequency of all element is < 0, return False, otherwise Return True
  - C++ - Create a array of 26, store frequency each character of magazine at ascii index, 
  - now iterate through ransom, and store their frequency in ransom array,
  - now ideally, frequency of ransom elements should be less than or equal to magazine
  - so if this is not the case, return False, else True
  - OR, using unordered map for 26 objects, 
  - increment magazine elements in map, and later, decrement ransom elements
  - if count/frequency goes <0, return False, else return True

- First Unique Character in a String - 387
  - using hash table approach, store frequency of each character, 
  - then iterate and if freq ==1, return i, else return -1

- Valid Anagram - 242
  - first check if lengths are equal or not, if not return False, else continue
  - now simply iterate in set of string1, and check if 
  - s1.count(i)!=s2.count(i), -> return False
  - else return True
  - OR
  - use map = collections.counter(s1), return map1==map2
  - OR
  - take frequency of each element from s1 into map, and later decrement from s2
  - finally, check if dict is empty or not, if empty, return True 
  - else return False

## 15 September 2021

- Remove Duplicates from Sorted Array - 26
  - used hashtable approach(duplicate), stored all elements in dict with value =1
  - if duplicate, then increased value by 1
  - then iterated through each element of dict, and stored in list,
  - only if it is not already present in it, hence only unique elements are stored
  - finally, cleared nums -> nums.clear() and then extended nums as nums.extend(new)
  - return nums

- Remove Element - 27
  - appended all element of given list into a new list, except ele==val
  - then nums.clear(), and later nums.extend(new), return nums

- Move Zeroes - 283
  - simply creating a new list and appending all elements except x!=0, 
  - and for each x==0, incrementing count/flag. 
  - then append 0 in new for len(flag)
  - OR
  - using enumerate function ( NOT STUDIED YET)

- Magical String - 481
  - Since how many current "1" or "2" depends on previous number in S
  - we can use a queue to get the corresponding information we need. 
  - Every time we update S, we update queue as well.
  - then return count(1) for all 1s in final list/string
  - OR 
  - implementing the same method with using a dict
  - **the important step/formula is S = S[i]\*[3-S[-1]]**

## 16 September 2021

- Shortest Distance to a Character - 821
  - Initially, locate the first occurrence of c in s, then create a list of n size, all initialized to 0
  - now iterate through each character, if ==c, assign flag to that index, and make list[i]=0
  - else, make list[i]= abs(flag-i)
  - now iterating for the shortest distances, by using min()
  - finally, return the list

- Sum of Digits of String After Convert - 1945
  - first converting all characters into their ascii numbers
  - then forming the string of that, and subsequently into int form
  - then for k times, performing sum() on each int in integer-string
  - return string later

## 17 September 2021

- Add Digits - 258
  - simple algo of divide by 10 and add

- Happy Number - 202
  - using a hashmap automatically changes Time-Complexity from O(n) to O(1)
  - so create a set and store all incoming digits using formula
  - n = sum(int(i)**2 for i in str(n)), until n!=1, for n==1, return True
  - Cycle Break rules:
  - if n is already in set, then return False
  - OR
  - using divmod() function for squaring and adding into set
  - use same restrictions until n==1, else for duplicate return False

## 18 September 2021

- Palindrome Number - 9
  - naive solution - use string, then reverse using [::-1], and check for equality, return True/False
  - Efficient approach - reverse the number using rem-divide technique, 
  - then check for equality, this neglects the need of conversion to string

- Roman to Integer - 13
  - define the roman alphabets in a dictionary with their corresponding values
  - then using reverse method, reverse the string, now check for each character 
  - using a simple logic, of last_item>current_item -> then decrement the total
  - else incrementing the total, finally return total

- Integer to Roman - 12
  - define 2 list - values and characters
  - now using rem/divide method, get the last digit and store the corresponding character in result string
  - return result
  - OR
  - create a 2D list, using simple logic store the corresponding character in string
  - return string
  
Link ot next page : <a href="https://github.com/KimtVak8143/LeetCodeDSA/blob/main/DailyReport2.md">Click Here</a>
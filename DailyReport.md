#Daily Progress

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

##11 september 2021
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
  - negative profit possibility,
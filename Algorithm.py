
# # # Linear Traversal Algorithm in Python
# # # Linear Traversal means visiting each element of a list (or array) one by one from the first element to the last element.
# # # Linear Traversal is the process of accessing every element of a data structure exactly once in sequential order.
# # # for example : arr = [1,2,3,4,5]
# # # Linear traversal visits the elements like this: 10 → 20 → 30 → 40 → 50 - It starts from index 0 and ends at n-1.
# # | Case             | Time Complexity | Explanation                                       |
# # | ---------------- | --------------- | ------------------------------------------------- |
# # | **Best Case**    | **O(1)**        | The target is the first element.                  |
# # | **Average Case** | **O(n)**        | The target is somewhere in the middle.            |
# # | **Worst Case**   | **O(n)**        | The target is the last element or is not present. |


def linear(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
    
print("Index:",linear([10,20,40,30,31,50], 30))


# Multiply Every Element
def linear_multiple(arr, value):
    for i in range(len(arr)):
        arr[i] = arr[i] * value
    
    return arr

print("multiply elements:",linear_multiple([1,2,3,4,5], 2))

# print("--------------------------------------------------------------------------------")
# # Binary Search Algorithm
# # Binary Search is a searching algorithm that finds an element in a sorted array by repeatedly dividing the search space into half.(The phrase "repeatedly dividing the search space into half" means choosing the middle element and deciding which half to continue searching.)
# # Important: Binary Search only works on a sorted array.
# # | Case         | Complexity   |
# # | ------------ | ------------ |
# # | Best Case    | **O(1)**     |# Best Case — O(1) The target is found in the very first middle element.
# # | Average Case | **O(log n)** |# Average Case — O(log n) The target is found after a few divisions.
# # | Worst Case   | **O(log n)** |# The algorithm keeps dividing until there is only one element left, and then:the target is found at the end of the search, or the target is not found.

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print("binary search:", binary_search([10,20,30,40,50,60],50))


# print("-------------------------------------------------------------------------")
# # Two Pointer Algorithm in Python - The Two Pointer Algorithm is called a "two pointer" algorithm because it uses two variables (pointers or indices) to keep track of positions in a data structure (usually an array or string).
# # Instead of using two nested loops, we use two pointers to reduce the time complexity.
# # In simple words: Two Pointer = Using two indexes to solve a problem efficiently.
# #           left                 right
# #             ↓                    ↓
# # Index :   0   1   2   3   4
# # Value : [10, 20, 30, 40, 50]


# # It helps to:
# # Search pairs
# # Reverse arrays
# # Reverse strings
# # Check palindrome
# # Remove duplicates
# # Solve Two Sum (Sorted Array)
# # Move zeros
# # Merge arrays

# # Most common Two Pointer algorithms run in O(n) time with O(1) extra space.

# # types of two pointer technique
# #  1. opposite direction - one pointer starts from the beginning and another starts from the end 

# # 2. Same Direction
# # Both pointers move from left to right.


# # example 2: reverse the list
def reverseL(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
    
print("Reverse List:", reverseL([2, 5, 3, 6, 4, 7]))

# example 3 = check palindrome
def checkchar(word):
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
            break
        left += 1
        right -= 1
    return True
    
print("Check P or NP:",checkchar("madam"))


# # Example 4: Pair Sum (Sorted Array) - Find two numbers whose sum is 9.
def twosum(arr, target):
    ans = []
    left = 0
    right = len(arr) - 1

    while left < right: 
        total = arr[left] + arr[right]
        if total == target:
            ans.append([arr[left], arr[right]])
            break
        elif total < target:
            left += 1
        else:
            right -= 1

    return ans


print("ans", twosum([1,2,3,4,5,6,7,8,9], 9))

# # Example 5: Reverse a String 
def reverseS(s):
    string = list(s)
    left = 1 # start from index 1 
    right = len(string) - 1
    while left < right:
        string[left], string[right] = string[right], string[left]
        left += 1
        right -= 1
    return "".join(string)
    
print("reverse string: ",reverseS("Borse")) 

# # Example 6: Remove Duplicates (Same Direction)
def removedup(arr):
    if len(arr) == 0:
        return 0
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return arr[:slow + 1]
    
    
print("Remove Duplicates :",removedup([1,1,2,2,3,3]))
        

# 5. Move All Zeros to the End
def move(arr):
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != 0:
            arr[fast], arr[slow] = arr[slow], arr[fast]
            slow += 1

    return arr

arr = [0,4,5,0,8]
print(move(arr)) # [4, 5, 8, 0, 0]

# print("--------------------------------------------------------------------")
# # Sliding Window Algorithm
# # The Sliding Window is an algorithmic technique used to process contiguous subarrays or substrings efficiently.
# # Instead of checking every possible subarray (which can take O(n²)), it maintains a window that expands or shrinks as needed, reducing many problems to O(n).

# # [2, 1, 5, 1, 3, 2]
# # Suppose the question is: Find the maximum sum of any 3 consecutive elements.
# # Method 1 (Brute Force)
# # Calculate every group of 3:
# # [2,1,5] = 8
# # [1,5,1] = 7
# # [5,1,3] = 9
# # [1,3,2] = 6

# # Maximum = 9
# # This works, but you keep adding the same numbers again and again.

def max_sum(arr, k):
    Window_sum = sum(arr[:k]) # supppse - sum (arr[:3]) = 2,1,5 = 
    max_sum = Window_sum

    for i in range(k, len(arr)):
        Window_sum = Window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, Window_sum)
    
    return max_sum

print("max_sum",max_sum([2,1,5,1,3,2],3))
# print("--------------------------------------------------------------------")
# # pefix Sum is a technique used to calculate the sum of elements in an array quickly.
# # Instead of calculating the sum again and again, we create an array where each position stores the sum of all previous elements including itself.
# # Time Complexity: O(1) - with prefix sum: the answer is obtained using only subtraction 

# # formula 
# # prefix[0] = arr[0]
# # prefix[i] = prefix[i-1] + arr[i]



# # Program 1: Create Prefix Sum
def prefix_sum(arr):
    prefix =[0] *len(arr) # means Create an empty prefix array.- [0,0,0,0,0,0]

    prefix[0] = arr[0] # prefix[0] = 2, now [2,0,0,0,0,0]
    for i in range(1, len(arr)): # suppose i = 1
        prefix[i] = prefix[i - 1] + arr[i] # so create prefix[1] = prefix[0] + arr[i] means 2 + 1 = 3, now - [2,3,0,0,0,0] continous loop to the end

    return prefix


print("prefix_sum: ",prefix_sum([2,1,5,6,7,8])) # [2, 3, 8, 14, 21, 29]

# # Program 2: Range Sum Query - suppose arr[2,4,6,8,10] -find the sum of index 1 to 3, expected = 4 + 6 + 8 = 18

def range_sum(arr, left, right): # left = 1 and right = 3
    prefix = [0] * len(arr) # # means Create an empty prefix array.- [0,0,0,0,0,0]
    prefix[0] = arr[0] #  # prefix[0] = 2, now [2,0,0,0,0,0]
    for i in range(1, len(arr)): # (1,5) = 1,2,3,4
        prefix[i] = prefix[i - 1] + arr[i] # foe ex iteration 1 - i = 1  arr = [2, 4, 6, 8, 10], prefix = [2, 0, 0, 0, 0],excute = prefix[1] = prefix[0] + arr[1],means prefix[1] = 2 + 4 = 6, now prefix = [2, 6, 0, 0, 0]

    if left == 0: # now check left = 1, 1 == 0(False) So this block is skipped
        return prefix[right]
    
    return prefix[right] - prefix[left - 1] # formula - So right = 3,left = 1, prefix[3] - prefix[0] = 20 - 2 = 18

arr = [2,4,6,8,10]
print("range_sum:",range_sum(arr,1,3)) 

# print("--------------------------------------------------------------------------")
# # Hash Map and Hash Table in Python
# # Hash Table - A Hash Table is a data structure that stores data in key-value pairs.
# # Instead of searching through all elements one by one, it uses a hash function to quickly find where the data is stored

# # Why it's O(n): We only loop through the array exactly once. Checking if a number exists in a Hash Map takes constant time, O(1).
# # Hash Map - A Hash Map is an implementation of a Hash Table.
# # in python, dict
# # is implemented using a hash table, so people often use the terms Hash Map and Hash Table interchangeably.

# # Create a hash map
# hash_map = {}

# # Insert
# hash_map["apple"] = 10

# # Access
# print(hash_map["apple"])

# # Update
# hash_map["apple"] = 20

# # Delete
# del hash_map["apple"]

# # Frequency Count (Most Common Interview Question) - IMP
# # Count frequency of numbers.
arr = [1,2,2,3,3,3,4,4,4,4]
freq = {}
for num in arr: # Python will take each element one by one. suppose num = 1 

    if num in freq: # To check 1 in freq({}) - No, So goto the else
        freq[num] += 1

    else:
        freq[num] = 1 # freq[1] = 1 -Number 1 occurred 1 time. - Store the value 1 using the key 1.
        # suppose freq[1] = 1 - dictionary[key] = value
        # python read like this
        # Dictionary Name : freq
        # Key   : 1
        # Value : 1
        # So Python stores: key -> value = 1 -> 1
        # dictionary become 
        # {
        # 1 : 1 
        #}

print(freq) # {1: 1, 2: 2, 3: 3, 4: 4}


# # Two sum using hash map
# # one of the most famous interview question

def two_sum(num, target):
    hashmap = {} # empty hashmap

    for i in range(len(num)):# (4) = 0,1,2,3 , suppose i = 0 num[0] = 2 num[1] = 7
        diff = target - num[i] # 9 - 2 = 7 , 9 - 7 = 2
   
        if diff in hashmap: # if 7 in {} - False
            return[hashmap[diff], i]
        
        hashmap[num[i]] = i # # hhashmap[2] = 0
        # means number 2 stored at index 0

num = [2,7,11,15]
print(two_sum(num, 9))# [0,1]

# print("--------------------------------------------------------------------------------")
# # Kadane's Algorithm (Maximum Sum Subarray)
# # Kadane's Algorithm is used to find the maximum sum of a contiguous (continuous) subarray
# # Time complexity - O(n)
# # space complexity - O(1)
# # example - 
# # arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# # The maximum sum subarray is: - 
# # 4 + (-1) + 2 + 1 = 6


# # Example
def kadane(arr):
    current_sum = arr[0] # -2 
    max_sum = arr[0] # -2 

    for i in range(1, len(arr)): # suppose i = 1
        current_sum = max(arr[i], current_sum + arr[i]) # current_sum = max(1, -2 + 1) = max(1,-1) = 1, So current_sum is updated = 1
        max_sum = max(max_sum, current_sum) # max_sum = max(-2,1) = 1, also max_sum updated = 1
    
    return max_sum

arr = [-2,1,-3,4,-1,2,1,-5,4]
print("Maximum Sum: ",kadane(arr)) # 6


# print("-----------------------------------------------------------------------------------")
# # Dutch National Flag Algorithm
# # It was invented by the famous computer scientist Edsger W. Dijkstra.
# # It is mainly used to sort an array containing only three different values, usually: 0, 1, 2
# # without using any sorting algorithm.

# # Better Approach -Use Three Pointers
# # Time Complexity - O(n)
# # Space - O(1)
# # Three Pointers
# # We use
# # low   -      low = 0
# # mid   -      mid = 0
# # high  -      high = len(arr) - 1

# # | Complexity | Value    |
# # | ---------- | -------- |
# # | Time       | **O(n)** |
# # | Space      | **O(1)** |

def dutch_flag(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

        elif arr[mid] == 1:
            mid += 1

        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

print("dutch_flag",dutch_flag([2, 0, 2, 1, 1, 0]))

# print("-----------------------------------------------------------------------------")
# # Moore's Voting Algorithm - It is used to find the Majority Element in an array.
# # A Majority Element is an element that appears more than n/2 times in an array.
# # where - n = Total number of elements
# # moore's algorithm - Time - O(n) and Space - O(1)


def majority_element(arr):
    candidate = None # means no candidate selected
    count = 0 

    for num in arr:
        if count == 0:
            candidate = num

        if num  == candidate:
            count += 1

        else:
            count -= 1

    return candidate

arr = [2,2,1,2,3,2,2]
print(majority_element(arr)) # 2 

# # Count the Majority Element
def majority_elements(arr):
    candidate = None
    freq = 0
    count = 0
    for num in arr:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
            freq += 1

        else:
             count -= 1
  
    return candidate, freq

arr = [1,1,2,1,3,1,1]
print(majority_elements(arr))


# # program - majority element in a string
def majority_char(text):
    candidate = None
    count = 0
    for ch in text:
        if count == 0:
            candidate = ch

        if ch == candidate:
            count += 1

        else:
            count -= 1
    return candidate

text = "aaaaabb"
print(majority_char(text)) # a

# # Program - Return Both Candidate and Vote Count
def majority_element(arr):

    candidate = None
    count = 0

    for num in arr:

        if count == 0:
            candidate = num

        if num == candidate:
            count += 1

        else:
            count -= 1
    return candidate, count

arr = [2,2,1,2,3,2,2]
print(majority_element(arr)) # (2, 3)



# print("----------------------------------------------------------------")
# # Cyclic Sort in Python - Cyclic Sort places every number in its correct position.
# # Cyclic Sort is a sorting algorithm used when the array contains numbers in a known range, such as 1 to n or 0 to n-1. 
# # Instead of comparing elements, it places each number at its correct index.
# # Time complexity - O(n)

def cyclic_sort(arr):
    i = 0 # start from the first index
    while i < len(arr): # i < 5
        correct = arr[i] - 1 # suppose i = 0, arr[i] = 3, 3 - 1 = 2, So 3 belong karto index 2
        if arr[i] != arr[correct]: # first condition 3 != 2, second 5 !=  2, third = 5 != 4, fourth = 4 != 1
            arr[i], arr[correct] = arr[correct], arr[i] # than swap 3,2 = 2,3 , array1 - 2,5,3,1,4, array2 = 5 2 3 1 4, array3 = 4 2 3 1 5, array4 = 1 2 3 4 5

        else:
            i += 1
    return arr

arr = [3,5,2,1,4]
print(cyclic_sort(arr)) # Output [1, 2, 3, 4, 5]

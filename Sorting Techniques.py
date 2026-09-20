print("------Sorting Techniques------")
print("------1 . Selection Sort-----------")
arr = [7, 4, 1, 5, 3]
n = len(arr)  # 5

for i in range(n - 1):  # -> 5 -1 = 4 means i = 0 ,1,2,3
    min = i
    for j in range(i + 1, n):  # suppose i = 1 ,j= 2,5 = 2,3,4
        if arr[j] < arr[min]:
            min = j
    arr[i], arr[min] = arr[min], arr[i]  # swapping the two number ex 7,1 = 1,7

print("Ascending Order:", arr) 

arr = [7, 4, 1, 5, 3]
n = len(arr)

for i in range(n - 1):
    min = i
    for j in range(i + 1, n):
        if arr[j] > arr[min]:
            min = j
    arr[i], arr[min] = arr[min], arr[i]

print("Decending Order:", arr)


arr = [7.2, 1.2, 1.2222, 1233.3]
n = len(arr)
i = 0
while i < n - 1:
    min = i
    j = i + 1
    while j < n:
        if arr[j] < arr[min]:
            min = j
        j = j + 1
    arr[i], arr[min] = arr[min], arr[i]
    i = i + 1
print("Ascending Order:", arr)

arr = ["a", "d", "c", "b", "e"]
n = len(arr)
i = 0
while i < n - 1:
    min = i
    j = i + 1
    while j < n:
        if arr[j] > arr[min]:
            min = j
        j = j + 1
    arr[i], arr[min] = arr[min], arr[i]
    i = i + 1
print("Descending Order:", arr)


print("-------2 . Bubble Sort-------")
arr = [7, 4, 1, 5, 3]

n = len(arr)  # 5
for i in range(n - 1, 0, -1):  # (4,0,-1) = 4,3,2,1
    for j in range(0, i):  # j star from 0 to i -> means i = 4 ,j = (0,4) = 0,1,2,3
        if arr[j] > arr[j + 1]:  # suppose j = 0  arr[0] > arr[1] checked
            temp = arr[j + 1]  # temp = arr[1]
            arr[j + 1] = arr[j]  # arr[1] = arr[0]
            arr[j] = temp  # arr[0] = arr[1] means arr[0] = 7 ,arr[1] = 4 == 4,7

print("Ascending Order:", arr)

arr = [7, 4, 1, 5, 3] 

n = len(arr) # length of the list
for i in range(n - 1, 0, -1): # using the for loop 
    for j in range(0, i):
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j] # swaping 

print("Descending Order:", arr) # [7,5,4,3,1]


arr = [7, 4, 1, 5, 3]

n = len(arr) # len(arr)
i = n - 1
while i > 0:
    j = 0
    while j < i:
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
        j = j + 1
    i = i - 1

print("Ascending Order:", arr)


arr = [7, 4, 1, 5, 3]

n = len(arr)

i = n - 1
while i > 0:
    j = 0
    while j < i:
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
        j = j + 1
    i = i - 1

print("Descending Order:", arr)


print("------Insertion Sort------")
arr = [7, 4, 1, 5, 3]
n = len(arr)
for i in range(1, n):  # (1,5) = 1,2,3,4
    temp = arr[i] # temp = i = value - 1,2,3,4
    j = i - 1
    while j >= 0 and temp < arr[j]:
        arr[j + 1] = arr[j] 
        j = j - 1
    arr[j + 1] = temp
print("Ascending Order:", arr) # Ascending Order: [1, 3, 4, 5, 7]

arr = [-1,5,7,3.6,11]
n = len(arr)
for i in range(1, n):
    temp = arr[i]
    j = i - 1
    while j >= 0 and arr[j] < temp:
        arr[j + 1] = arr[j]
        j = j - 1
    arr[j + 1] = temp
print("Descending Order:", arr) #Descending Order: [11, 7, 5, 3.6, -1]


arr = [7, 4, 1, 5, 3]
n = len(arr)
i = 1
while i < n:
    temp = arr[i]
    j = i - 1
    while j >= 0 and arr[j] < temp:
        arr[j + 1] = arr[j]
        j = j - 1
    arr[j + 1] = temp
    i = i + 1
print("Descending Order:", arr) # Descending Order: [7, 5, 4, 3, 1]

arr = ["a", "d", "c", "b", "e"]
n = len(arr)
i = 0
while i < n:
    temp = arr[i]
    j = i - 1
    while j >= 0 and temp < arr[j]:
        arr[j + 1] = arr[j]
        j = j - 1
    arr[j + 1] = temp
    i = i + 1
print("Ascending Order:",arr)

print("--------------------")

def mergesort(arr):

    n = len(arr)
    if n > 1:
        mid = n // 2  # 5 // 2 = 2
        left = arr[:mid]  # left = [:2] = 0,1 = [7,4]
        right = arr[mid:]  # right = [2:] = 2,3,4 = [1,5,3]
        l1 = len(left)
        l2 = len(right)

        # meragesort[7,4] means -> The program calls the same function again, but this time with: arr = [7,4] ,So execution goes back to the first line of the function:def mergeSort(arr):
        # Than check all condition n = len(arr) means [7,4] = 2 ,check "if condition" this True than go to mid = n // 2 = 2 // 2 = 1 Than create the left and right means(merge)
        # left = arr[:mid] = [:1] = [7] and right = [1:] = [4] ,Than come to the "mergesort(left) = [7]" So goto the again "n" , n = 1 ,check if ,(Suppose if condtion is True than run this cycle
        # suppose False to while condition .)  check if 1 < 1 = False and again check mergesort(right) = [4] - This also false . Now it merges [7] and [4]; and it l1 and l2 = 1 because len(left) and len(right) = 1
        mergesort(left)
        mergesort(right)

        i = 0
        j = 0
        k = 0
        while i < l1 and j < l2: 
            if left[i] < right[j]:
                arr[k] = left[i]
                i = i + 1
            else:
                arr[k] = right[j]
                j = j + 1
            k = k + 1

        while i < l1: # check len(left)
            arr[k] = left[i]
            i = i + 1
            k = k + 1

        while j < l2: # check len(righ)
            arr[k] = right[j]
            j = j + 1
            k = k + 1


arr = [7, 4, 1, 5, 3]
mergesort(arr)
print("merge sort :", arr)


a = ["H","A","R","S","H","A","L"]
n = len(a)
for i in range(n - 1,0,-1):
    for j in range(0,i):
        if a[j] > a[j + 1]:
            temp = a[j + 1]
            a[j + 1] = a[j]
            a[j] = temp
print(a)
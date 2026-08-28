print("--------------------- 1 --------------------- ")

for i in range(4):  # i = 0,1,2,3
    for j in range(4):  # j = 0 ,1,2,3
        # The end parameter is used with the print() function to decide what should be printed after the output
        print("*", end=" ")  # end = " " stay in one line with print space
    print()  # use print() move the next line

print("--------------------- 2 --------------------- ")

for i in range(1, 5):  # i starting 1,2,3,4
    for j in range(i):  # j = i suppose i = 1 than also j = i = 1
        print("*", end=" ")
    print()

print("--------------------- 3 --------------------- ")

for i in range(1, 5):  # i = 1,2,3,4
    for j in range(1, i + 1):  # (1, i + 1) suppose i = 1  , So j = (1,i+1) = (1,2) = 1
        print(j, end=" ")
    print()  # move the next line

print("--------------------- 4 --------------------- ")

for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()

print("--------------------- 5 --------------------- ")

for i in range(4, 0, -1):  # 4,3,2,1
    for j in range(i):
        print("*", end=" ")
    print()

print("--------------------- 6 --------------------- ")
for i in range(4, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")

    print()
print("--------------------- 7 --------------------- ")
for i in range(1, 5):
    for j in range(4 - i):
        print(" ", end=" ")  # print space in the output
    for j in range(2 * i - 1):
        print("*", end=" ")

    print()

print("--------------------- 8 --------------------- ")
for i in range(4, 0, -1):
    for j in range(4 - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        # end="" tells Python:  "Don't move to the next line after printing.
        print("*", end=" ")

    print()

print("--------------------- 9 --------------------- ")

for i in range(1, 5):
    for j in range(4 - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()  # move the next line

for i in range(4, 0, -1):
    for j in range(4 - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()

print("--------------------- 10 --------------------- ")
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(3, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print("--------------------- 11 --------------------- ")
for i in range(1, 5):
    for j in range(i):
        # check the condition (i + j) % 2 Suppose i = 1, j = (1) = (start the 0 and stop the 1 means) j = 0  Than = (1 + 0) % 2 = 1 % 2 = reminder =  1 So print 1.
        print((i + j) % 2, end=" ")
    print()

print("--------------------- 12 --------------------- ")
for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end=" ")
    for j in range(2*(4 - i)):
        print(" ", end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")

    print()

print("--------------------- 13 --------------------- ")
num = 1
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num = num + 1
    print()

print("--------------------- 14 --------------------- ")

letters = "ABCD"
for i in range(len(letters)):  # i = 4 = 0,1,2,3
    for j in range(i + 1):  # j = i + 1 = 0 + 1 = 1,So j = (1) = 0
        print(letters[j], end=" ")  # letters[0] = "A"
    print()

print("--------------------- 15 --------------------- ")
letters = "ABCD"
for i in range(len(letters), 0, -1):
    for j in range(i):
        print(letters[j], end=" ")
    print()

print("--------------------- 16 --------------------- ")
letters = "ABCD"
for i in range(len(letters)):
    for j in range(i + 1):
        print(letters[i], end=" ")
    print()

print("--------------------- 17 --------------------- ")
letters = "ABCD"
n = len(letters)
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(letters[j], end=" ")
    for j in range(i - 1, -1, -1):
        print(letters[j], end=" ")
    print()

# letters = "ABCD"
# n = len(letters)
# i = 0
# while i < n:
#     j = 0
#     while j < n - i - 1:
#         print(" ", end=" ")
#         j += 1
#     j = 0
#     while j <= i:
#         print(letters[j], end=" ")
#         j += 1 # j = j + 1
#     j = i - 1
#     while j >= 0:
#         print(letters[j], end=" ")
#         j -= 1 # j = j - 1
#     print()
#     i += 1

print("--------------------- 18 --------------------- ")
letters = "DCBA"
for i in range(len(letters)):
    for j in range(i, - 1, -1):
        print(letters[j], end=" ")
    print()

print("--------------------- 19 --------------------- ")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    for j in range(2 * (5 - i)):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    for j in range(2 * (5 - i)):
        print(" ", end=" ")
    for j in range(i, 0, -1):
        print("*", end=" ")
    print()

print("--------------------- 20 --------------------- ")
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    for j in range(2 * (4 - i)):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(3, 0, -1):
    for j in range(i):
        print("*", end=" ")
    for j in range(2 * (4 - i)):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()


print("--------------------- 21 --------------------- ")

for i in range(5):
    for j in range(5):
        if i == 0 or i == 5 - 1 or j == 0 or j == 5 - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("--------------------- 22 --------------------- ")

n = 4
size = 2 * n - 1
for i in range(size):
    for j in range(size):
        top = i
        left = j
        bottom = size - 1 - i
        right = size - 1 - j
        print(n - min(top, left, bottom, right), end=" ")
    print()



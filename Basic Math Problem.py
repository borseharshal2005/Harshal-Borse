print("*** Basic Math Problem ***")
print("-----1 . count all digits of number-----")
n = 1234
count = 0
while n > 0:  # while loop check n is greater
    count += 1
    n = n // 10  # it's a floor division operator suppose 1234 / 10 = 123.4 - return float but 1234 // 10 - remove the decimal part and return the intger value 123
print(count)  # 4
print("=====or=====")
n = 1234
# str(n) = convert the number in to string = "1234" than count the string and print
count = len(str(n))
print(count)  # 4

print("====or=====")
n = 1234
count = 0
for i in str(n):
    count = count + 1
print(count)  # 4


print("------2 . Reverse the number------")
n = 1234
rev = 0
while n > 0:
    ld = n % 10
    rev = (rev * 10) + ld
    n = n // 10
print(rev)  # 4321
print("-------or-------")
n = 1234
rev = ""  # rev "" means stored the reverse number
while n > 0:
    ld = n % 10
    rev = rev + str(ld)
    n = n // 10
print(rev)  # 4321
print("------or-------")
n = 2580
rev = 0
count = len(str(n))
for i in range(count):
    digit = n % 10
    rev = (rev * 10) + digit
    n = n // 10
print(rev)  # 852

print("-------3 . Palindrome number --------")
n = 121
rev = 0
temp = n
while n > 0:
    ld = n % 10
    rev = (rev * 10) + ld
    n = n // 10
if temp == rev:  # the check condition temp value = rev value
    print("Palindrome")  # number is palindrome
else:
    print("Not Palindrome")


n = 122
rev = 0
temp = n

for i in range(len(str(n))):
    ld = n % 10
    rev = (rev * 10) + ld
    n = n // 10
if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")  # number is not palindrome

print("------4 . GCD of two number -------")
n1 = 4
n2 = 6
gcd = 0
for i in range(1, min(n1, n2) + 1):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i
print(gcd)  # 2

n1 = 4
n2 = 6
gcd = 0
i = 1
while i <= min(n1, n2):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i
    i = i + 1

print(gcd)  # 2

print("--------5 . Armstrong number-------")
n = 153
sum = 0
temp = n
while n > 0:
    rem = n % 10
    sum = sum + rem ** 3
    n = n // 10
if temp == sum:
    print("Armstrong")  # number is armstrong
else:
    print("Not Armstrong")

n = 2000
sum = 0
temp = n
for i in str(n):
    rem = n % 10
    sum = sum + (rem * rem * rem)
    n = n // 10
if temp == sum:
    print("Armstrong")
else:
    print("Not Armstrong")  # number is not armstrong

print("------6 . Print all divisors ------")
def divisors(n):
    ans  = []
    i = 1
    while  i <= n:
        if n % i == 0 :
            ans. append(i)
        i += 1
    return ans

print(divisors(6))

n = 5
ans = []
for i in range(1, n + 1):
    if n % i == 0:
        # if condition is success to add the number suppose i = 1 = 5 % 1 == 0 it's True to add the number
        ans.append(i)
print(ans)  # answer in square braket -> [1,5]

n = 8
for i in range(1, n + 1):  # (1,9) = 1,2,3,4,5,6,7,8
    if n % i == 0:
        print(i)  # -> 1,2,4,8


print("-------7. Prime number -------")

n = 7
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1
if count == 2:
    print("Prime")  # number 7 is prime
else:
    print("Not Prime")

n = 8
i = 1
count = 0
while i <= n:
    if n % i == 0:
        count += 1
    i += 1
if count == 2:
    print("Prime")
else:
    print("Not Prime")  # number 8 is not  prime

#Name:Wyatt Toler
#Class: 5th Hour
#Assignment: HW10

import random as r

#1. Print "Hello World!"
print("Hello World")
#2. Create 3 variables that each randomly generate a number between 1 and 10, named A, B, and C.
A = r.randint(1,10)
B = r.randint(1,10)
C = r.randint(1,10)
#3. Print A, B, and C on the same line.
print(A , B , C)
#4. Make an if statement that prints if variable A is greater than, less than, or equal to 5.
if A > 5:
    print(A, "is Greater then 5")
if A < 5:
    print(A, "is Less then 5")
if A == 5:
    print(A, "is equal to 5")
#5. Make an if statement that prints if variable B is between 3 and 7, or not.
if B > 3 and B < 7:
    print(B, "is between 3 and 7")
#6. Make an if statement that prints if variable C is even or odd.
if C % 2 == 0:
    print(C, "is even")
else:
    print(C, "is odd")
#7. Create a variable whose value is 3 + a randomly generated number between 1 and 20
RandomSum = 3+r.randint(1,20)
#8. Make an if statement that prints if the variable from #7 is greater than, less than, or equal to A + B + C.
if RandomSum > A + B + C:
    print(RandomSum, "is greater than A + B + C")
if RandomSum < A + B + C:
    print(RandomSum, "is less than A + B + C")
if RandomSum == A + B + C:
    print(RandomSum, "is equal to A + B + C")



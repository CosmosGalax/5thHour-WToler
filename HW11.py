#Name:Wyatt Toler
#Class: 5th Hour
#Assignment: HW11

import random as r

#1. Print "Hello World!"
print("Hello World")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
ListRandomabc = [r.randint(1, 100), r.randint(1, 100), r.randint(1, 100)]
#3. Print the list.
print(ListRandomabc)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if ListRandomabc[0] > ListRandomabc[1]:
    if ListRandomabc[0] > ListRandomabc[2]:
        print(ListRandomabc[0], "is the highest")
        H = ListRandomabc[0]
if  ListRandomabc[1] > ListRandomabc[0]:
    if ListRandomabc[1] > ListRandomabc[2]:
        print(ListRandomabc[1], "is the highest")
        H = ListRandomabc[1]
if ListRandomabc[2] > ListRandomabc[0]:
    if ListRandomabc[2] > ListRandomabc[1]:
        print(ListRandomabc[2], "is the highest")
        H =ListRandomabc[2]
#5. Tie the result (the largest number) from #4 to a variable called "num".
num = H
print(num)
#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 3 == 0 and num % 2 == 0:
    print("Both is divisible by 3 and 2")
elif num % 2 == 0:
    print("divisible by 2")
elif num % 3 == 0:
    print("divisible by 3")
else:
    print(num, "is not divisible by both 2 and 3")
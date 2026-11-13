#Name:Wyatt Toler
#Class: 5th Hour
#Assignment: HW15

import time, random, math
#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.
for i in range(5,0,-1):
    time.sleep(0.3)
    print(i)
else:
    print("Hello World")
#2. Create a for loop that counts up and prints only even numbers between 1 and 30.
for c in range(0, 32, 2):
    print(c)
#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.
for c in range(0, 31):
    if c % 3 == 0:
        continue
    else:
        print(c)
#4. Create a for loop that prints 5 different animals from a list.
for l in ["dog", "cat", "bird", "snake", "zebra"]:
    print(l)
#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
text = input("Name a word")
reversedText = text[::-1]
for d in reversedText:
    print(d)
#6. Create a list containing 10 integers of your choice and print the list.
Listint = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), ]
#7. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = []
oddNumbers = []
#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.
for u in range(len(Listint)):
    if Listint[u] % 2 == 0:
        evenNumbers.append(Listint[u])
    else:
        oddNumbers.append(Listint[u])
print(Listint)
print(evenNumbers)
print(oddNumbers)
#9. Create a variable that asks the user for an integer and an empty integer variable.
intInput = int(input("Enter a number"))
empInt = 1
#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)
for e in range (1, intInput+ 1):
    empInt = empInt * e
print(empInt)
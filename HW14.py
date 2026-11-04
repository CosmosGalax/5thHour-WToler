#Name:Wyatt Toler
#Class: 5th Hour
#Assignment: HW14
import random
import time
#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
Clock = 5
while Clock >= 1:
    print(Clock)
    Clock -= 1
    if Clock == 0:
        print("Hello World")
        break
#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
N = 1
while True:
    if 1 <= N <= 30:
        if N % 2 == 0:
            print(N)
            N += 1
        else:
            N += 1
    else:
        break
#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
N2 = 1
while True:
    if 1 <= N2 <= 29:
        N2 += 1
        if N2 % 3 == 0:
            continue
        print(N2)
    else:
        break
#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
N3 = random.randint(1, 6)
while N3 != 1:
    print(N3)
    N3 = random.randint(1, 6)
else:
    print("Has Hit 1")
#5. Create a while loop that asks for a number input until the user inputs the number 0.
while input("enter a number:") != "0":
    print("Not that one")
else:
    print("There you go, I like that one!")
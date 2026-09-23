#Name:Wyatt Toler
#Class: 5th Hour
#Assignment: HW8

#1. Import the "random" library
import random
#2. print "Hello World!"
print("Hello World")
#3. Create three different variables that each randomly generate an integer between 1 and 10
R1 = random.randint(1, 10)
R2 = random.randint(1, 10)
R3 = random.randint(1, 10)
#4. Print the three variables from #3 on the same line.
print(R1, R2, R3)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
R1two = R1 + 2
R2four = R2 - 4
R3onepointfive = R3 * 1.5
#6. Print each result from #5 on the same line.
print(R1two, R2four, R3onepointfive)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
RL1 = random.randint(1, 6)
RL2 = random.randint(1, 6)
RL3 = random.randint(1, 6)
RL4 = random.randint(1, 6)
RList = [RL1, RL2, RL3, RL4]
print(RList)
#8. Sort the list in #7 and print it.
RList.sort()
print(RList)
#9. Add together the highest three numbers in the list from #7 and print the result.
RList.sort(reverse=True)
print(RList[0] + RList[1] + RList[2])
#10. Create a list with 5 names of other students in this class and print the list.
StudentList = ["Wyatt", "Santi", "Oliver", "Anthony", "Max"]
print(StudentList)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(StudentList)
print(StudentList)
#12. Print a random choice from the list of names from #10.
print(random.choice(StudentList))
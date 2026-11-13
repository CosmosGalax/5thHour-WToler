#Name:Wyatt Toler
#Class: 5th Hour
#Assignment: HW16
import enchant
#1. import the "random" library
import random
dictionary = enchant.Dict("en_US")
#2. print "Hello World!"
print("Hello World")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a = int(input("Enter a number"))
b = int(input("Enter another number"))
c = int(input("Enter another number"))
#4. Add a and b together, then divide the sum by c. Print the result.
print((a + b)/c)
var = ((a + b)/c)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
print(var)
if round(var) % 2 == 0:
    print("even")
else:
    print("odd")
#6. Create a list of five different random integers between 1 and 10.
randlist = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
#7. Print the 4th number in the list.
print(randlist)
print(randlist[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
randlist.append(random.randint(1, 10))
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
randlist.sort()
print(randlist)
print(randlist[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i = 0
while i < 100:
    print(i)
    i += 1
    if i > 100:
        break
#11. Create a list containing the names of five other students in the classroom.
namelist = ["santi", "oliver", "jake", "cruz", "max"]
#12. Create a for loop that individually prints out the names of each student in the list.
for u in namelist:
    print(u)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
for t in range(1, 101):
    if t % 10 == 0:
        break
    else:
        print(t)
#14. Free space. Do something creative. :)
## random name picker
prefixes = ["king ", "queen ", "Mr.", "Mrs.", "Miss.", "Ms.", "Mx.", "Dr.", "Prof.", "Rev.", "Capt.", "Sir ", "Dame ", "Lord ", "Lady ", ""]
Random_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i","j","k",'l','m','o','p','q','r','s','t','u','v','x','y','z']
suffixes = ["Jr.","", "Senior."]
FinalName = []
for p in range(5):
    name = random.choice(Random_letters)
    FinalName.append(name)
FinalFinalName = str("".join(FinalName))
while not dictionary.check(FinalFinalName):
    for p in range(5):
        name = random.choice(Random_letters)
        FinalName.append(name)
    FinalFinalName = str("".join(FinalName))
    FinalName = []
else:
    print(random.choice(prefixes) + FinalFinalName, "" + random.choice(suffixes))


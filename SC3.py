#Name:Wyatt Toler
#Class: 5th Hour
#Assignment: SC3

#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".

#Create a while loop that follows the rules of the game.
Number = 1
while 1 <= Number <= 100:
    Number += 1
    if Number % 3 == 0 and Number % 5 == 0:
        print("FizzBuzz")
    elif Number % 3 == 0:
        print("Fizz")
    elif Number % 5 == 0:
        print("Buzz")
    else:
        print(Number)

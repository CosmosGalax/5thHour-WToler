#Name:Wyatt Toler
#Class: 5th Hour
#Assignment: SC4

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.
APlayers = int(input("Amount of players: "))
total = 0
for i in range(APlayers-1):
    rate = int(input("What do you wanna rate the model from 1 to 5: "))
    while not 5 > rate > 0:
        print("Error Out Of Range")
        rate = int(input("What do you wanna rate the model from 1 to 5: "))
    else:
        total += rate
print(total / (APlayers-1))
#Name:Wyatt Toler
#Class: 5th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.

enemys = {
    "Enemy1" :  {
        "Damage" : 5,
        "HP" : 10,
        "Speed" : 10,
        "Wisdom" : 1,
        "Mana" : 0
    },
    "Enemy2" :  {
        "Damage" : 20,
        "HP" : 2,
        "Speed" : 4,
        "Wisdom" : 0,
        "Mana" : 0
    },
    "Enemy3" :  {
        "Damage" : 3,
        "HP" : 5,
        "Speed" : 30,
        "Wisdom" : 0,
        "Mana" : 0
    },
    "Enemy4" :  {
        "Damage" : 10,
        "HP" : 15,
        "Speed" : 10,
        "Wisdom" : 5,
        "Mana" : 20
    },
    "Enemy5" :  {
        "Damage" : 40,
        "HP" : 1,
        "Speed" : 20,
        "Wisdom" : 10,
        "Mana" : 40

    }
}

print("do you wanna change Values?")
if input("Y/N").lower() == "y":
    print("What Enemy?(1, 2, 3, 4, 5)")
    while True:
        UserInput = input()
        if UserInput == "1":
            enemys["Enemy1"]["Damage"] = int(input("Damage: "))
            print(enemys["Enemy1"]["Damage"], "Is now the new Enemy Damage Change another?(Y/N)")
        elif UserInput == "2":
            enemys["Enemy2"]["Damage"] = int(input("Damage: "))
            print(enemys["Enemy2"]["Damage"], "Is now the new Enemy Damage Change another?(Y/N)")
        elif UserInput == "3":
            enemys["Enemy3"]["Damage"] = int(input("Damage: "))
            print(enemys["Enemy3"]["Damage"], "Is now the new Enemy Damage Change another?(Y/N)")
        elif UserInput == "4":
            enemys["Enemy4"]["Damage"] = int(input("Damage: "))
            print(enemys["Enemy4"]["Damage"], "Is now the new Enemy Damage Change another?(Y/N)")
        elif UserInput == "5":
            enemys["Enemy5"]["Damage"] = int(input("Damage: "))
            print(enemys["Enemy5"]["Damage"], "Is now the new Enemy Damage Change another?(Y/N)")
        elif UserInput == "N":
            break
        elif UserInput == "Y":
            print("What Enemy?(1, 2, 3, 4, 5)")
        else :
            print("Invalid Input")
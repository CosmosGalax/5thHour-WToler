import random
AmountOfJackpots = 0
CountTillJackpot = 2
JackpotTries = []
Tries = int(input("How many Tries would you like?"))
for _ in range(Tries) :
    Slot1 = random.randint(1, 9)
    Slot2 = random.randint(1, 9)
    Slot3 = random.randint(1, 9)
    SlotList = [Slot1, Slot2, Slot3]
    print(SlotList)
    CountTillJackpot = CountTillJackpot + 1
    if SlotList[0] and SlotList[1] and SlotList[2] == 7:
        AmountOfJackpots += 1
        print(SlotList)
        print("Found Jackpot in", str(CountTillJackpot), "tries")
        JackpotTries.append(CountTillJackpot)
        CountTillJackpot = 2
print("Total about of Jackpots for", Tries, "Tries is", AmountOfJackpots, "or", str(round(Tries/AmountOfJackpots, 2))+ "% chance")
JackpotTries = []
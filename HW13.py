#Name:Wyatt Toler
#Class: 5th Hour
#Assignment: HW13
import random
print("Hello World")
#1. Import the random function

#2. Create a variable called 'temp' that randomly generates a number between 1 and 30
temp = random.randint(1,30)
print(temp)
#3. Go to the link below and convert the code into pseudocode in comments, then code the flowchart completely:
#https://adacomputerscience.org/images/content/computer_science/design_and_development/program_design/figures/ada_cs_design_flow_ifelseif.svg
#if temp > 20
    #read it's hot
    #read Thank you!
#else if temp > 10
    #read it's mild
    #read Thank you!
#else
    #read it's cold
    #read Thank you!
if temp > 20:
    print("it's hot")
elif temp > 10:
    print("it's mild")
else:
    print("it's cold")
print("Thank you!")
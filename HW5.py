#Name:Wyatt Toler
#Class: 5th Hour
#Assignment: HW5

#1. Print Hello World!
print("Hello World!")
#1. Create a list with 5 strings containing 5 different names in it.
Strg_List = ["Steve", "Bob", "John", "Jeff", "Sheldon"]
print(Strg_List)
#2. Append a new name onto the Name List.
Strg_List.append("Penny")
#3. Print out the 4th name on the list.
print(Strg_List, 3)
#4. Create a list with 4 different integers in it.
Num_list = [1, 2, 3, 4, 5]
#5. Insert a new integer into the 2nd spot and print the new list.
Num_list.insert(1, 2.5)
print(Num_list)
#6. Sort the list from lowest to highest and print the sorted list.
Num_list.sort()
print(Num_list)
#7. Add the 1st three numbers on the sorted list together and print the sum.
Num_List_3_Total = Num_list[0] + Num_list[1] + Num_list[2]
print(Num_List_3_Total)
#8. Create a list with two strings, two variables, and too boolean values.
Mixed_list = ["One", "Two", 1 , 2, True, False]
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(Mixed_list[int(input("Enter Index"))])
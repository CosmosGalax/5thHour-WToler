#Name:Wyatt Toler
#Class: 5th Hour
#Assignment: HW6

print("Hello World!")
#1. Create a list with 9 different numbers inside.
Num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(Num_list)
#2. Sort the list from highest to lowest.
Num_list.sort(reverse=True)
print(Num_list)
#3. Create an empty list.
Na_list = []
#4. Remove the median number from the first list and add it to the second list.
Na_list.append(Num_list.index(4))
Num_list.pop(4)
print(Na_list)
#5. Remove the first number from the first list and add it to the second list.
Na_list.append(Num_list[0])
Num_list.pop(0)
#6. Print both lists.
print(Num_list)
print(Na_list)
#7. Add the two numbers in the second list together and print the result.
Na_list_sum = sum(Na_list)
print(Na_list_sum)
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
Num_list.insert(5 , 5)
Num_list.sort(reverse=True)
print(Num_list)
#9. Sort the first list from lowest to highest and print it.
Num_list.sort()
print(Num_list)
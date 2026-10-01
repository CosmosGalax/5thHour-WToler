#Name:Wyatt Toler
#Class: 5th Hour
#Assignment: HW9
import random
#1. Print Hello World!
print("Hello World")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
dict = {
    "one" : 1,
    "two" : 2,
    "Numbers" : [1,57,19,39,10]
}
#3. Print the keys of the dictionary from #2.
print(dict.keys())
#4. Print the values of the dictionary from #2
print(dict.values())
#5. Print one of the three numbers from the list by itself
print(dict["Numbers"][random.randint(0,4)])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
dict.update({"Name" : "Wyatt Toler"})
#7. Print the entire dictionary from #2 with the updated key and value.
print(dict)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
Student = {
    'student1' : {
        'name' : 'Santi',
        'age' : 14,
        'Grade' : '9th'
    },
    'student2': {
        'name': 'Anthony',
        'age': 14,
        'Grade': '9th'
    },
    'student3': {
        'name': 'Oliver',
        'age': 14,
        'Grade': '9th'
    }
}
#9. Print the names of all three classmates on the same line.
print(Student['student1']['name'], Student['student2']['name'], Student['student3']['name'])
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
Student.pop('student1')
print(Student)
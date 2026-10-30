import random as r
List_To_Sort = [r.randint(1,100), r.randint(1,100), r.randint(1,100), r.randint(1,100), r.randint(1,100)]
list_length = len(List_To_Sort)
Index = 0
picked_Value = List_To_Sort[Index]
print(List_To_Sort)
Remove = List_To_Sort.pop(Index + 1)
def Swap():
    global Index
    global List_To_Sort
    global picked_Value
    List_To_Sort.insert(Index-1, Index + 1)
    List_To_Sort.pop(List_To_Sort[Index+1])
def Check():
    global Index
    global Remove
    print(Index)
    picked_Value = List_To_Sort[Index]
    print("Picked Value: ", picked_Value)
    print(List_To_Sort[Index + 1])
    if picked_Value > List_To_Sort[Index + 1]:
        Swap()
        Index = Index + 1
    else:
        print("Passed")
    print(Index)


for i in range(list_length - 1):
    Check()
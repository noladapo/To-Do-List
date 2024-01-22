#aminat & nike 
# 1/11/24
# to do list 

list = []

#this function allows people to make a list and add remove or mark things as complete or clear the list and more 
def toDo():
    print("Welcome to To do list ")
    print("Please choose an operation: (Type in a number between 1 - 8)")
    print("1.Add to list  \n2.View list \n3.Mark as done \n4.Remove a task from the to-do list \n5. Remove all tasks \n6. Sort List Alphabetically   \n7. Print the numbers of items on the list \n8. Quit ")
    option = int(input("option: "))
    while True:
        if(option == 8):
            break
        elif (option == 1):
            x = (input ("What would you like to add?"))
            list.append(x)
        elif (option == 2):
            print(list)
        elif (option == 3):
            change = input("what would you like to mark complete?")
            new = list.index(change)
            list[new] = (change + " X")
        elif (option == 4):
            leave=(input("What would you like to remove?"))
            list.remove(leave)
        elif (option == 5):
            list.clear()
        elif (option == 6):
            list.sort()
            print(list)
        elif (option == 7):
            x = len(list)
            print(x)
        toDo()
#main
toDo()
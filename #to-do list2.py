#to-do list2
#Kayla McClendon
#1-12-24
#5. Remove all items 


#starter to mka ethe intial list for the user
print("make a to-do list with 5 items!!")
todoList = [input("Add an item")]
for i in range (4):
    todoList.append(input("add another"))
print(todoList)

#function to run the code again
def again():
    next = input ("would you like to continue")
    next = next.capitalize()
    if next == "Yes":
        toDo()
    elif next == "No":
        end()
#ends the code
def end():
    print("Bye-Bye :)!")
#gives the users options regarding the previously made list
def toDo():
    global todoList
    ans = input("Which option would you like, 1-8")
    #ask the user to add a single task to their list
    if ans == "1":
        todoList.append(input ("add a task"))
        again()
    #displays the current list
    elif ans == "2":
        print (todoList)
        again()
    
    #marks an item the list that the user stated is completed
    elif ans == "3":
        com = input(print(todoList,"Which one have you completed?"))
        i = todoList.index(com)
        todoList[i] = com + "X"
        print(todoList)
        again()
    
    #allows the user to remove an item off of the list
    elif ans == "4":
        r = input(print(todoList,"Which one do you want to remove?"))
        todoList.remove(r)
        print(todoList)
        again()
    
    #clears list
    elif ans == "5":
        todoList.clear()
        print("your list is now empty. If you wish to run again you must go to option one")
        again()
    #sorts the list in alphabetical order
    elif ans == "6":
        todoList.sort()
        print(todoList)
        again()
    
    #Tells you the number of items on your list
    elif ans == "7":
        print("There are",len(todoList), "items on your list.")
        again()
  
    #ends the program
    elif ans == "8":
        end()
    #Informs user of their mistake and re runs the program
    else:
        print ("not an option, try again")
        toDo()
#main
toDo()
print("Hello I'm a shopping list!")
shopping_list = [] #create the initial list

while True:
    
    
    print("Enter d to display list, a to add an item, r to remove an item at an index, q to quit:")
    #take the user's choice
    option = input()
    
    if (option == 'd'):
        print("Here is your shopping list:")
        for item in shopping_list:
            print("-"+item)
            
    elif (option == 'a'):
        print("Enter the item you want to add:")
        item = input()
        shopping_list.append(item)
        
    elif (option == 'r'):
        print("Enter the index you want to remove:")
        index = input()
        index = int(index)
        del shopping_list[index]
    elif (option == 'q'):
        print("Bye!")
        break

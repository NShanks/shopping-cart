def storeInfo():
    d = {}
    def showList(): # new function to show the list of stores to visit so I don't have to type this a million times.
        print("")
        print("-------Store List-------")
        print("")
        for key in d.keys():
            print(key, ':', d[key])
        print("")
        print("------------------------")
        print("")
    

    while True:
        # First decision a user makes
        print("Type 'store' to add stores")
        print("Type 'add' to add items to stores")
        print("Type 'delete' to delete items from stores")
        print("Type 'show' to see your lists")
        print("Type 'quit' to quit")
        choice = input("What would you like to do? ")
        print("")
        
        # First option. Adding stores to the dictionary
        if choice.lower() == "store":
            choosing = True # Not sure what this does but I think it makes the while loop work. Would while True also work?
            while choosing == True:
                store = input("What stores do you want to add to your list? ")
                print("Type 'quit' to quit")
                if store.lower() != "quit":
                    d[store] = "" # this takes the input and assigns it nothing. dict[key] = value. I need the value to be an empty list.
                    d.update( {store : []})
                else:
                    showList()
                    break


        # Second option. Adding items to the store. Users will get another input to choose what store to add items to.
        elif choice.lower() == "add":
            if bool(d) == False: # Checks if the dictionary is empty. If it is, send user back to start. Otherwise, run the rest of the add code.
                print("You have to add stores first")
                print("")
            else:
                showList()
                storeChoice = input("What store do you want to add item to? ")
                print("")
                if storeChoice.lower() in d.keys(): # if the input matches a store name, it will start to add to that stores list.
                    choosing = True
                    while choosing == True:
                        item = input(f"What item do you want to add to your {storeChoice.title()} list? ")
                        print("")
                        print("Type 'quit' to stop adding items.")
                        if item.lower() != "quit":
                            d[storeChoice.lower()].append(item) # Append the input to key's value in the dictionary
                        else:
                            print("")
                            print(f"The following are items on your {storeChoice.title()} list ")
                            print(d[storeChoice.lower()], sep="/n")
                            print("")
                            break
                else:
                    print("")
                    print("Store doesn't exist. Please try again")
                    print("")
                    

        elif choice.lower() == "delete":
            if bool(d) == False: # Checks if the dictionary is empty. If it is, send user back to start. Otherwise, run the rest of the add code.
                print("You have to add stores first")
                print("")
            else:
                showList()
                storeChoice = input("What store do you want to remove an item from? ")
                print("")
                if storeChoice.lower() in d.keys(): # if the input matches a store name, it will start to add to that stores list.
                    if bool(d[storeChoice]) == False: # Checks if the store list is empty. If it is, send user back to start. Otherwise, run the rest of the add code.
                        print("There are no items to remove.")
                        print("")
                    else:
                        if storeChoice not in d.keys():
                            print("----------------------------------------------------------asfasdfasdfsd")
                            print("Store doesn't exist. Please try again")
                            print("")
                        elif storeChoice.lower() in d.keys(): # if the input matches a store name, it will start to remove from that stores list.
                            choosing = True
                            while choosing == True:
                                showList()
                                item = input(f"What item do you want to remove from your {storeChoice.title()} list? ")
                                print("Type 'quit' to return to the main menu.")
                                print("")
                                if item.lower() in storeChoice.lower(): #-------------------------------------------------------------------------------------------------------------------------------------------
                                    d[storeChoice.lower()].remove(item) # Remove the input from the value in the dictionary
                                    print("item removed")
                                elif item.lower()  == "quit":
                                    print("")
                                    print(f"The following are items on your {storeChoice.title()} list ")
                                    print(d[storeChoice.lower()], sep="/n")
                                    print("")
                                    break
                                else:
                                    print("")
                                    print("Item not found. Please try again")
                                    print("")
                else:
                    print("")
                    print("Store doesn't exist. Please try again")
                    print("")

        elif choice.lower() == "show":
            showList()


        else:
            print("")
            print("Invalid input. Please try again")
            print("")

storeInfo()
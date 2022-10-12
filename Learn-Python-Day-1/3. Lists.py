List = ["ListItem1","ListItem2","ListItem3","ListItem4"]

def intValueInput(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Value is not an integer")
            continue
        else:
            return userInput
            break

def strValueInput(message):
    while True:
        try:
            userInput = str(input(message))
        except ValueError:
            print("Value is not an String")
            continue
        else:
            return userInput
            break



while True:
    selection = intValueInput("Select Which Operation You Want To Use:\n1:Input Into List\n2:Read Value From List\n3: Exit\n")
    
    if selection == 1:
        val = str(input("What do you want to store int the list?\n"))
        List.append(val)
        print("Your input is stored in position: " + str(len(List)))

    elif selection == 2:
        val = intValueInput("Input Value Required: ")
        if val <= len(List):
            print("Value in position " + str(val) + " is : " + List[val-1])
        else:
            print("Please Input an availble location within this list.")




    elif selection == 3:
        cont = strValueInput("Are You Sure You Want To Continue? ")
        if cont.lower() == "y":
            break
        elif cont.lower() =="n":
            continue
        else:
            print("Please input a valid Answer Y or N")
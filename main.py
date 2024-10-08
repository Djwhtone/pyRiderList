import testDB
import model_functions, mf
from nameObj import Riders

def show_group():
    rider_group = input("Enter group: ")
    rider_group = rider_group.upper()
    group = testDB.getGroup(rider_group)

    for x in group:
        print(x)
    print("\n new riders added")

# Stores user feedback into variables
def addRAS():
    name        = input("Name: ")
    shift       = input("Shift: ")
    location    = input("Location: ")
    group_label = input("Group ID: ").upper()

    mf.addRider(name,shift,location,group_label)
    #rider = Riders(name=name, shift=shift, location=location, group_label=group_label) 
    #testDB.addRas(rider)

# Delete riders from DB/list
def delete_rider():
    rider_id = int(input("Rider ID: "))
    temp = testDB.getRider(rider_id)
    print(temp)
    if temp == None:
        print("ID does not exist")
    else:
        command = input(f'Do you want to delete "{temp} ", y,n: ')
        if command == "y":
            testDB.deleteRider(rider_id)
            print(f'Rider "{temp}" was deleted from database.\n')
        else:
            print("Back to list.")


            
# Displays all rider information in the list 
def showAllRiders():
    riders = []
    riders = testDB.showAll()

    for x in riders:
        print(x)
    print()

# Initial menu to guide user
def menu():
    print("Start of the program") # new

    print("add - Enter rider info")
    print("show - Show riders")
    print("del - Delete a rider")
    print("Exit - Exit program")
    print("g - return group") # new

    print()

# Shows all number of riders on each shift - new
def show_shift():
    group = input('Please enter a shift: 1st/2nd/3rd: ')
    holder = testDB.getGroup(group)
    print(group)

# Runs the program and appropiate functions are called by user
def main():
    #rider = []
    testDB.connect()
    menu()

    while True:
        prompt = input("Selection: ")
        if prompt.lower() == 'add':
            addRAS()
        elif prompt.lower() == 'menu':
            menu()
        elif prompt.lower() == 'show':
            showAllRiders()
        elif prompt.lower() == 'del':
            delete_rider()
        elif prompt.lower() == 'g':
            show_group()
            #function for returning shift
        elif prompt.lower() == 'exit':
            break
        else:
            print(f'Invalid Option! "menu" to display options')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


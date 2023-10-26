import sqlite3
import testDB
from nameObj import Riders


def addRAS():
    name        = input("Name: ")
    shift       = input("Shift: ")
    location    = input("Location: ")
    group_label = input("Group ID: ")

    rider = Riders(name=name, shift=shift, location=location, group_label=group_label)
    testDB.addRas(rider)

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

def showAllRiders():
    riders = []
    riders = testDB.showAll()

    for x in riders:
        print(x)
    print()


def menu():
    print("add - Enter rider info")
    print("show - Show riders")
    print("del - Delete a rider")
    print("Exit - Exit program")
    print()


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
        elif prompt.lower() == 'exit':
            break
        else:
            print(f'Invalid Option! "menu" to display options')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


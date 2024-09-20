import testDB
from nameObj import Riders

def addRider(name, shift, location, group):
    rider = Riders(name=name, shift=shift, location=location, group_label=group)
    testDB.addRas(rider)

    
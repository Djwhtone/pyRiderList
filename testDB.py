import sqlite3
from nameObj import Riders

def connect():
    global conn
    conn = sqlite3.connect('riderdb.db')

def createTables():
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE BowlingGreen(name TEXT, shift TEXT, location TEXT, group_label TEXT)')
    conn.commit()

def addRas(rider):
    sql = '''INSERT INTO RasRiders (name, shift, location, group_label)
             VALUES (?,?,?,?)'''
    cursor = conn.cursor()
    cursor.execute(sql, (rider.name,rider.shift,rider.location,rider.group_label))
    conn.commit()


def deleteRider(rider_id):
    sql = '''DELETE FROM RasRiders WHERE riderID = ?'''

    c = conn.cursor()
    c.execute(sql, (rider_id,))
    conn.commit()


def showAll():
    query = '''SELECT * FROM RasRiders'''
    cursor = conn.cursor()
    cursor.execute(query)

    results = cursor.fetchall()

    riders = []
    for x in results:
        riders.append(x)
    return riders

# Allows the selection of riders from the list
def getRider(rider_id):
    query = '''SELECT riderID, name, shift, location, group_label
               FROM RasRiders
               WHERE riderID = ?'''
    c = conn.cursor()
    c.execute(query, (rider_id,))
    row = c.fetchone()
    return row

# Will extract group from riderID possibly
def getGroup(group_label):
    query = '''SELECT riderID, name, shift, location, group_label
               FROM RasRiders 
               WHERE group_label = ?'''
    c = conn.cursor()
    c.execute(query, (group_label))
    row = c.fetchone()
    return row

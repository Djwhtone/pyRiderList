import sqlite3
from typing import List
from nameObj import Riders

def connect():
    global conn
    conn = sqlite3.connect('riderdb.db')

def createTables():
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE BowlingGreen(name TEXT, shift TEXT, location TEXT, group_label TEXT)')
    conn.commit()

def addRas(rider: Riders):
    sql = '''INSERT INTO RasRiders (name, shift, location, group_label)
             VALUES (:name, :shift, :location, :group_label)'''
    cursor = conn.cursor()

    params = {
        "name": rider.name,
        "shift": rider.shift,
        "location": rider.location,
        "group_label": rider.group_label
    }

    cursor.execute(sql, params)
    conn.commit()


def deleteRider(rider_id: Riders):
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
def getRider(rider_id: int):
    query = '''SELECT riderID, name, shift, location, group_label
               FROM RasRiders
               WHERE riderID = :riderID'''
    c = conn.cursor()

    params = {
        "riderID": rider_id
    }

    c.execute(query, params)
    row = c.fetchone()
    return row

# Will extract group from group label 
def getGroup(group_label: str) -> List[Riders]:
    query = '''SELECT riderID, name, shift, location, group_label
               FROM RasRiders 
               WHERE group_label = :group_label'''
    c = conn.cursor()

    params = {
        "group_label": group_label 
    }

    c.execute(query, params)
    rows = c.fetchall() 

    riders = [Rider(*row) for row in rows]

    return riders
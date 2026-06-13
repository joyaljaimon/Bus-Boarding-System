import mysql.connector as mycon
conn = mycon.connect(host='localhost', user='root',
password='1234', database='jj_bbs')
cur = conn.cursor()
bus = None

def nmc(name):
    query = 'select * from student where name=%s'
    tup = (name,)
    cur.execute(query, tup)
    data = cur.fetchall()
    if len(data) == 0:
        return False
    else:
        return True

def board(name):
    global bus
    bus = input("Enter bus no:")
    14
    if bus.isdigit():
        query = 'update student set status="Boarded",bus=%s where
name=%s'
        tup = (bus, name.lower())
        cur.execute(query, tup)
        conn.commit()
        print(name.title(), "has boarded in bus number", bus)
    else:
        print("Invalid bus number")

def deboard(name):
    if nmc(name) == True:
        query = 'update student set status="Deboarded" where
name=%s'
        tup = (name.lower(),)
        cur.execute(query, tup)
        conn.commit()
        print(name.title(), "has deboarded")
    else:
        print("Name not found")

def add(name, phone, gender):
    global student
    15
    if nmc(name) == False:
        query = 'insert into student (name,phone,gender)
values(%s,%s,%s)'
        tup = (name.title(), phone, gender)
        cur.execute(query, tup)
        conn.commit()
        print(name, "has been added")
    else:
        print("Name already exists")

def remove(name):
    if nmc(name) == True:
        query = 'delete from student where name=%s'
        tup = (name.title(),)
        cur.execute(query, tup)
        conn.commit()
        print(name, "has been removed")
    else:
        print("Name not found")

def lst():
    query = "select * from student"
    16
    cur.execute(query)
    data = cur.fetchall()
    for row in data:
        print(row)

def search(name):
    query = "select * from student where name=%s"
    tup = (name,)
    cur.execute(query, tup)
    data = cur.fetchall()
    if len(data) == 0:
        print("Name not found")
    else:
        for row in data:
            print(row)

import csv

def export():
    query = "SELECT * FROM student"
    17
    cur.execute(query)
    data = cur.fetchall()
    with open('student.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Phone', 'Gender', 'Bus No.', 'Status'])
        for row in data:
            writer.writerow(row)
    print("Data exported to student.csv successfully.")

user = "yes"
student = []
bus_details = {}

while user.lower() == "yes":
    action = input("Choose a function \n\t 1) Add Student [Add] \n\t 2)
Remove Student [Remove] \n\t 3) Board Student
18
[Board] \n\t 4) Deboard Student [Deboard]\n\t 5) List
Data [List] \n\t 6)Search [Search] \n\t 7)Export Data
[Export] \n Enter action: ")
    if action.lower() == "add":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        gender = input("Male or Female [M/F]")
        add(name, phone, gender)
    elif action.lower() == "remove":
        name = input("Enter name:")
        remove(name)
    elif action.lower() == "board":
        name = input("Enter name:")
        if nmc(name) == True:
            board(name)
        else:
            print("Student not found")
    elif action.lower() == "deboard":
        name = input("Enter name:")
        if nmc(name) == True:
            deboard(name)
        else:
            print("Student not found:")
    elif action.lower() == "list":
        lst()
    elif action.lower() == "search":
        name = input("Enter name to search")
        search(name)
    elif action.lower() == "export":
        export()
    else:
        print("Invalid Function")
        continue
    user = input("Do you want to continue (yes/no): ")
else:
    if user.lower() == "no":
        quit()
    else:
        print("Invalid Input:")
        print("Quitting Program")
        quit()
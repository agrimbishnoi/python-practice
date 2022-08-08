import pickle
'''
(A)Write menu-driven program using functions for the following operations
on a file of Employees having [Empno,Name,Salary ,Deptt,Phone]:-
1. Create
2. Display entire file
3. Search for an employee whose empno is given.
4. Search for an employee whose name is given
5. Display employees of a given deptt , also count them.
6. Search for an employee whose phone number is given.
7. Search for an employee whose Salary is highest.
8. Delete an employee whose empno is given(don’t use another list/file).
9. Delete employees whose Salary <50000.
10. Append a new employee to the file.
11. Update the salary of employee whose empno is given by 10%
bonus.(Don’t use another file/list.)
'''


def create():
    f = open('emp.dat', 'wb')
    while True:
        no = int(input("Input admission number : "))
        name = input("Enter name string : ")
        sal=int(input("Enter salary number : "))
        dep=int(input("Enter department number: "))
        ph=int(input("Enter phone number : "))
        s = [no,name,sal,dep,ph]
        pickle.dump(s, f)
        ask = input("Repeat? : ")
        if ask in 'Nn':
            break
    f.close()


def display1():
    f = open('emp.dat', 'rb')
    try:
        while True:
            emp = pickle.load(f)
            print(emp)
    except EOFError:
        f.close()


def display2(location):
    f = open(location, 'rb')
    try:
        while True:
            emp = pickle.load(f)
            print(emp)
    except EOFError:
        f.close()


def search1(num):
    flag = False
    f = open('emp.dat', 'rb')
    try:
        while True:
            emp = pickle.load(f)
            if emp[0] == num:
                flag = True
                print(emp)
                break
    except EOFError:
        f.close()
    if flag==True:
        print("found!")
    else:
        print("Not found!")


def search2(name):
    flag = False
    f = open('emp.dat', 'rb')
    try:
        while True:
            emp = pickle.load(f)
            if emp[1].lower() == name.lower():
                flag = True
                print(emp)
                break
    except EOFError:
        f.close()
    if flag == True:
        print("found!")
    else:
        print("Not found!")


def search3(name):
    flag = False
    f = open('emp.dat', 'rb')
    c=0
    l=[]
    try:
        while True:
            emp = pickle.load(f)
            if emp[1].lower() == name.lower():
                flag = True
                print(emp)
                c=c+1
                l.append(emp)
    except EOFError:
        f.close()
    if flag==True:
        print("found ",c,"Employees with name ",name)
        for p in l:
            print(p)
    else:
        print("Not found!")




def search4(phone):
    flag = False
    f = open('emp.dat', 'rb')
    try:
        while True:
            emp = pickle.load(f)
            if emp[4] == phone:
                flag = True
                print(emp)
                break
    except EOFError:
        f.close()
    if flag == True:
        print("found!")
    else:
        print("Not found!")


def count_dept(dno):
    f = open('emp.dat', 'rb')
    c=0
    try:
        while True:
            emp=pickle.load(f)
            if emp[3]==dno:
                c+=1
    except EOFError:
        f.close()
    if c==0:
        print("Not found")
    else:
        print(c,"employees in department number ",dno)


def highest_sal1():
    f = open('emp.dat', 'rb')
    high=0
    try:
        while True:
            e=pickle.load(f)
            if e[2]>high:
                temp=e
                high=e[2]
    except EOFError:
        f.close()
    print(temp,"has highest salary of ",high)


def highest_sal2():
    f = open('emp.dat', 'rb')
    high = 0
    try:
        while True:
            e = pickle.load(f)
            if e[2] > high:
                high = e[2]

    except EOFError:
        f.close()
    print("highest salary is ", high)

import os

def delete(num):
    f=open('emp.dat','rb')
    n=open('temp.dat','wb')
    found=False

    try:
        while True:
            s=pickle.load(f)
            if s[0]!= num:
                pickle.dump(s,n)
            else:
                found=True
    except EOFError:
        f.close()
        n.close()

    if found==True:
        print("Record found and deleted.")
    else:
        print("Counld not find the record")

    os.remove('emp.dat')
    os.rename('temp.dat','emp.dat')



def update1(num):
    f=open('emp.dat','rb')
    l=[]
    try:
        while True:
            e=pickle.load(f)
            l.append(e)
    except EOFError:
        f.close()
    print(l)
    
    for x in l:
        if x[0]==num:
            x[2]=x[2]+0.1*x[2]
    f=open('emp.dat','wb')
    for x in l:
        pickle.dump(x,f)
    f.close()

#update using seek() and try()

def update2(num):
    
    flag=False
    f=open('emp.dat','rb+')
    try:
        while True:
            pos=f.tell()
            e=pickle.load(f)
            if num==e[0]:
                flag=True
                e[2]=1.1*e[2]
                f.seek(pos)
                pickle.dump(e,f)
                break
    except EOFError:
        f.close()

    if flag==True:
        print("Updated salary")
    else:
        print("Not found record")


print('''
    Menu driven:
    1-Create  - Create and add elements in file
    2-Display1- Filename defaulted as 'emp.dat'
    3-Display2- Filename as argument
    4-Search1 - Employee number
    5-Search2 - Name - Single
    6-Search3 - Name - Multiple
    7-Search4 - Phone number 
    8-Count Department - number of empl
    9-Highest Salary1 - who has the highest salary
    10-Highest Salary2 - what is the highest salary
    11-Delete  - delete a employee
    12-Update1 - using a list
    13-Update2 - seek and tell function
    14-Exit
    ''')

while True:

    command = int(input("Enter command : "))
    if command == 1:
        create()
    elif command == 2:
        display1()
    elif command == 3:
        file= input("Enter file location : ")
        display2(file)
    elif command == 4:
        num = int(input("Enter number : "))
        search1(num)
    elif command == 5:
        name= input("Enter name : ")
        search2(name)
    elif command == 6:
        name = input("Enter name : ")
        search3(name)
    elif command == 7:
        num = int(input("Enter number : "))
        search4(num)
    elif command == 8:
        num = int(input("Enter department number : "))
        count_dept(num)
    elif command == 9:
        highest_sal1()
    elif command == 10:
        highest_sal2()
    elif command == 11:
        num = int(input("Enter number : "))
        delete(num)
    elif command == 12:
        num = int(input("Enter number : "))
        update1(num)
    elif command == 13:
        num = int(input("Enter number : "))
        update2(num)
    elif command ==14:
        break
    else:
        print("Wrong command given ! ")


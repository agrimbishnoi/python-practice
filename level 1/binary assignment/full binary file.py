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


'''


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
    
Enter command : 1
Input admission number : 1
Enter name string : a
Enter salary number : 100
Enter department number: 1
Enter phone number : 4565
Repeat? : y
Input admission number : 2
Enter name string : b
Enter salary number : 200
Enter department number: 2
Enter phone number : 45654
Repeat? : y
Input admission number : 3
Enter name string : c
Enter salary number : 60000
Enter department number: 2
Enter phone number : 4565467
Repeat? : y
Input admission number : 4
Enter name string : d
Enter salary number : 70000
Enter department number: 1
Enter phone number : 5654645
Repeat? : y
Input admission number : 5
Enter name string : e
Enter salary number : 100000
Enter department number: 2
Enter phone number : 234254432
Repeat? : n
Enter command : 2
[1, 'a', 100, 1, 4565]
[2, 'b', 200, 2, 45654]
[3, 'c', 60000, 2, 4565467]
[4, 'd', 70000, 1, 5654645]
[5, 'e', 100000, 2, 234254432]
Enter command : 3
Enter file location : emp.dat
[1, 'a', 100, 1, 4565]
[2, 'b', 200, 2, 45654]
[3, 'c', 60000, 2, 4565467]
[4, 'd', 70000, 1, 5654645]
[5, 'e', 100000, 2, 234254432]
Enter command : 4
Enter number : 1
[1, 'a', 100, 1, 4565]
found!
Enter command : 5
Enter name : a
[1, 'a', 100, 1, 4565]
found!
Enter command : 6
Enter name : b
[2, 'b', 200, 2, 45654]
found  1 Employees with name  b
[2, 'b', 200, 2, 45654]
Enter command : 7
Enter number : 4565
[1, 'a', 100, 1, 4565]
found!
Enter command : 8
Enter department number : 1
2 employees in department number  1
Enter command : 9
[5, 'e', 100000, 2, 234254432] has highest salary of  100000
Enter command : 10
highest salary is  100000
Enter command : 11
Enter number : 4
Record found and deleted.
Enter command : 12
Enter number : 3
[[1, 'a', 100, 1, 4565], [2, 'b', 200, 2, 45654], [3, 'c', 60000, 2, 4565467], [5, 'e', 100000, 2, 234254432]]
Enter command : 2
[1, 'a', 100, 1, 4565]
[2, 'b', 200, 2, 45654]
[3, 'c', 66000.0, 2, 4565467]
[5, 'e', 100000, 2, 234254432]
Enter command : 13
Enter number : 5
Updated salary
Enter command : 2
[1, 'a', 100, 1, 4565]
[2, 'b', 200, 2, 45654]
[3, 'c', 66000.0, 2, 4565467]
[5, 'e', 110000.00000000001, 2, 234254432]
Enter command : 13
Enter number : 1
Updated salary
Enter command : 14

(B) Write a menu-driven program using functions to store data about
students having adno,name,mark1,mark2,mark3 using dictionary .
1. Create
2. Display entire file
3. Search for a particular student whose adno is given.
4. Search,display & count students scoring above 90 in all 3 subjects.
5. Delete a student whose mark is below 40 in all 3 subjects.
6. Update a student’s mark1 by adding 5 grace marks
'''

def create():
    f = open('st.dat', 'wb')
    d = {}
    while True:
        admo = int(input("Enter addission number : "))
        d['admo'] = admo
        name = input("Enter name : ")
        d['name'] = name
        mk1 = int(input("Enter marks 1 : "))
        d['marks1'] = mk1
        mk2 = int(input("Enter marks 2 : "))
        d['marks2'] = mk2
        mk3 = int(input("Enter marks 3 : "))
        d['marks3'] = mk3
        ask = input("Reapeat : ")
        pickle.dump(d,f)
        if ask in 'Nn':
            break
    f.close()

def display():
    f = open('st.dat', 'rb')
    try:
        while True:
            d = pickle.load(f)
            print('admo : ', d['admo'])
            print('name : ', d['name'])
            print('marks1 : ', d['marks1'])
            print('marks2 : ', d['marks2'])
            print('Marks3 : ', d['marks3'])
    except EOFError:
        f.close()

def search(num):
    flag = False
    f = open('st.dat', 'rb')
    try:
        while True:
            d = pickle.load(f)
            if d['admo'] == num:
                flag = True
                print(d)
                break
    except EOFError:
        f.close()
    if flag == True:
        print("found!")
    else:
        print("Not found!")

def above90():
    c = 0
    k = []
    f = open('st.dat', 'rb')
    try:
        while True:
            d = pickle.load(f)
            if d['marks1'] > 90 and d['marks2'] > 90 and d['marks3'] > 90:
                c += 1
                tempname = d['name']
                k.append(tempname)
    except EOFError:
        f.close()

    print(c, "student have scored more than 90 marks in all 3 subjects.")
    print("They are named: ")
    for x in k:
        print(x)

def less40():
    f = open('st.dat', 'rb')
    p = open('temp.dat', 'wb')
    try:
        while True:
            d = pickle.load(f)
            if d['marks1'] < 40 and d['marks2'] < 40 and d['marks3'] < 40:
                print(d['name'], "Student deleted.")
            else:
                pickle.dump(d, p)
    except EOFError:
        f.close()
        p.close()

        import os
        os.remove("st.dat")
        os.rename("temp.dat", "st.dat")

def gracemark(adno):
    flag = False
    f = open('st.dat', 'rb')
    p = open('temp.dat', 'wb')
    try:
        while True:
            d = pickle.load(f)
            if d['admo'] == adno:
                flag = True
                d['marks1'] += 5
                d['marks2'] += 5
                d['marks3'] += 5
                pickle.dump(d, p)
            else:
                pickle.dump(d, p)
    except EOFError:
        f.close()
        p.close()

        import os
        os.remove("st.dat")
        os.rename("temp.dat", "st.dat")

    if flag == True:
        print("Found!")
    else:
        print("Not found!")
        

while True:
    print('''
    Menu driven:
    1-Create  
    2-Display 
    3-Search
    4-Search above 90
    5-Delete below 40
    6-Grace 5 marks
    7-Exit
    ''')

    command = int(input("Enter command : "))
    if command == 1:
        create()
    elif command == 2:
        display()
    elif command == 3:
        no = int(input("Enter adno to search : "))
        search(no)
    elif command == 4:
        above90()
    elif command == 5:
        less40()
    elif command == 6:
        no = int(input("Enter adno to grace : "))
        gracemark(no)
    elif command == 7:
        break
    else:
        print("Wrong command given ! ")


'''
    Menu driven:
    1-Create  
    2-Display 
    3-Search
    4-Search above 90
    5-Delete below 40
    6-Grace 5 marks
    7-Exit
    
Enter command : 1
Enter addission number : 1
Enter name : agrim
Enter marks 1 : 88
Enter marks 2 : 45
Enter marks 3 : 100
Reapeat : y
Enter addission number : 2
Enter name : james
Enter marks 1 : 66
Enter marks 2 : 33
Enter marks 3 : 70
Reapeat : y
Enter addission number : 3
Enter name : ronald
Enter marks 1 : 12
Enter marks 2 : 23
Enter marks 3 : 12
Reapeat : y
Enter addission number : 4
Enter name : tina
Enter marks 1 : 98
Enter marks 2 : 99
Enter marks 3 : 97
Reapeat : n

    Menu driven:
    1-Create  
    2-Display 
    3-Search
    4-Search above 90
    5-Delete below 40
    6-Grace 5 marks
    7-Exit
    
Enter command : 2
admo :  1
name :  agrim
marks1 :  88
marks2 :  45
Marks3 :  100
admo :  2
name :  james
marks1 :  66
marks2 :  33
Marks3 :  70
admo :  3
name :  ronald
marks1 :  12
marks2 :  23
Marks3 :  12
admo :  4
name :  tina
marks1 :  98
marks2 :  99
Marks3 :  97

    Menu driven:
    1-Create  
    2-Display 
    3-Search
    4-Search above 90
    5-Delete below 40
    6-Grace 5 marks
    7-Exit
    
Enter command : 3
Enter adno to search : 3
{'admo': 3, 'name': 'ronald', 'marks1': 12, 'marks2': 23, 'marks3': 12}
found!

    Menu driven:
    1-Create  
    2-Display 
    3-Search
    4-Search above 90
    5-Delete below 40
    6-Grace 5 marks
    7-Exit
    
Enter command : 4
1 student have scored more than 90 marks in all 3 subjects.
They are named: 
tina

    Menu driven:
    1-Create  
    2-Display 
    3-Search
    4-Search above 90
    5-Delete below 40
    6-Grace 5 marks
    7-Exit
    
Enter command : 5
ronald Student deleted.

    Menu driven:
    1-Create  
    2-Display 
    3-Search
    4-Search above 90
    5-Delete below 40
    6-Grace 5 marks
    7-Exit
    
Enter command : 6
Enter adno to grace : 3
Not found!

    Menu driven:
    1-Create  
    2-Display 
    3-Search
    4-Search above 90
    5-Delete below 40
    6-Grace 5 marks
    7-Exit
    
Enter command : 6
Enter adno to grace : 2
Found!

    Menu driven:
    1-Create  
    2-Display 
    3-Search
    4-Search above 90
    5-Delete below 40
    6-Grace 5 marks
    7-Exit
    
Enter command : 2
admo :  1
name :  agrim
marks1 :  88
marks2 :  45
Marks3 :  100
admo :  2
name :  james
marks1 :  71
marks2 :  38
Marks3 :  75
admo :  4
name :  tina
marks1 :  98
marks2 :  99
Marks3 :  97

    Menu driven:
    1-Create  
    2-Display 
    3-Search
    4-Search above 90
    5-Delete below 40
    6-Grace 5 marks
    7-Exit
    
Enter command : 7

'''


'''
(B) Write a menu-driven program using functions to store data about
students having adno,name,mark1,mark2,mark3 using dictionary .
1. Create
2. Display entire file
3. Search for a particular student whose adno is given.
4. Search,display & count students scoring above 90 in all 3 subjects.
5. Delete a student whose mark is below 40 in all 3 subjects.
6. Update a student’s mark1 by adding 5 grace marks
'''


import pickle

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



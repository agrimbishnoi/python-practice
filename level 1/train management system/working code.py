import pickle
import os
import sys

dict={}

def write_in_file():
    print("Admin permission required.")
    passw=input("Enter password : ")
    auth=0
    if passw=='trainpassword123':
        auth=1
    if auth==1:
        file=open("rail.dat","ab")
        while True:
            dict["trainid"]=int(input("Enter train id : "))
            dict["trainname"]=int(input("Enter train name : "))
            dict["trainfair"]=int(input("Enter train fair : "))
            dict["trainvacancy"]=int(input("Enter seats available : "))
            dict["trainstart"]=input("Enter train departure location : ")
            dict["trainend"]=input("Enter train arrival location : ")

            pickle.dump(dict,file)
            ask=input("Repeat? :")
            if ask in 'Nn':
                break
        file.close()
    else:
        print("Permission Denied. Wrong Password Entered")

def display():
    file=open("rail.dat","rb")
    try:
        while True:
            r=pickle.load(file)
            print("***")
            print("Train Id : ",r['trainid'])
            print("Train Name : ",r['trainname'])
            print("Train Fair : ",r['trainfair'])
            print("Train Departure : ",r['trainstart'])
            print("Train Arrival : ",r['trainend'])
            print("Train Vacancy : ",r['trainvacancy'])
            print("***")
    except EOFError:
        pass
    file.close()

def search():
    file=open("rail.dat","rb")
    n=int(input("Enter train id to search : "))
    found=0
    try:
        while True:
            data=pickle.load(file)
            if data["trainid"]==n:
                print("Record found")
                print(data)
                found=1
                break
    except EOFError:
        pass
    if found==0:
        print("No Train with such a id found")
    file.close()

def update():
    print("Admin permission required.")
    passw=input("Enter password : ")
    auth=0
    if passw=='trainpassword123':
        auth=1
    if auth==1:
        f1=open("rail.dat","rb")
        f2=open("temp.dat","ab")
        r=int(input("Enter train id for updation : "))
        try:
            while True:
                data=pickle.load(f1)
                if data["trainid"]==r:
                    print("Enter new details")
                    data["trainid"]=int(input("Update train id : "))
                    data["trainname"]=int(input("Update train name : "))
                    data["trainfair"]=int(input("Update train fair : "))
                    data["trainstart"]=input("Update train departure location : ")
                    data["trainend"]=input("Update train arrival location : ")
                    data["trainvacancy"]=int(input("Update available seats in train : "))
                    pickle.dump(data,f2)
                else:
                    pickle.dump(data,f2)
        except EOFError:
            pass
        f1.close()
        f2.close()
        os.remove("rail.dat")
        os.rename("temp.dat","rail.dat")
        file=open("rail.dat","rb")
        try:
            while True:
                r=pickle.load(file)
                print(r)
        except EOFError:
            pass
    else:
        print("Permission Denied. Wrong Password Entered")





def delete():
    print("Admin permission required.")
    passw=input("Enter password : ")
    auth=0
    if passw=='trainpassword123':
        auth=1
    if auth==1:
        f1=open("rail.dat","rb")
        f2=open("temp.dat","ab")
        r=int(input("Enter train id for deletion : "))
        try:
            while True:
                data=pickle.load(f1)
                if data["trainid"]==r:
                    pass
                else:
                    pickle.dump(data,f2)
        except EOFError:
            pass
        f1.close()
        f2.close()
        os.remove("rail.dat")
        os.rename("temp.dat","rail.dat")
        file=open("rail.dat","rb")
        print("Deleted successfully!")
        try:
            while True:
                r=pickle.load(file)
                print(r)
        except EOFError:
            pass
    else:
        print("Permission Denied. Wrong Password Entered")

def book():
    file=open("rail.dat","rb")
    n=int(input("Enter train id to book seats : "))
    found=0
    try:
        while True:
            data=pickle.load(file)
            if data["trainid"]==n:
                print("Record found")
                print("Train has ",data["trainvacancy"],"seats available at the momment.")
                noseats=int(input("Enter number of seats to book : "))
                if noseats > data["trainvacancy"]:
                    print("Cannot book more tickets than available.")
                    break
                else:
                    print(noseats,"booked successfully.")
                    print("successfully booked",noseats,"seats")
                found=1
                break

    except EOFError:
        file.close()
    if found==0:
        print("No Train with such a id found")
    if found==1:
        f1=open("rail.dat","rb")
        f2=open("temp.dat","ab")
        r=n
        try:
            while True:
                data=pickle.load(f1)
                if data["trainid"]==r:
                    data["trainvacancy"] -= noseats
                    pickle.dump(data,f2)
                else:
                    pickle.dump(data,f2)
        except EOFError:
            pass
        f1.close()
        f2.close()
        file.close()
        os.remove("rail.dat")
        os.rename("temp.dat","rail.dat")





def cancellation():
    file=open("rail.dat","rb")
    n=int(input("Enter train id to cancel your seats : "))
    found=0
    try:
        while True:
            data=pickle.load(file)
            if data["trainid"]==n:
                print("Record found")
                noseats=int(input("Enter number of seats to be canceled : "))
                print(noseats,"seats selected to cancel.")
                conform=input("Are you sure you want to cancel tickets? :")
                if conform in 'yY':
                    print(noseats,"seats successfully cancelled.")
                    found=1
                else:
                    print("Canncellation aborted!")
                
                break

    except EOFError:
        file.close()
    if found==0:
        print("No Train with such a id found")
    if found==1:
        f1=open("rail.dat","rb")
        f2=open("temp.dat","ab")
        r=n
        try:
            while True:
                data=pickle.load(f1)
                if data["trainid"]==r:
                    data["trainvacancy"] += noseats
                    pickle.dump(data,f2)
                else:
                    pickle.dump(data,f2)
        except EOFError:
            pass
        f1.close()
        f2.close()
        file.close()
        os.remove("rail.dat")
        os.rename("temp.dat","rail.dat")



def updateadmin():
    oldpass=input("Enter old password : ")
    if oldpass=='trainpassword123':
        newpass=input("Enter new password : ")
        newpassagain=input("Retype the new password : ")
        if newpass==newpassagain:
            print("Password updated successfully")
        else:
            print("Passwords didnt match.")
    else:
        print("Wrong password given.")

while True:
    print()
    print("MENU \n 1-Write in file(Admin) \n 2-Display \n 3-Search \n 4-Book tickets \n 5-Cancel Tickets\n 6-Update(Admin) \n 7-Delete(Admin) \n 8-Update Admin Password\n 0-Exit \r")
    print()
    ch=int(input("Enter command from menu : "))
    if ch==1:
        print("Selected to write in file.")
        write_in_file()
    elif ch==2:
        print("Selected to Display data.")
        display()
    elif ch==3:
        print("Selected for searching in file.")
        search()
    elif ch==4:
        print("Selected for booking tickets.")
        book()
    elif ch==5:
        print("Selected for canceling tickets.")
        cancellation()
    elif ch==6:
        print("Selected to update file.")
        update()
    elif ch==7:
        print("Selected to delete record.")
        delete()
    elif ch==8:
        print("Selected to update admin password.")
        updateadmin()
    elif ch==0:
        print("Selected to Exit.")
        break
    else:
        print("Wrong command given!")

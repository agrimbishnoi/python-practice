'''
LIST ASSIGNMENT
BY AGRIM RAI
Roll no. 2
class 11D


Q1) WAP to search for an element in a given
list of numbers using Linear Search.

Q2) WAP to count frequency of a given element
in list of numbers.

Q3) WAP to input a list of integers. Find the
total and average of same.

Q4) Find minimum and maximum from list of
integers.

Q5)Input the list of numbers. Count negative,
positive and zero elements.

Q6)Count even, odd and 0 elements from the
list.

Q7)Find the biggest and second biggest
element from the list.

Q8)Reverse the elements of a list and print.

Q9)BUBBLE SORT
Q10)INSERTION SORT

Q 11) Search for an element using BINARY
Search.
Q12) WAP to create a list according to the user,
swap the alternate elements with each other.

Q13) Use the list of students names. Ask the
user about each name whether it is to be kept
or not, delete names user does not want.

Q14) WAP to take a list of elements from user
and calculate number of prime elements in it.

Q15) WAP to input a list from user and swap
the first half of the list with the second half.




'''




'''


Q1) WAP to search for an element in a given
list of numbers using Linear Search.


'''
print(" WAP to search for an element in a given list of numbers using Linear Search.")

l=eval(input("Enter list : "))
num=int(input("Enter element to be searched : "))
for i in range(len(l)):
    if num==l[i]:
        print("Element found")
        break
else:
    print("Elemnt not found")





'''

Q2) WAP to count frequency of a given element
in list of numbers.

'''

print("WAP to count frequency of a given element in list of numbers.")
l=eval(input("Enter list : "))
num=int(input("Enter element to be searched for frequency : "))
c=0
for x in l:
    if x==num:
        c+=1
print("Frequency of elemnt is ",c)




'''

Q3) WAP to input a list of integers. Find the
total and average of same.

'''

print("WAP to input a list of integers. Find the total and average of same.")
l=eval(input("Enter list : "))
t=0
for x in l:
    t+=x
    avg=t/len(l)

print("sum=",t)
print("average=",avg)


'''

Q4) Find minimum and maximum from list of
integers.

'''
print("Find minimum and maximum from list of integers")
l=eval(input("Enter list : "))
maximum=max(l)
minimum=min(l)
print("Maximum value in list is ",maximum)
print("Minimum value in list is ",minimum)




'''

Q5)Input the list of numbers. Count negative,
positive and zero elements.


'''

print("Input the list of numbers. Count negative,positive and zero elements")
l=eval(input("Enter a list : "))
n=0
p=0
z=0
for number in l:
    if number==0:
        z+=1
    elif number>0:
        p+=1
    else:
        n+=1
print("There are",z," zeros in list.")
print("There are",p," positives in list.")
print("There are",n," negatives in list.")






'''

Q6)Count even, odd and 0 elements from the
list.


'''
print("Count even, odd and 0 elements from the list")

l=eval(input("Enter a list : "))
e=0
o=0
z=0
for number in l:
    if number==0:
        z+=1
    elif number%2==0:
        e+=1
    else:
        o+=1
print("There are",z," zeros in list.")
print("There are",e," evens in list.")
print("There are",o," odds in list.")



'''

Q7)Find the biggest and second biggest
element from the list.


'''


l=eval(input("Enter out a list : "))
big = l[0]
for num in l:
       if num>big:
           big=num
templist=l
l.remove(big)

sbig = templist[0]
for num in templist:
       if num>sbig:
           sbig=num
print("biggest",big)
print("second big",sbig)


'''

Q8)Reverse the elements of a list and print.

'''



list=eval(input("Enter out a list : "))
list = list[::-1]
print(list)




'''

Q9)BUBBLE SORT

'''
print("BUBBLE SORT")

l=eval(input("Enter a list : "))
n=len(l)
for i in range(n-1):
    for j in range(n-1-i):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)




'''

selction dort

'''

l=eval(input("Enter a list : "))
n=len(l)

for i in range(n-1):
    for j in range(1+i,n):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]

print(l)

'''

Q10)INSERTION SORT

'''
print('Q10)INSERTION SORT')
l=[2,13,12,4]
for i in range(1,len(l)):
    temp=l[i]
    j=i-1
    while j>0 and l[j]>temp:
        l[j+1]=l[j]
        j=j-1
    l[j+1]=temp
print(l)

'''

Q 11) Search for an element using BINARY
Search.

'''

print('Search for an element using BINARY Search')
l=[2,13,12,4]
n=len(l)
num=int(input("Enter number to be searched:"))

beg=0
end=n-1
mid=(beg-end)//2
while l[mid]!=num:
    if num > l[mid]:
        end=mid-1
    else:
        beg=mid+1
    mid=(beg-end)//2


if l[mid]==num:
    print("Found at",mid+1)
else:
    print("Not found")


'''

Q12) WAP to create a list according to the user,
swap the alternate elements with each other.

'''
l=[]
while True:
    ask=input("What to add element? y/n" )
    if ask in 'Nn':
        break
    elif ask in 'Yy':
        newele=int(input("Enter a number : "))
        l.append(newele)
    else:
        print("You typed out a wrong word!")
print(l)



print("List before swap:", l)

n=len(l)



i = 0
while i < n :
    t = l[i]
    l[i] = l[i + 1]
    l[i + 1] = t
    i = i + 2

print("List after swap:", l)










'''

Q13) Use the list of students names. Ask the
user about each name whether it is to be kept
or not, delete names user does not want.

'''
l=['agrim','raj','salman','ram','lakhan','Gandhi','Rahul']
print("answer in 'y' for yes and in 'n' for no.")
newlist=[]
for n in l:
    print(n)
    ask=input("Do you want to keep?")
    if ask in 'yY':
        newlist.append(n)
    elif ask in 'Nn':
        print("Deleted!")
    else:
        print("Wrong input")
print(newlist)



'''

Q14) WAP to take a list of elements from user
and calculate number of prime elements in it.

'''
l=eval(input("Enter a list : "))
noprime=0

for n in l:
    flag=0
    for x in range(2,n):
        if n%x==0:
            flag =1
            break
        
    if flag==1:
        noprime+=0
    if flag==0:
        noprime+=1

print('There are ',noprime,'prime numbers in list.')
'''

Q15) WAP to input a list from user and swap
the first half of the list with the second half.

'''
l=eval(input("Enter a list : "))
n=len(l)

if n%2 !=0:
    mid=n//2
    
    for x in range(1,n+1):
        lleft=l[0:mid]
        lright=l[mid+1:]
    print(lleft)
    print(l[mid])
    print(lright)
    
    newlist=lright[::-1]
    newlist.append(l[mid])
    for new in lleft[::-1]:
        newlist.append(new)
    print("swapped list is generated.")
    print(newlist)
    
else:
    print("cant run on even numbers!")





'''

output gernerated


========= RESTART: C:\Users\agrimbishnoi\Desktop\list asssignment.py =========
 WAP to search for an element in a given list of numbers using Linear Search.
Enter list : [2,13,12,4,55]
Enter element to be searched : 3
Elemnt not found
WAP to count frequency of a given element in list of numbers.
Enter list : [2,13,12,4,55]
Enter element to be searched for frequency : 12
Frequency of elemnt is  1
WAP to input a list of integers. Find the total and average of same.
Enter list : [2,13,12,4,55]
sum= 86
average= 17.2
Find minimum and maximum from list of integers
Enter list : [2,13,12,4,55]
Maximum value in list is  55
Minimum value in list is  2
Input the list of numbers. Count negative,positive and zero elements
Enter a list : [2,13,12,4,55]
There are 0  zeros in list.
There are 5  positives in list.
There are 0  negatives in list.
Count even, odd and 0 elements from the list
Enter a list : [2,13,12,4,55]
There are 0  zeros in list.
There are 3  evens in list.
There are 2  odds in list.
Enter out a list : [2,13,12,4,55]
biggest 55
second big 13
Enter out a list : [2,13,12,4,55]
[55, 4, 12, 13, 2]
BUBBLE SORT
Enter a list : [2,13,12,4,55]
[2, 4, 12, 13, 55]
Enter a list : [2,13,12,4,55]
[2, 4, 12, 13, 55]
Q10)INSERTION SORT
[2, 4, 12, 13]
Search for an element using BINARY Search
Enter number to be searched:12
Found at -1
What to add element? y/ny
Enter a number : 34
What to add element? y/ny
Enter a number : 55
What to add element? y/ny
Enter a number : 67
What to add element? y/ny
Enter a number : 22
What to add element? y/nn
[34, 55, 67, 22]
List before swap: [34, 55, 67, 22]
List after swap: [55, 34, 22, 67]
answer in 'y' for yes and in 'n' for no.
agrim
Do you want to keep?y
raj
Do you want to keep?n
Deleted!
salman
Do you want to keep?y
ram
Do you want to keep?n
Deleted!
lakhan
Do you want to keep?y
Gandhi
Do you want to keep?n
Deleted!
Rahul
Do you want to keep?y
['agrim', 'salman', 'lakhan', 'Rahul']
Enter a list : [2,13,12,4,55]
There are  2 prime numbers in list.
Enter a list : [2,13,12,4,55]
[2, 13]
12
[4, 55]
swapped list is generated.
[55, 4, 12, 13, 2]
>>> 


'''



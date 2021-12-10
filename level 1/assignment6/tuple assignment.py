#Tuple Assignment 
#Date: 12/10/2021
#Agrim Rai
#Class:11D , rollno : 2

'''

QUESTION:


Q1 WAP to input n numbers, store it in a tuple and
display the elements of the tuple.

Q2 Input n numbers store it in a tuple. Find the
minimum and maximum values in the tuple.

Q3 Input the elements in two tuples. Interchange the
tuple values.

Q4 Input five subject names and store it in a tuple.
Display the tuple on the screen.

Q5 Find the sum and average of n numbers stored in a
tuple.

Q6 Input n numbers, store it in a tuple. Separate the
tuple in the following manner:-
T = (10,20,30,40,50,60)
T1 = (10,30,50)
T2 = (20,40,60)

Q7 Input the elements in the tuple. Print each tuple
element with the forward and backward index.

Q8 Find the second largest number in the tuple.

Q9 WAP to Input numbers and find
1) MEAN (t/n)
2) MEDIAN (n/2+1 +n/2 )/2
3) MODE
4) STANDARD DEVIATION
5) VARIANCE


EXTRA QUESTIONS: 

check if tuple sorted by default.
include in assignment


'''





'''

Q1 WAP to input n numbers, store it in a tuple and
display the elements of the tuple.

'''

print('''

Q1 WAP to input n numbers, store it in a tuple and display the elements of the tuple.

	''')
t=()
n=int(input("Enter number of elemnets to be added in tuple : "))
for i in range(1,n+1):
	a=int(input("Enter elemnet : "))
	t=t+(a,)

print(t)

'''

Q2 Input n numbers store it in a tuple. Find the
minimum and maximum values in the tuple.

'''
print('''

Q2 Input n numbers store it in a tuple. 
Find the minimum and maximum values in the tuple.

	''')
t=()
n=int(input("Enter number of elemnets to be added in tuple : "))
for i in range(1,n+1):
	a=int(input("Enter elemnet : "))
	t=t+(a,)
print(t)
mini=min(t)
maxi=max(t)

print('using direct functions..')
print('Minimum most elemnet : ',mini)
print('Maximum most elemnet : ',maxi)

print('using for loop..')
mini=t[0]
maxi=t[0]
for i in range(n):
	if t[i] > maxi:
		maxi=t[i]
	if t[i] < mini:
		mini=t[i]

print('Minimum most elemnet : ',mini)
print('Maximum most elemnet : ',maxi)


'''

Q3 Input the elements in two tuples. Interchange the
tuple values.

'''


print('''

Q3 Input the elements in two tuples. Interchange the tuple values.

	''')
t1=eval(input("Enter a tuple1 : "))
t2=eval(input("Enter a tuple2 : "))

print(t1,t2)
t1,t2=t2,t1
print("After swapping..")
print("tuple1 : ",t1)
print("tuple2 : ",t2)



'''
Q4 Input five subject names and store it in a tuple.
Display the tuple on the screen.

'''
print('''

Q4 Input five subject names and store it in a tuple.Display the tuple on the screen.

	''')
t=()
for i in range(0,5):
	n=input("Enter subject name to be entered : ")
	t=t+(n,)
print(t)



'''

Q5 Find the sum and average of n numbers stored in a
tuple.		

'''
print('''

Q5 Find the sum and average of n numbers stored in a tuple.
	
	''')
t=eval(input("Enter a tuple : "))
length=len(t)
s=0
for x in range(length):
	s+=t[x]
avg=s/length

print('sum = ',s)
print('average = ',avg)


'''

Q6 Input n numbers, store it in a tuple. Separate the
tuple in the following manner:-
T = (10,20,30,40,50,60)
T1 = (10,30,50)
T2 = (20,40,60)

'''
print('''

Q6 Input n numbers, store it in a tuple. Separate the
tuple in the following manner:-
T = (10,20,30,40,50,60)
T1 = (10,30,50)
T2 = (20,40,60)

	''')
t=eval(input("Enter a tuple : "))
print('using slicing..')
t1=t[0::2]
t2=t[1::2]
print(t1,t2)

t1=()
t2=()

for i in range(0,len(t),2):
	t1=t1+(t[i],)
	t2=t2+(t[i+1],)
print('using for loop...')
print(t1,t2)

'''

Q7 Input the elements in the tuple. Print each tuple
element with the forward and backward index.

'''
print('''

Q7 Input the elements in the tuple. Print each tuple
element with the forward and backward index.


	''')
t=eval(input("Enter a tuple : "))

print('using slicing...')
print(t[0],' ',t[-5])
print(t[1],' ',t[-4])
print(t[2],' ',t[-3])
print(t[3],' ',t[-2])

print("using for loop...")
for i in range(0,len(t)):
	print(t[i],' ',t[-len(t)+i])


'''

Q8) Find the second largest number in the tuple.

'''


print('''

Q8) Find the second largest number in the tuple.

	''')

t=eval(input("Enter tuple : "))
bmax=-999
smax=-999
for x in t:
    if x>bmax:
        smax=bmax
        bmax=x 
    elif x>smax:
        smax=x 
print('biggest number : ',bmax)
print('second biggest number : ',smax)



'''

Q9 WAP to Input numbers and find
1) MEAN (t/n)
2) MEDIAN (n/2+1 +n/2 )/2
3) MODE
4) STANDARD DEVIATION
5) VARIANCE

'''
print('''

Q9 WAP to Input numbers and find
1) MEAN (t/n)
2) MEDIAN (n/2+1 +n/2 )/2
3) MODE
4) STANDARD DEVIATION
5) VARIANCE

	''')

t=eval(input("Enter a tuple : "))
l1=list(t)
import statistics

mea=statistics.mean(l1)
medi=statistics.median(l1)
vari=statistics.variance(l1)
stde=statistics.stdev(l1)
print('using statistics module...')
print('mean of tupple ',mea)
print('median of tupple ',medi)
print('variance of tupple ',vari)
print('standard variance of tupple ',stde)




'''

Extra Questions..


'''


#check if tuple sorted by default.
#include in assignment
print('''

check if tuple sorted by default.


	''')
t=eval(input("Enter a tuple: "))
if list(t) == sorted(t):
    print('tuple alredy in assending order')
else:
    print('tuple not sorted by default')



'''
OUTPUT


Q1 WAP to input n numbers, store it in a tuple and display the elements of the tuple.


Enter number of elemnets to be added in tuple : 5
Enter elemnet : 43
Enter elemnet : 23
Enter elemnet : 56
Enter elemnet : 34
Enter elemnet : 11
(43, 23, 56, 34, 11)


Q2 Input n numbers store it in a tuple.
Find the minimum and maximum values in the tuple.


Enter number of elemnets to be added in tuple : 4
Enter elemnet : 32
Enter elemnet : 453
Enter elemnet : 13
Enter elemnet : 566
(32, 453, 13, 566)
using direct functions..
Minimum most elemnet :  13
Maximum most elemnet :  566
using for loop..
Minimum most elemnet :  13
Maximum most elemnet :  566


Q3 Input the elements in two tuples. Interchange the tuple values.


Enter a tuple1 : (1,23,4,66)
Enter a tuple2 : (24,25,2,34,3)
(1, 23, 4, 66) (24, 25, 2, 34, 3)
After swapping..
tuple1 :  (24, 25, 2, 34, 3)
tuple2 :  (1, 23, 4, 66)


Q4 Input five subject names and store it in a tuple.Display the tuple on the screen.


Enter subject name to be entered : physics
Enter subject name to be entered : computer
Enter subject name to be entered : pe
Enter subject name to be entered : art
Enter subject name to be entered : maths
('physics', 'computer', 'pe', 'art', 'maths')


Q5 Find the sum and average of n numbers stored in a tuple.


Enter a tuple : (1,123,14,23523,145)
sum =  23806
average =  4761.2


Q6 Input n numbers, store it in a tuple. Separate the
tuple in the following manner:-
T = (10,20,30,40,50,60)
T1 = (10,30,50)
T2 = (20,40,60)


Enter a tuple : (10,20,40,6,7,8)
using slicing..
(10, 40, 7) (20, 6, 8)
using for loop...
(10, 40, 7) (20, 6, 8)


Q7 Input the elements in the tuple. Print each tuple
element with the forward and backward index.



Enter a tuple : (10,20,30,40,50)
using slicing...
10   10
20   20
30   30
40   40
using for loop...
10   10
20   20
30   30
40   40
50   50


Q8) Find the second largest number in the tuple.


Enter tuple : (10,20,30,40)
40 30


Q9 WAP to Input numbers and find
1) MEAN (t/n)
2) MEDIAN (n/2+1 +n/2 )/2
3) MODE
4) STANDARD DEVIATION
5) VARIANCE


Enter a tuple : (345,234,15,135,1)
using statistics module...
mean of tupple  146
median of tupple  135
variance of tupple  21413
standard variance of tupple  146.3318147225681


check if tuple sorted by default.



Enter a tuple: (10,20,30,40,50)
tuple alredy in assending order



'''
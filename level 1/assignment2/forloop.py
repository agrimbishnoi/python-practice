#This is file of python 'for loop' by Agrim Rai-11d
#date:1/9/2021

'''
questions:


                       ASSIGNMENT -2 (FOR LOOP )
Q1. WAP to print natural numbers till ‘n’. Also , find the sum.
Q2.  WAP to print the table of a given number.
Q3. WAP to input any number and print its factorial.
Q4. WAP  to print odd numbers till a given number ’ n’ and find their sum.
Q5. WAP to print Fibonacci series till given number ‘n’.
 Q6. WAP to print first ‘n’ natural numbers in reverse order.
*SERIES
Q7. WAP to print the series till ‘n’ terms 
a)1     4     7    10    13   16……….
b)1   4      9    16      25   36………
Q8. WAP to  print the reversed number.
Q9. WAP to print  whether  the  number entered by the user is prime or not.
Q10. WAP to print the sum of the series till ‘n’ terms 

a)	s = x + x^2 + x^3 ……………
b)	s = x + x^3 + x^5………….
c)	S =1 + x/1! + x^2/2!.......
d)	 S = 1 + x/2 + x^2/3………
e)	 S = x – x^2/2! + x^3/3! – x^4/4!..........
*PATTERNS
Q11. WAP to print the following pattern:-
a)	1
12
123
1234
12345
b)	 12345
1234
     123
12
1
c)55555
55555
55555
d)*
    **
        ***
       ****
      *****
e)	1
    22
   333
   4444
    55555
Q12. WAP to print hcf and lcm of any two numbers.
Q13. WAP to print any number ‘a’ raise to the power ‘b’. 




'''


#Answers





print('''

 Q1. WAP to print natural numbers till ‘n’. Also , find the sum. 

''')
n = int(input("Enter a value : "))
sum=0
for x in range(1,n+1):
    print(x)
    sum=sum+x
print("Sum calculated is ",sum)


print('''

Q2.  WAP to print the table of a given number.

''') 

tablenumber = int(input("Enter number : "))
for x in range(1,11):
    print(x*tablenumber)

print('''

 Q3. WAP to input any number and print its factorial.

''')

factorial = 1
factorialnumber = int(input("Enter a value : "))
for x in range(1,factorialnumber+1):
    factorial=factorial*x 
print("Factorial of numbers is : ",factorial)

print('''

 Q4. WAP  to print odd numbers till a given number ’ n’ and find their sum.

''')
sum = 0
sumofnumber = int(input("Enter a value : "))
for x in range(1,sumofnumber+1,2):
    sum=sum+x
    print(x)
  
print("Sum of odd numbers is : ",sum)


print('''

 Q5. WAP to print Fibonacci series till given number ‘n’.

''')


a=1
b=2
print(a,b)
fibon = int(input("Enter a number : "))
for i in (1,fibon-1):
    c=a+b 
    print(c,end='')
    a=b 
    b=c 

print('''

 Q6. WAP to print first ‘n’ natural numbers in reverse order.

''')

p=1
number = int(input("Enter number : "))
for x in range(number,0,-1):
    p=p*x
    print(x)
print("product is ",p)

print('''

# Q7. WAP to print the series till ‘n’ terms 
# a)1     4     7    10    13   16……….

''')


numbergiven = int(input("Enter number : "))
for x in range(1,numbergiven+1,3):
    print(x)

print('''

# b)1   4      9    16      25   36………

''')

numberformuser = int(input("Enter a number : "))
for x in range(1,numberformuser+1):
    print(x**2)


print('''

8. WAP to  print the reversed number.

''')


n = int(input("Enter a number : "))
for x in range(x,0,-1):
    print(x)


print('''

 Q9. WAP to print  whether  the  number entered by the user is prime or not.

''')


import math

n = int(input("Enter a number to check if it is prime or not : "))
prime_flag = 0
 
if(n > 1):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            prime_flag = 1
            break
    if (prime_flag == 0):
        print("true")
    else:
        print("false")
else:
    print("false")




print('''
# PATTERNS
# Q11. WAP to print the following pattern:-

# a)
# 1
# 12
# 123
# 1234
# 12345

''')

for n in range(1,6):
    for x in range(1,n+1):
        print(x,end=' ')  
    print()

print()

print('''

# b)

# 12345
# 1234
# 123
# 12
# 1

''')

for n in range(5,0,-1):
    for x in range(1,n+1):
        print(x,end=' ')  
    print()

print()
print('''

# c)
# 55555
# 55555
# 55555

''')

for n in range(1,6):
    for x in range(1,5):
        print("5",end=' ')
    print()

print()


print('''
# d)

#  *
#  **
#  ***
#  ****
#  *****

''')
for n in range(1,6):
    for x in range(1,n+1):
        print("*",end=' ')  
    print()
    
print()

print('''
# e)

#  1
#  22
#  333
#  4444
#  55555

''')

for x in range(1,6):
    for n in range(1,x+1):
        print(x,end=' ')
    print()

print('''

 Q12. WAP to print hcf.

''')


x=int(input('Enter a number : '))
y=int(input("Enter another number : "))

if x > y:
    smaller = y
else:
    smaller = x
for i in range(1, smaller+1):
    if((x % i == 0) and (y % i == 0)):
        hcf = i

print('hcf calculated is ',hcf)






print('''

 Q13. WAP to print any number ‘a’ raise to the power ‘b’. 

''')
number = int(input("Enter a number : "))
power = int(input("Enter the number's power : "))
square = number**power
print("Number after power is ",square)



'''
Output:




PS C:\Users\agrimbishnoi\Desktop\STUFF\weekly 2 computer> python .\forloop.py


 Q1. WAP to print natural numbers till ‘n’. Also , find the sum.


Enter a value : 11
1
2
3
4
5
6
7
8
9
10
11
Sum calculated is  66


Q2.  WAP to print the table of a given number.


Enter number : 11
11
22
33
44
55
66
77
88
99
110


 Q3. WAP to input any number and print its factorial.


Enter a value : 11
Factorial of numbers is :  39916800


 Q4. WAP  to print odd numbers till a given number ’ n’ and find their sum.


Enter a value : 11
1
3
5
7
9
11
Sum of odd numbers is :  36


 Q5. WAP to print Fibonacci series till given number ‘n’.


1 2
Enter a number : 33
35

 Q6. WAP to print first ‘n’ natural numbers in reverse order.


Enter number : 22
22
21
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
product is  1124000727777607680000


# Q7. WAP to print the series till ‘n’ terms
# a)1     4     7    10    13   16……….


Enter number : 23
1
4
7
10
13
16
19
22


# b)1   4      9    16      25   36………


Enter a number : 23
1
4
9
16
25
36
49
64
81
100
121
144
169
196
225
256
289
324
361
400
441
484
529


8. WAP to  print the reversed number.


Enter a number : 33
23
22
21
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1


 Q9. WAP to print  whether  the  number entered by the user is prime or not.


Enter a number to check if it is prime or not : 7
true

# PATTERNS
# Q11. WAP to print the following pattern:-

# a)
# 1
# 12
# 123
# 1234
# 12345


1
1 2
1 2 3
1 2 3 4
1 2 3 4 5



# b)

# 12345
# 1234
# 123
# 12
# 1


1 2 3 4 5
1 2 3 4
1 2 3
1 2
1



# c)
# 55555
# 55555
# 55555


5 5 5 5
5 5 5 5
5 5 5 5
5 5 5 5
5 5 5 5


# d)

#  *
#  **
#  ***
#  ****
#  *****


*
* *
* * *
* * * *
* * * * *


# e)

#  1
#  22
#  333
#  4444
#  55555


1
2 2
3 3 3
4 4 4 4
5 5 5 5 5


 Q12. WAP to print hcf.


Enter a number : 33
Enter another number : 11
hcf calculated is  11


 Q13. WAP to print any number ‘a’ raise to the power ‘b’.


Enter a number : 3
Enter the number's power : 3
Number after power is  27





'''




#while loops
#Assignment3 on while loop
#Agrim Rai - 11d
#2/9/2021


'''

ASSIGNMENT 3
WHILE LOOP
Q1)Print  SFS  5 times.
Q2)Calculate the factorial of a given number.
Q3)WAP to calculate and print the sums of even and odd integers of the first n natural numbers.
Q3.5) WAP to input integers till user wants.Print  the sum of even nos. and sum of odd nos.nt
Q4)Input any two numbers. Calculate ‘a’ to the power’ b ‘without using a**b.
Q5)Input any integer, print its individual digits.
Q6)Print the sum of digits of a given integer.
Q7)Check if the given number is an armstrong number.ex-153,407
Q8)Check if the given number is a palindrome number.
Q9)Check if the given number is  a perfect number.ex-6,28
Q10) Input some numbers till the user wants. Total them and print the total.
Q11) WAP to input any no to check if it is a prime no.
Q12) WAP asking the user to guess a no from a given range. Do not allow more than 3 chances.
Q13)Write a menu- driven program to-
1)Calculate sum
2)Calculate product
3)Calculate difference
4)Calculate division
5)Exit
Q14)Print prime numbers in range(2,100).
Q15)Write a menu driven program to-
1)Check if the  given number is  Armstrong number.
2)Check if the given number is  Palindrome number.
3)Check if the given number is a  Perfect number.
(eg:- 28=1+2+4+7+14)sum of proper divisors.
4)Check if the given number is a  Special number.ex-145=1!+4!+5!
 5) Check if the given number is a Prime number



'''



print('''

Q1)Print  SFS  5 times.

''')

i = 1
while i <= 5:
    print("sfs")
    i += 1

print('''

Q2)Calculate the factorial of a given number.

''')

num = int(input("Enter a number : "))
factorial = 1

while (num > 0):
    factorial = factorial * num
    num = num - 1
print(factorial)

print('''

WAP to input integers till user wants.Print  the sum of even nos. and sum of odd nos.

''')

number = int(input("Enter a number : "))

even_Sum = 0
odd_Sum = 0

for num in range(1, number + 1):
    if (num % 2 == 0):
        even_Sum = even_Sum + num
    else:
        odd_Sum = odd_Sum + num

print("Odd numbers : ", odd_Sum)
print("Even numbers : ", even_Sum)

print('''

Q5)Input any integer, print its individual digits

''')

number = int(input("enter number : "))
while number != 0:
    d = number % 10
    print(d)
    number = number // 10

#reverse throwing number

print('''
Q10) Input some numbers till the user wants. Total them and print the total.
''')

oddsum = 0
evensum = 0

while True:

    ask = input("Enter a number to add or a string to break : ")
    if ask.isdigit() == True:
        if int(ask) % 2 == 0:
            evensum = evensum + int(ask)
        else:
            oddsum = oddsum + int(ask)
    else:
        break

print("even sum", evensum)
print("odd sum", oddsum)

print('''
Input any two numbers. Calculate ‘a’ to the power’ b ‘without using a**b.
''')

number = int(input("Enter a number : "))
power = int(input("Enter its power : "))

import math
print(math.pow(number,power))






print('''

Q8)Check if the given number is a palindrome number.

''')

number = int(input("Enter any number :"))

temp = number
reverse_num = 0
while (number > 0):
    digit = number % 10
    reverse_num = reverse_num * 10 + digit
    number = number // 10
if (temp == reverse_num):
    print("The number is palindrome")
else:
    print("Not a palindrome")

print('''

Q9)Check if the given number is  a perfect number.ex-6,28

''')

n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if (n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print(" Perfect number")
else:
    print("Non Perfect number")


print('''

Input some numbers till the user wants. Total them and print the total.

''')

#while True:
#    ask = input("Enter a number : ")
#    if ask.isdigit():
#        print(ask)
#        sum = sum + int(ask)
#print("sum calculated is ", sum)


print('''

Q6)Print the sum of digits of a given integer.

''')

sum = 0
number = int(input("enter number : "))
while number != 0:
    d = number % 10
    sum = sum + d
    number = number // 10
print(sum)


print('''

Q7)Check if the given number is an armstrong number.ex-153,407

''')

num = int(input("Enter a  3 digit number : "))
order = 3
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit**order
    temp //= 10

if num == sum:
    print(num, "- Armstrong number")
else:
    print(num, "-Not an Armstrong number")

print('''

Q8)Check if the given number is a palindrome number.

''')

n = int(input("Enter a number : "))

temp = n
rev = 0
while (n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
if (temp == rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

print('''

Q12) WAP asking the user to guess a no from a given range. Do not allow more than 3 chances.

''')

secret = 7
chance = 0
guess = int(input("Enter a number : "))
while chance <= 3:
    if guess == secret:
        print("Correct")
        break
    else:
        chance = chance + 1

print('''



Q13)Write a menu- driven program to-
1)Calculate sum
2)Calculate product
3)Calculate difference
4)Calculate division
5)Exit



''')

print('''


1)Calculate sum
'sum'

2)Calculate product
'product'

3)Calculate difference
'difference'

4)Calculate division
'division'

5)Exit
'exit'


''')

while True:

    num1 = int(input("Enter 1st number : "))
    num2 = int(input("Enter 2nd number : "))
    command = input("Enter a command from syntax : ")

    if command == 'sum':
        print(num1 + num2)

    elif command == 'product':
        print(num1 * num2)

    elif command == 'difference':
        print(num1 - num2)

    elif command == 'division':
        print(num1 / num2)

    elif command == 'exit':
        break
    else:
        break

print('''

        Q14)Print prime numbers in range(2,100).

''')

for x in range(2, 100):
    print(x)

print('''

15)Write a menu driven program to-

1)Check if the  given number is  Armstrong number.
'armstrong'

2)Check if the given number is  Palindrome number.
'palindrome'

3)Check if the given number is a  Perfect number.
(eg:- 28=1+2+4+7+14)sum of proper divisors.
'perfect'






''')

while True:

    num1 = int(input("Enter the number : "))
    command = input("Enter a command from synrax : ")

    if command == 'armstrong':
        
        order = num1.len()
        sum = 0 
        temp = num1
        while temp > 0:
            digit = temp % 10
            sum += digit**order
            temp //= 10
        if num1 == sum:
            print(num1, "- Armstrong number")
        else:
            print(num1, "-Not an Armstrong number")



    elif command == 'palindrome':


        temp = num1
        reverse_num = 0
        while (num1 > 0):
            digit = num1 % 10
            reverse_num = reverse_num * 10 + digit
            num1 = num1 // 10
        if (temp == reverse_num):
            print("The number is palindrome!")
        else:
            print("Not a palindrome!")
        

    elif command == 'perfect':
        
        sum1 = 0
        for i in range(1, n):
            if (num1 % i == 0):
                sum1 = sum1 + i

            if (sum1 == num1):
                print(" Perfect number")
            else:
                print("Non Perfect number")

    elif command == 'exit':
        break
    else:
        break











'''

output:






PS C:\Users\agrimbishnoi\Desktop\STUFF\weekly 2 computer\assignment3> python .\whileloop.py


Q1)Print  SFS  5 times.


sfs
sfs
sfs
sfs
sfs


Q2)Calculate the factorial of a given number.


Enter a number : 22
1124000727777607680000


WAP to input integers till user wants.Print  the sum of even nos. and sum of odd nos.


Enter a number : 22
Odd numbers :  121
Even numbers :  132


Q5)Input any integer, print its individual digits


enter number : 22
2
2

Q10) Input some numbers till the user wants. Total them and print the total.

Enter a number to add or a string to break : 22
Enter a number to add or a string to break : 22
Enter a number to add or a string to break : 22
Enter a number to add or a string to break : d
even sum 66
odd sum

Input any two numbers. Calculate ‘a’ to the power’ b ‘without using a**b.

Enter a number : 22
Enter its power : 22
3.4142787736421956e+29


Q8)Check if the given number is a palindrome number.


Enter any number :22
The number is palindrome


Q9)Check if the given number is  a perfect number.ex-6,28


Enter any number: 22
Non Perfect number


Input some numbers till the user wants. Total them and print the total.




Q6)Print the sum of digits of a given integer.


enter number : 22
4


Q7)Check if the given number is an armstrong number.ex-153,407


Enter a  3 digit number : 407
407 - Armstrong number


Q8)Check if the given number is a palindrome number.


Enter a number : 22
The number is a palindrome!


Q12) WAP asking the user to guess a no from a given range. Do not allow more than 3 chances.


Enter a number : 3




Q13)Write a menu- driven program to-
1)Calculate sum
2)Calculate product
3)Calculate difference
4)Calculate division
5)Exit







1)Calculate sum
'sum'

2)Calculate product
'product'

3)Calculate difference
'difference'

4)Calculate division
'division'

5)Exit
'exit'



Enter 1st number : 2
Enter 2nd number : 3
Enter a command from syntax : sum
5
Enter 1st number : 33
Enter 2nd number : 33
Enter a command from syntax : exit


        Q14)Print prime numbers in range(2,100).


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
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99


15)Write a menu driven program to-

1)Check if the  given number is  Armstrong number.
'armstrong'

2)Check if the given number is  Palindrome number.
'palindrome'

3)Check if the given number is a  Perfect number.
(eg:- 28=1+2+4+7+14)sum of proper divisors.
'perfect'







Enter the number : 22
Enter a command from synrax : palindrome
The number is palindrome!
Enter the number : 3323
Enter a command from synrax : palindrome
Not a palindrome!
Enter the number : 1221
Enter a command from synrax : exit
PS C:\Users\agrimbishnoi\Desktop\STUFF\weekly 2 computer\assignment3>







'''
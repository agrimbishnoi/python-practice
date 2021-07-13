# This script is written by Agrim Bishnoi for fair use only.
# Date : 13/7/2021
# Assignment 1 python scripts.
# This assignment is on " if opperator "
# Entire output of script is attached.

# Q1. WAP to print two no. and print sum and product .

num1 = int(input("Enter value of first number : "))
num2 = int(input("Enter value of secong number : "))

print("Sum is ", num1 + num2)
print("product is ", num1 * num2)

# Q2. WAP to find the roots of a quadratic eq.

import math

sqrnum = int(input("Enter number to be square rootes : "))
print("Square root is ", math.sqrt(sqrnum))

# Q3.WAP to swap two no. without using third variable.

swap3 = int(input("Enter first number : "))
swap4 = int(input("Enter second number : "))

swapsum = swap3 + swap4

swap3 = swapsum - swap3
swap4 = swapsum - swap3

print("Swap numbers are ", swap3, " and ", swap4)

# Q4.WAP to swap two no. by using the third variable.

swap1 = int(input("Enter value of first no. : "))
swap2 = int(input("Enter value of second no. : "))

initialswap1 = swap1
swap1 = swap2
swap2 = initialswap1

print("Swap numbers are respectively ", swap1, swap2)

# 5. WAP to take two no. and print greater one or print equal.

newnum1 = int(input("Enter value of first number : "))
newnum2 = int(input("Enter value of second number : "))
if newnum1 > newnum2:
    print("first number is greater.")
elif newnum2 > newnum1:
    print("second number is greater.")
else:
    print("Equal numbers!")

# Q6. WAP to take the age of the user and print if they are
#eligible to vote or not.

age = int(input("Enter your age : "))
if age >= 18:
    print("You can vote!")
else:
    print("you cannot vote!")

# Q7. WAP to find largest out of three no. entered by the user.

number1 = int(input("Enter first number : "))
number2 = int(input("Enter second number : "))
number3 = int(input("Enter third number : "))

if (number1 > number2) and (number1 > number3):
    print("largest =", number1)
elif (number2 > number1) and (number2 > number3):
    print("largest =", number2)
elif (number3 > number1) and (number3 > number2):
    print("largest = ", number3)
else:
    print("All numbers are equal")
'''Q8.WAP to take the grade from the user and give remark as per
the table.

GRADE REMARK

A EXCELLENT
B VERY GOOD
C GOOD
D WORK HARD
E FAIL

'''
name = input("Enter name : ")

sub1 = int(input("Enter marks in subject 1 : "))
sub2 = int(input("Enter marks in subject 2 : "))
sub3 = int(input("Enter marks in subject 3 : "))
sub4 = int(input("Enter marks in subject 4 : "))
sub5 = int(input("Enter marks in subject 5 : "))

avg = (sub1 + sub2 + sub3 + sub4 + sub5) / 5

if avg >= 90:
    print("Grade A ")

elif avg < 90 and avg >= 80:
    print("Grade B")

elif avg < 80 and avg >= 60:
    print("Grade C")

elif avg < 60 and avg >= 40:
    print("Grade D")

elif avg < 40:
    print("Grade E")

else:
    print("error ! ")

#Q9.WAP to take the day of the week(1 to 7) and print the
#corresponding day of week.

weekno = int(input("Enter any number between 1-7 : "))

if weekno == 1:
    print("Monday")
elif weekno == 2:
    print("Tuesday")
elif weekno == 3:
    print("Wednessday")
elif weekno == 4:
    print("Thursday")
elif weekno == 5:
    print("Friday")
elif weekno == 6:
    print("Saturday")
elif weekno == 7:
    print("Sunday")
else:
    print("Wrong info entered.")
'''Q10. WAP to take a letter from user and print if letter is upper
case alphabet, lowercase alphabet, digit or some other
character
'''

character = input("Enter any character : ")[0]

if character.isupper():
    print("UPPERCASE alphabet.")

elif character.islower():
    print("LOWERCASE alphabet.")

else:
    print("Not an alphabet.")
'''Q11.WAP to accept monthly salary from the user, find and
display income tax with the help of following rules:
MONTHLY SALARY INCOME TAX
9000 OR MORE 40% of monthly salary
7500 - 8999 20% of monthly salary
7499 OR LESS 10% of monthly salary


'''

salary = int(input("Enter the salary : "))
if salary >= 9000:
    tax = salary * (40 / 100)
elif salary <= 8999 and salary >= 7500:
    tax = salary * (20 / 100)
elif salary <= 7499:
    tax = salary * (10 / 100)

print("Tax calculated is ", tax)

#Q12. WAP to accept 2 nos and an operator(+,-
#,*,/,//,%).According to operator,print the results.

operation1 = int(input("Enter first number : "))
operation2 = int(input("Enter second number : "))
operation = input(" + - * / % ")

if operation == '+':
    print("Addition of numbers id", operation1 + operation2)

elif operation == '-':
    print("Addition of numbers id", operation1 - operation2)

elif operation == '*':
    print("Addition of numbers id", operation1 * operation2)

elif operation == '/':
    print("Addition of numbers id", operation1 / operation2)

elif operation == '%':
    print("Addition of numbers id", operation1 % operation2)
else:
    print("Invalid opperation.")
'''
Q13. Calculate the Elecricity Bill according to points given
below:-
Units=Pres-Pres
for units upto 100.....3 rs /unit
for next 200 units...........5 rs/unit
above 300 units.........7rs/unit
meter rent=500
'''

unitpre = int(input("Enter no. of units of previous month : "))
unitpresent = int(input("Enter no. of units of present date : "))
unitval = unitpresent - unitpre

if unitval < 100:
    print("Bill : ", (unitval * 3) + 500)
elif unitval >= 100 and unitval < 200:
    print("Bill : ", ((100 * 3) + ((unitval - 100) * 5)) + 500)
else:
    print("Bill : ", ((100 * 3) + (200 * 5) + ((unitval - 300) * 7) + 500))

#OUTPUT ATTACHED:

'''

PS C:\Users\agrimbishnoi> & C:/Users/agrimbishnoi/AppData/Local/Programs/Python/Python37-32/python.exe "d:/workings/personal codes/assignments school;/assignent-practicle-1-1.py"
Enter value of first number : 23
Enter value of secong number : 23
Sum is  46
product is  529
Enter number to be square rootes : 9
Square root is  3.0
Enter first number : 5
Enter second number : 6
Swap numbers are  6  and  5
Enter value of first no. : 6
Enter value of second no. : 7
Swap numbers are respectively  7 6
Enter value of first number : 23
Enter value of second number : 34
second number is greated.
Enter your age : 3
you cannot vote!
Enter first number : 3
Enter second number : 4
Enter third number : 5
largest =  5
Enter name : agrim
Enter marks in subject 1 : 2
Enter marks in subject 2 : 33
Enter marks in subject 3 : 43
Enter marks in subject 4 : 53
Enter marks in subject 5 : 43
Grade E
Enter any number between 1-7 : 5
Friday
Enter any character : G
UPPERCASE alphabet.
Enter the salary : 50000
Tax calculated is  125000.0
Enter first number : 32
Enter second number : 23
 + - * / % +
Addition of numbers id 55
Enter no. of units of previous month : 233
Enter no. of units of present date : 2455
PS C:\Users\agrimbishnoi> & C:/Users/agrimbishnoi/AppData/Local/Programs/Python/Python37-32/python.exe "d:/workings/personal codes/assignments school;/assignent-practicle-1-1.py"
Enter value of first number : 34
Enter value of secong number : 343
Sum is  377
product is  11662
Enter number to be square rootes : 999
Square root is  31.606961258558215
Enter first number : 34
Enter second number : 233
Swap numbers are  233  and  34
Enter value of first no. : 343
Enter value of second no. : 3444
Swap numbers are respectively  3444 343
Enter value of first number : 34
Enter value of second number : 443
second number is greater.
Enter your age : 34
You can vote!
Enter first number : 34
Enter second number : 43
Enter third number : 355
largest =  355
Enter name : agrim
Enter marks in subject 1 : 55
Enter marks in subject 2 : 55
Enter marks in subject 3 : 55
Enter marks in subject 4 : 55
Enter marks in subject 5 : 55
Grade D
Enter any number between 1-7 : 7
Sunday
Enter any character : T
UPPERCASE alphabet.
Enter the salary : 500000
Tax calculated is  200000.0
Enter first number : 34
Enter second number : 43
 + - * / % /
Addition of numbers id 0.7906976744186046
Enter no. of units of previous month : 500
Enter no. of units of present date : 507
Bill :  521

'''
#This Script is prepared by Agrim Rai
#Assignment4- Strings functions and methods
#output and questions attached!
'''
QUESTIONS : 


Q1) Input any string and display it in the cyclic order.(exABC…ABC,BCA,CAB.) 
Q2) Print alternate characters of a string. 
Q3) Input any string convert each occurance of a given char in opposite case and print the string.(BOTH METHODS) 
Q4) Replace every occurance of a given character into opposite case.
Q5)WAP a program to find the frequency of any particular  alphabet in a string entered by a user. Also make a frequency Table for each alphabet. 
Q6) WAP to input a string and capitalize every word’s first letter.
Q7) Input any string and count the number of alphabets,digits and spaces. 
Q8) WAP to print reverse of given string.(Using SLICE & For loop) 
Q9) Check if given string is palindrome or not. 


Q10) PATTERN 

1)
a      
ab   
abc   
abcd

2)
abcd
abc
ab   
a 

3) (a)”INDIA”
I
I N
I N D
I N D I
I N D I A 

(b)
I N D I A 
I N D I
I N D
I N
I

 REPLICATION PATERN:
 
@ @ @ @ @
@ @ @ @
@ @ @
@ @
@


Q11) Count number of vowels in a given string.
 Q12) Find sum of digits from a given string.
 Q13) Remove vowels and form another string from given strig without vowels.
  Q14) Input any string,form another string where every alternate char is capitalized. 
   Q15) Replace all the occurances of “is” to “was”.
    Q16) Input a string and a substring.Display the position of substring in string.







'''


print('''

Q1) Print a string in cyclic order.

''')
str=input("Enter a string : ")
print(str[::-1])
print(str[::1])





print('''

Q2) Print alternate characters of string 

''')

strnew=input("Enter a string : ")
print(strnew[0::2])

print('''

Q3) Replace every occurace of character in opposite case.

''')
strnew=input("Enter a string : ")
for x in strnew:
    if x.lower()==True:
        print(x.upper,end='')
    elif x.upper()==True:
        print(x.lower,end='')
    else:
        print(x)





print('''

Printing frequency of a character in a string. 
Also print its frequency table.

''')


str=input("Enter any string : ")
ch=input("Char for counting : ")

c=str.count(ch)
print(c)
     





print('''

Q5)WAP a program to find the frequency of any particular alphabet in a string entered by a user. 
Also make a frequency Table for each alphabet.

''')

str=input("Give a string : ")
s=""
for x in str:
    if x not in s:
        s+=x
    print(x,' frequency has ',str.count(x))
print('alphabets in string are ',s)






print('''

Q6) WAP to input a string and capitalize every word’s first letter.

''')


str1=input("enter a string : ")
print(str1.title())






print('''

Q7) Input any string and count the number of alphabets,digits and spaces. 

''')


str2=input("enter a string")

a=0
d=0
s=0

for x in str2:
    if x.isalpha():
        a=a+1
    elif x.isdigit():
        d=d+1
    elif x.isspace():
        s=s+1


print("alpha : ",a)
print("digit : ",d)
print("space : ",s)







print('''

 WAP to print reverse of given string.(Using Slicing)

''')


str3=input("Enter a string : ")
print(str3[::-1])



print('''

Q9) Check if given string is palindrome or not

''')


my_str = input("Enter a string : ")
my_str = my_str.casefold()
rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
   print("palindrome.")
else:
   print("not a palindrome.")







print('''

Q15) Replace all the occurances of “is” to “was”.

''')


str4=input("Enter any string : ")
s=str4.replace('is','was')
print(str4)
print(s)





print('''

Q16) Input a string and a substring.Display the position of substring in string.

''')


str5=input("Enter a string : ")
sub=input("Enter a sub string : ")
print("Word is at ",str5.find(sub)," level ")







print('''

Q14) Input any string,form another string where every alternate char is capitalized

''')

str6=input("Enter a string : ")
s=''
for i in range(0,len(str6)):
    if i%2==0:
        s=s+str6[i].upper()
    else:
        s=s+str6.lower()

print(s)








print('''

Q13) Remove vowels and form another string from given strig without vowels. 

''')

str7=input("Enter a string : ")
s=''

for i in range(len(str7)):
    if str7[i] not in 'AEIOUaeiou':
        s=s+str7[i]
print(s)







print('''

Q12) Find sum of digits from a given string.

''')


str8=input("Enter a string : ")
s=0
for x in range(len(str8)):
    if str8[x].isdigit():
        s=s+int(str8[x])
    

print("Sum of digits is : ",s)



print('''

Q11) Count number of vowels in a given string.

''')



s=''
str9=input("enter a string : ")
for x in range(len(str9)):
    if str9[x] in 'AEIOUaeuio':
        s=s+str9[x]
print("Number of vovules are ",s)




print('''
patterns

a)
@
@ @
@ @ @
@ @ @ @
@ @ @ @ @

''')

for x in range(1,6):
    for i in range(1,x+1):
        print(" @ ",end='')
    print()
print('''

a
a b
a b c
a b c d


''')

pattercase='abcd'
for x in range(1,5):
    for i in range(0,x):
        print(pattercase[i] ,sep=' ' ,end=' ')
    print()


print('''

a b c d
a b c
a b
a

''')


pattercase='abcd'
for x in range(4,0,-1):
    for i in range(0,x):
        print(pattercase[i] ,sep=' ' ,end=' ')
    print()

print('''

I
IN
IND
INDI
INDIA

''')


pattercase='INDIA'
for x in range(0,6,1):
    for i in range(0,x):
        print(pattercase[i] ,sep=' ' ,end=' ')
    print()



print('''

INDIA
INDI
IND
IN
I


''')



pattercase='INDIA'
for x in range(5,0,-1):
    for i in range(0,x):
        print(pattercase[i] ,sep=' ' ,end=' ')
    print()








'''

OUTPUT GENERATED : 


PS C:\Users\agrimbishnoi\Desktop\everything\STUFF\weekly 2 computer\assignment4> python .\string.py


Q1) Print a string in cyclic order.


Enter a string : agrim rai
iar mirga
agrim rai


Q2) Print alternate characters of string


Enter a string : schoo;
sho


Q3) Replace every occurace of character in opposite case.


Enter a string : Tomatos
T
o
m
a
t
o
s


Printing frequency of a character in a string.
Also print its frequency table.


Enter any string : computer python
Char for counting : t
2


Q5)WAP a program to find the frequency of any particular alphabet in a string entered by a user.
Also make a frequency Table for each alphabet.


Give a string : javascript
j  frequency has  1
a  frequency has  2
v  frequency has  1
a  frequency has  2
s  frequency has  1
c  frequency has  1
r  frequency has  1
i  frequency has  1
p  frequency has  1
t  frequency has  1
alphabets in string are  javscript


Q6) WAP to input a string and capitalize every word’s first letter.


enter a string : bike car
Bike Car


Q7) Input any string and count the number of alphabets,digits and spaces.


enter a stringstrings123231
alpha :  7
digit :  6
space :  0


 WAP to print reverse of given string.(Using Slicing)


Enter a string : reversethis
sihtesrever


Q9) Check if given string is palindrome or not


Enter a string : nitin
palindrome.


Q15) Replace all the occurances of “is” to “was”.


Enter any string : he is good
he is good
he was good


Q16) Input a string and a substring.Display the position of substring in string.


Enter a string : agrim bishnoi
Enter a sub string : bis
Word is at  6  level


Q14) Input any string,form another string where every alternate char is capitalized


Enter a string : Agrim rrr
Aagrim rrrRagrim rrrMagrim rrrRagrim rrrR


Q13) Remove vowels and form another string from given strig without vowels.


Enter a string : aeiorisas
rss


Q12) Find sum of digits from a given string.


Enter a string : asd6sa76d6as7d6s7adas
Sum of digits is :  45


Q11) Count number of vowels in a given string.


enter a string : asdasdoapaa
Number of vovules are  aaoaaa

patterns

a)
@
@ @
@ @ @
@ @ @ @
@ @ @ @ @


 @
 @  @
 @  @  @
 @  @  @  @
 @  @  @  @  @


a
a b
a b c
a b c d



a
a b
a b c
a b c d


a b c d
a b c
a b
a


a b c d
a b c
a b
a


I
IN
IND
INDI
INDIA



I
I N
I N D
I N D I
I N D I A


INDIA
INDI
IND
IN
I



I N D I A
I N D I
I N D
I N
I
PS C:\Users\agrimbishnoi\Desktop\everything\STUFF\weekly 2 computer\assignment4>


















'''
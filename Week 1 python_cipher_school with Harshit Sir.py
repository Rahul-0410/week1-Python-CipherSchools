print("Hello world")
print("hello \"world\" world")
print("name\trahul")
# excercise1
print("this is \\\\ double backslash")
print("/\\/\\/\\/\\/\\")
print(" he is \t awesome")
print("\\\" \\n \\t \\\' ")
print(r"linea \n lineb")
# printing emoji by copying code from unicode.org
print("\U0001F600	")
print(2**0.5)
print(round(2**0.5))
print("(My name is rahul)")
number1=int(input())
number2=int(input())
total= number1+number2
print( "the total is "+ str(total))
name,age=input("enter your name and age").split()
print(name)
print(age)
# string formatting
name="Rahul"
age=20
print("hello {} your age is {}".format(name,age)) #python 3
print(f"hello {name} your age is {age +2}") #python 3.6
number1=int( input())
number2=int(input())
number3=int(input())
now= (number1+number2+number3)/3
print(now)
number1,number2,number3=input("enter three numbers").split(",")
print(f"the average of three numbers is : {(int(number1)+int(number2)+int(number3))/3}")
a=input("give your name: ")
print(a[::-1])


name,character=input("enter your name and charac:").split(",")
print(len(name))

print(character.count("a"))
print(f"length of name is: {len(name)}")
print(f"chara count: {name.count(character)}") #here it is case sensitive
# now to make the count case insensitive
print(f"charc count: {name.lower().count(character.lower())}")
name="    Rahul    "
# lstrip() method
dot="..............."
print(name + dot)
print(name.lstrip()+ dot)
print(name.rstrip()+dot)
print(name.strip()+dot)
name1="     Ra    hu l"
dots="................"
print(name1.replace(" ","")+ dots)
# center method
name= "Rahul"
print(name.center(9,"*"))
name=input("enter your name: ")
print(name.center(len(name) + 8,"*"))
# strings are immutable
string= "string"
print(string[1])
print(string.replace('t','T'))
print(string)
name="harsh"
name+="it"
print(name)

# if else
ageOfPerson=22
if ageOfPerson >18:
    print("you are eligible to vote")
else:
        print("you are not eligible to vote")
print(ageOfPerson>18)
print(ageOfPerson==18)
age=int(input("please enter your age"))
if age>=15:
    print("you are above 15")
# pass statement
x=18
if x>18:
    pass
age=int(input("please enter your age: "))
if age>=15:
    print("you are above 15")
else:
    print("you are not 15")
# nested if else
winning_number=int(5)
gussed_number=int(input("type your number in b/w 1 and 100: "))
if winning_number==gussed_number:
    print("You have won")
else:
    if winning_number>gussed_number:
            print("too low")
    if winning_number<gussed_number: # this is also correct
           print("too high")
    else:
        print("too high")
#  gueesing randowm numbers
import random
print(random.randint(0,100))
winning_number=random.randint(0,100)
gussed_number=int(input("type your number in b/w 1 and 100: "))
print(winning_number)
if winning_number==gussed_number:
    print("You have won")
else:
    if winning_number>gussed_number:
            print("too low")
    # if winning_number<gussed_number: # this is also correct
    #        print("too high")
    else:
        print("too high")


name='abc'
age=19
if name=='abc' and age==19: # if in and u want true then both must be true
    print("condition true")
else:
    print("condition false")
if name=='abc' or age==19: #if one of the two is true then true
    print("condition true")
else:
    print("condition false")
user_name=input("Please enter your name : ")
user_age=int(input("Please enter your age: "))
if user_age>=10 and ( user_name[0]=='a' or user_name=='A'):
    print("You can watch movie")
else:
    print("you can not watch movie")
# if elif else statement
age=int(input("please input your age: "))
if age==0 or age<0:
    print("you can't watch")
if 0<age<=3:
    print("Ticket price : Free")
elif 0<age<=3:
    print("Ticket price : Free")
elif 3<age <=10:
    print("Ticket price: 150")
elif 10<age<=60:
    print("ticket price : 250")
else:
    print("Ticket price:200 ")
name="Harshit"
if 'a' in name:
    print("a is presnt in name")
else:
    print("a is not in name")
name="abc"
if name:
    print("string is not empty")
else:
    print("string is empty")
name=input("Please enter your name: ")
if name:
    print(f"your name is: {name}")
else:
    print("type your name")


# loops
# while loop
i=2
while i<=10:
    print(f"hello world {i}")
    i=i+1
total=0
i=1
while i<=10:
    total=total+i
    i=i+1
print(total)

n=int(input("please put any number:"))
total=0
i=1
while i<=n:
    total=total+i
    i=i+1
print(total)

n=input("Give a number having more than one digit")
total=0
i=0
while i<len(n):
  total=total +  int(n[i])
  i=i+1
print(total)
name=input("Please type in your name:")
temp_var= ""
i= 0
while i < len(name):
    if name[i] not in temp_var:
      print(f"{name[i]} : {name.count(name[i])} ")
    temp_var+= name[i]
    i+= 1

    
# infinite loop
i=0
while i<=0:
    print("hello world")
while True:
    print("hello world")
# for loop
# for i in range(10): #0 to 9
# for i in range(1,11): # 1 to 10
#     print(f"hello world : {i}")
#     print("this is line \n")
# total=0
# for i in range(1,11):
#     total+= i
# print(total)
# n=int(input("enter the number: "))
# total=0
# for i in range(1,n+1):
#     total+=i
# print(total)
# total=0
# num=input("enter a number: ")
# for i in range(0,len(num)):
#     total+=int(num[i])
# print(total) 
# name=input("please enter your name:")
# temp=""
# for i in range(len(name)):
#     if name[i] not in temp:
#         print(f"{name[i]} :{name.count(name[i])}")
#         temp += name[i]

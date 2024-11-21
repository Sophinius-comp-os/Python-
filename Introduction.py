#Print is a method used execute the output
from http.cookiejar import uppercase_escaped_char

print("Welcome to SkTech")
print("Welcome to Python Programming")
print(20+30)


#Variable is a memory location used to store data

school = "SkTech"
firstname = "Sk"
lastname = "Tech"
number = 100
num1 = 20
num2 = 30
print(school)
print(firstname)
print(lastname)
print(number)
print(firstname,lastname)

#Data type-it is categorization or classification of data
number =int(67) #integer
second = float(34.5)
greetings = str("Hello Sk")
isSKADev = bool(True)


#Data structures in Python Programming-Multiple values in a single variable.
fruits =['Oranges', 'Mangoes','Banana'] #Lists --Ordered and changeable
cars = ("Toyota", "Mercedes","Audi") #Tuples --Ordered and unchangeable
countries = {'Kenya', 'Somalia', 'Algeria'} #Sets  -Unordered and unchangeable
student = {
    "firstname":"Koech",
    "age": 25,
     "Occupation": "Software Engineer",
    "gender": "Male",
    "location": "Nairobi"
} #Dictionary -Key value pairs

print(student)
print(cars)
print(fruits)
print(countries)
print(student["age"])

print(number)
print(second)
print(greetings)
print(isSKADev)


#Determining a datatype
print(type(fruits))
print(type(student))
print(type(countries))


#Typecasting
print(float(67))
print(int(second))

#Checking for a leap year
year = int(input("Enter  your year: "))
if  year % 4 == 0:
   if year % 100 == 0:
    if year % 400 == 0:
        print("leap year!")
    else:
     print("not a leap year!")
   else:
    print("leap year!")




#String-Combining the text.
text = "Hello Python"
print(text)

#Accessing an element in a string

print(text[0])

#Length of a string
print(len(text))

#Modifying a string

print(text.upper())
print(text.lower())

#String concatenation-Joining strings
greetings ="Hello Sk"
Firstname ="Software Engineer"

print(greetings +" " + Firstname)
print(greetings+ Firstname)


#Operators -
#Arithmetic Operators

Num1= 22
Num2 = 12

print(Num1+Num2)
print(Num1*Num2)
print(Num1/Num2)
print(Num1-Num2)
print(Num1%Num2) #Modules -Returns the remainder

#Comparision Operators
print(Num1<Num2)
print(Num1>Num2)
print(Num1>=Num2)
print(Num1<=Num2)
print(Num1==Num2)
print(Num1!=Num2)

#Assignment Operators
x = 5
x += 4
x -= 4
x *= 4
x /= 4
x %= 4

#Logical Operators -and , or , not
print(23 < 6 and 16 < 10 )
print(23 < 6 or 16 < 10 )
print(not(23 < 6 or  16 < 10 ))


#Control Statements
temperature = 15
if temperature > 25:
    print("it's too hot")
elif temperature < 25:
    print("it's too cold")
else:
    print("Void")

#checks the smallest number
    #num3 =12
    #num4 = 65
    #num5 = 23
    num3 = int(input("Enter first number: "))
    num4 = int(input("Enter second number: "))
    num5 = int(input("Enter third  number: "))

    if num3 < num4 and num3 < num5:
        print("It's the smallest number")
    elif num4 < num5 and num4 < num5:
        print("num4,is the smallest number")
    else:
        print("num5, Is the smallest number")

#Checking even numbers
number =50
if number % 2 == 0:
    print("Number, it is an even number")
else:
    print("Number, it is an odd number")

#Loops in python
#While loop
x =20
while x <= 25:
    print(x)
    x += 1

    #Decreasing numbers
    count = 105
    while count >= 100:
        print(count)
        count -= 1

#For loop
for x in range(1,5):
   print(x)
for num in range(1,11,2):
    print(num)

#list
languages = ["Python","C++","Java"]
for language in languages:
    print(language)
    
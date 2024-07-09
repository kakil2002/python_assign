# Assignment-1: if condition
# Check if a person is eligible to vote based on their age

# Input: Age of the person

# Check if the person is eligible to vote

age=int(input("enter the age:"))
if age>=18:
    print("eligible to vote")
if age<18:
    print("not eligible to vote")

# Assignment-2: if else condition
# WAP that checks whether a number is positive or negative
num=int(input("enter the number:"))
if num>=0:
    print("number is positive")
else:
    print("number is negative")

# Assignment-3: if else condition
# WAP that Checks if a given number is even or odd

num=int(input("enter the number:"))
if num%2==0:
    print("even number")
else:
    print("odd number")

# Assignment-4: nested if condition
# WAP to find the greatest of 3 numbers
num1=int(input("enter the number1:"))
num2=int(input("enter the number2:"))
num3=int(input("enter the number3:"))
if num1>num2:
    if num2>num3:
        print("num1 is greater")
if num2>num1:
    if num2>num3:
        print("num2 is greater")
if num3>num1:
    if num3>num2:
        print("num3 is greater")
# Assignment-5: nested if else condition
"""

Movie Ticket Pricing
Imagine a movie theater that offers different ticket prices based on the age of the customer and the time of the day. The rules might be as follows:

Regular price: $10
Children under 12 and seniors over 65 get a 50% discount.
Matinee show (before 5 PM) offers a 25% discount to all.
"""
Regular_price=10
age=int(input("enter the age:"))
time=int(input("enter the time:"))
if time<17:
    if age<12 or age>65:
        discount_price=Regular_price*(75/100)
    else:
        discount_price=Regular_price*(25/100)
else:
    if age<12 or age>65:
        discount_price=Regular_price*(50/100)
    else:
        discount_price=0
ticket_price=Regular_price-discount_price
print(f"move ticket price is:{ticket_price}")


# Assignment-6: nested if else condition
# WAP to find the biggest country among 3 based on the population
country_1=int(input("enter the country_1:"))
country_2=int(input("enter the country_2:"))
country_3=int(input("enter the country_3:"))
if country_1>country_2:
    if country_1>country_3:
        print("country_1 is greater")
    else:
        print("country_3 is greater")
else:
    if country_2>country_3:
        print("country_2 is greater")
    else:
        print("country_3 is greater")





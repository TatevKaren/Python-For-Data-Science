#
number = 10
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

age = 20
if age >= 90:
    age_cat = "90+"
elif age >=80:
    age_cat = "80-90"
elif age >=70:
    age_cat = "70-80"
elif age >=60:
    age_cat = "60-70"
else:
    age_cat = "60-"

print("Your age category is", age_cat)


number = -999

if number > 0:
    print("The number is positive", number )
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is negative or 0", number)


age = 18
income = 1000
if age >= 16 and income >= 5000:
    print("Person is allowed to buy a car")
else:
    print("Person is not allowed to buy a car")


for number in range(1, 10):
    #print(number)
    if number == 7:
        print(number)
        break


for number in range(1, 10):
    print(number)
    if number == 7:
        print(number)
        continue

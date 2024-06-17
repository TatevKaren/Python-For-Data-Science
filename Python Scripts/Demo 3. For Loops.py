fruits = ["banana", "apples", "peers", "pineapples", "oranges"]
# For loop to loop through list
for fruit in fruits:
    print(fruit)

for fruit in fruits:
    print(fruit + " times 2")

# Looping through string to spell it out
string_ = "banana"
for char in string_:
    print(char)

# Nested For Loops to loop through each fruit in the list and spell it out
for fruit in fruits:
    print("First For Loop: Fruit we are spelling out",fruit)
    for char in fruit:
        print(char)

# For loop to print all numbers from 1, 2, ..., 10
for num in range(1, 11):
    print(num)

# For loop to print all numbers from 1, 2, ..., 100
for num in range(1, 101):
    print(num)

# For loop to print a statement 100 times
for num in range(100):
    print("Welcome to the World of Data Science")

# Nested For Loop with double Ranges from 1, 14 to get pairwise summation
for i in range(1, 15):
    for j in range(1, 15):
        print("i = ", i, " and j = ", j)
        print(i + j)

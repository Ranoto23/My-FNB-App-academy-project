#Control Statements

num = 0

if num > 0:
    print("This number is positive")
elif num == 0:
    print("This number is zero")
else:
    print("This number is negative")
    
#Intermediate Control Statements

num1 = int(input("Enter the first number:  "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(num1,"is greater than", num2)
elif num2 > num1:
    print(num2, "is greater than", num1)
else:
    print("Both numbers are equal")
    
#Advanced Control Statements

# Loop Control Statements

fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "cherry":
        break # Exits the loop if cherry is found
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "cherry":
        continue # Skips cherry and moves to the iteration
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "cherry":
        pass # Placeholder, no action is needed for cherry8
    print(fruit)
    
    #Using a while loop to count
    
    count = 1
    
    while count <= 5:
        print(count)
        count += 1 # Increments the count by 1
        if count == 3:
            break # Exits the loop when the count reach - 3
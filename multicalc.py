#assignment 1 ask first number ask operator ask third number display result
#assignment 2 even odd results (ask, print if even or odd)
#assignment 3 ask for input; if / by 3, print fizz; if / by 5 print buzz; if both print fizz buzz

#ASSIGNMENT 1



print("Select Operation.")
print("1. Addition.")
print("2. Subtraction")
print("3. Multiplication.")
print("4. Division.")
operator = input("Enter choice (1/2/3/4): ")


no1 = float(input("Enter First Number: "))
no2 = float(input("Enter Second Number: "))



def add(no1,no2):
    sum = no1+no2
    return sum

def subtract(no1,no2):
    diff = no1-no2
    return diff

def multiply(no1,no2):
    mult = no1*no2
    return mult

def divide(no1,no2):
    div = no1/no2
    return div



if operator == "1":
    print(no1,"+", no2, "=", add(no1,no2))

elif operator == "2":
    print(no1, "-", no2, "=", subtract(no1,no2))

elif operator == "3":
    print(no1, "*", no2, "=", multiply(no1,no2))

elif operator == "4":
    print(no1, "/", no2, "=", divide(no1,no2))

else:
    print("Invalid Input")

#assignment 3 ask for input; if / by 3, print fizz; if / by 5 print buzz; if both print fizz buzz


num = int(input("Enter Whole Number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FIZZ BUZZ")
elif num % 3 == 0:
    print("FIZZ!!!!")
elif num % 5 == 0:
    print("BUZZ!!!!")
#if num % 3 == 0 and num % 5 == 0:
    #print("FIZZ BUZZ")

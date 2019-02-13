#enter total
#enter tip
#create function to calculate tip and print() for user


total_amount = input('Enter Total Amount: ')
tip_amount = input('Enter Tip %: ')

def tip_percent(a,b):
    #return total_amount / tip_amount = tip_total
    tip_total = float(a) * float(b) / 100
    return tip_total

tip_total = tip_percent(total_amount,tip_amount)
#print("Tip total would be " + tip_percent) error: cannot concatenate str to str; error with float?
print("Your tip would be " + "$" + str(tip_total) + ".")

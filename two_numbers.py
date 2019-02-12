#input two numbers from user
#have both numbers added
#print results for user to see

no1 = input('Number one: ')
no2 = input('Number two: ')

def add(a,b):
    result = float(a) + float(b)
    return result

result = add(no1,no2)
print('And the total is... ' + str(result) + '.')
  

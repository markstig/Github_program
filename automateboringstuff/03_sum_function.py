# create a sum function and factorial function


print('Please enter a number, we will show you the total and its factorial number.')

num = int(input('Please enter your number: '))

snum = 0
fnum = 1

for i in range(1, num+1):
    snum += i
    fnum *= i

print('The total number is ' + str(snum))
print('The factorial number is ' + str(fnum))

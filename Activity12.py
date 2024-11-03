 #Write a program to check whether the given values have boolean values or not.

a = 16
b = 64
c = 10

if a and b and c:
    print('All of values have boolean values as true')
else:
    print('All of the boolean values are false')
x = -6
y = 15
z = 81

if x>0 or y>0:
    print('Either of the numbers are greater than the number 0.')
elif y<80 or z<80:
    print('Either of the numbers are less than the number 80.')
else:
    print('Invalid numbers.')
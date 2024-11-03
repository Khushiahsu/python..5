#Write a program to calculate the BMI of a person?
a = float(input('Enter your weight'))
b = float(input('Enter your height now'))
print(a,'and', b)

bmi=a/(b/100)**2
print(bmi)
if bmi<18.4:
    print('You are underweight.')
elif bmi<=24.9:
    print('You are healthy.')
elif bmi <= 29.9:
    print('You are overweight')
elif bmi<= 39.9:
    print('You are obese')
else:
    print('Go to the gym')
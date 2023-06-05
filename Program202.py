# Write a program to find the roots of quadratic equation.
import math

print('The general form of a quadratic equation is : ax^2 + bx + c')
a = int(input('Enter the value of a : '))
b = int(input('Enter the value of b : '))
c = int(input('Enter the value of c : '))

root1 = (-b + math.sqrt((b**2)-(4*a*c)))/(2*a)
root2 = (-b - math.sqrt((b**2)-(4*a*c)))/(2*a)

print('The first root of the quadratic is : ',root1)
print('The Second root of the quadratic is : ',root2)

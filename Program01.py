# Write a menu driven programs to
# a. Accept the minutes and print its equivalent hours [ if minutes &lt; 60, print the
# minutes, if m = 65 then print 1 hour 5 minutes, if m = 60, then print 1 hour ]
# b. To compute greatest common divisor (GCD) and least common multiple (LCM) of
# two integers
import math

def main():
    print('1. Minutes to hours Calculator')
    print('2. Compute GCD and LCM of 2 integers')
    uc = int(input('Enter your choice : '))

    if(uc == 1):
        mins = int(input('Enter the number of minutes : '))
        hours = mins // 60
        min = mins % 60
        print(hours,' hour(s)',min,' minute(s)')
    elif(uc == 2):
        n1 = int(input('Enter the first number : '))
        n2 = int(input('Enter the second number : '))
        hcf = math.gcd(n1,n2)
        lcm = math.lcm(n1,n2)
        print('GCD = ',hcf)
        print('LCM = ',lcm)

    else:
        print('Wrong number entered, please try again !!')

main()
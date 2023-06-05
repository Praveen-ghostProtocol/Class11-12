# Write a program to accept the consumer name, EB number, number of units and type
# of consumption [ D – Domestic , C – commercial ] Calculate the amount to be paid
# based on the following criteria
# For Domestic purpose
# a. for the first 100 units - No charges
# b. for units 101- 200, Rs.7 per unit
# c. for units 201-300, Rs. 9.50 per unit
# d. for units 301 and above Rs. 12 per unit.
# For Commercial purpose
# a. for the first 100 , Rs. 10 per unit
# b. for units 101- 200, Rs. 25 per unit
# c. for units 201-300, Rs. 40 per unit
# d. for units 301 and above Rs. 55 per unit.
# Print the bill in a neat format

from typing import ChainMap


cname = input('Enter the name of the consumer : ')
ebno = int(input('Enter the EB Number : '))
units = int(input('Enter the number of units consumed : '))
type = input('Enter C for Commercial and D for Domestic type of consumption : ')
charge = 0

if(type.upper() == 'C'):
    if(units <= 100):
        charge = 0
    elif(units > 100 and units <= 200):
        charge = (units-100)*7
    elif(units < 200 and units<= 300):
        charge = (100*7)+((units-200)*9.5)
    else:
        charge = (100*7)+(100*9.5)+((units-300)*12)
elif(type.upper() == 'D'):
    if(units <= 100):
        charge = units*10
    elif(units > 100 and units <= 200):
        charge = (100*10)+((units-100)*25)
    elif(units < 200 and units<= 300):
        charge = (100*10)+(100*25)+((units-200)*40)
    else:
        charge = (100*10)+(100*25)+(100*40)+((units-300)*55)

print('\t\t\tELECTRICITY BILL')
print('CONSUMER NAME       : ',cname)
print('EB NUMBER           : ',ebno)
if(type.upper() == 'C'):
    print('TYPE OF CONSUMPTION : Commercial')
else:
    print('TYPE OF CONSUMPTION : Domestic')
print('NUMBER OF UNITS     : ',units)
print('TOTAL AMOUNT        : ',charge)

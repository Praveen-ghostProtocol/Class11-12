#   Write a program to accept the name and the basic pay of an employee and print the neat
# salary slip for the employee. [ DA = 20% of BP, HRA = 30% of BP, TA = 10% of BP, PF
# = 13% of BP, IT = 5% of BP, Gross =BP+TA+DA+HRA , Deduction = PF+IT,
# Net pay = Gross – Deduction]  
# Print the Salary slip of the employee in a neat format

ename = input("Enter the employee name : ")
bp = int(input("Enter the basic pay : "))
da = 0.2*bp
hra = 0.3*bp
ta = 0.1*bp
pf = 0.13*bp
it = 0.05 * bp
gross = bp + ta + da + hra
ded = pf + it
net = gross - ded

print('\t\t\t SALARY SLIP')
print('\t\t\t -----------')
print('NAME : ',ename)
print('-'*40)
print('BASIC PAY: ',bp,'\tPF:',pf)
print('D.A      : ',da,'\tIT',it)
print('H.R.A    : ',hra)
print('T.A      : ',ta)
print('Gross    :',gross,'\tDeduction: ',ded)
print('NET PAY  :',net)
print('-'*40)

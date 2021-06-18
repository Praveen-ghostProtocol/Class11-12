# Write a program that takes any two Lists L and M of the same size and adds their elements
# together to form a new list N. for eg. l =[3,1,4] and M =[1,5,9] then N should be [4,6,13]

n = int(input('Enter the number of elements in the lists : '))

L = []
M = []

print('Enter ',n,' integers')
for i in range(0,n):
    L.append(int(input()))

print('Enter ',n,' integers')
for i in range(0,n):
    M.append(int(input()))

sum = []
for i in range(0,n):
    sum.append(L[i]+M[i])

print('New list is : ')
print(sum)
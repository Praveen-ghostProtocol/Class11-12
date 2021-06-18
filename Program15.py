# Accept N numbers in the List L. Shift the elements in the given pattern.[no parallel list]
# Eg. L = [11,45,67,89,100] after shift L=[100,89,67,45,11]

n = int(input('Enter the number of integers in the numbers : '))
nums = []

print('Enter ',n,' integers')
for i in range(0,n):
    nums.append(int(input()))

nums.reverse()

print(nums)
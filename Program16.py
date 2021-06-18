# Accept N numbers in the List L. Shift the elements in the given pattern.[no parallel list]
# Eg. L = [1,2,3,4,5,6] after shifting L =[2,1,4,3,6,5]

n = int(input('Enter the number of integers in the numbers : '))
nums = []

print('Enter ',n,' integers')
for i in range(0,n):
    nums.append(int(input()))

for i in range(0,n,2):
    temp = nums[i+1]
    nums[i+1] = nums[i]
    nums[i] = temp

print(nums)
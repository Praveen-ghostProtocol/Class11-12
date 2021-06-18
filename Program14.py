# Accept N numbers in the List L. Shift the elements in the given pattern.
# Eg. L = [1,2,3,4,5,6] after shifting L =[6,1,2,3,4,5] [no parallel list]

n = int(input('Enter the number of integers in the numbers : '))
nums = []

print('Enter ',n,' integers')
for i in range(0,n):
    nums.append(int(input()))

nums.insert(0,nums[n-1])
nums.pop()

print(nums)
# Write a program that inputs a list of numbers and shift all the zeroes to right and all non-zero
# numbers to left of the list. [ without using parallel list]
nums = []
n = int(input('Enter the number of integers in the numbers : '))

print('Enter ',n,' integers')
for i in range(0,n):
    nums.append(int(input()))

insert_index = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[insert_index]=nums[i]
        insert_index+=1
for i in range(insert_index,len(nums)):
    nums[i]=0

print('The changed list is : ')
print(nums
)
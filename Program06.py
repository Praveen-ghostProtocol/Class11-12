# Write a program that takes a string with multiple words and then capitalizes the first letter of
# each word and forms a new string containing first letters of each word.

str = input('Enter a string : ').strip()

word = str.title()

print('Original String : ',str)
print('Capitalize string : ',word)

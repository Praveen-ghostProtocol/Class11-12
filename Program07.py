# Write a program that should accept a line. It should then print the given line and the following
# statistics relating to the line:
# i) Number of words ii) number of characters iii) percentage of character that are alpha numeric

str = input('Enter a line : ').strip()

words = 1
chars = 0
alphanum = 0

for char in str:
    if(char.isspace()):
        words = words + 1
    elif(char.isalnum()):
        alphanum = alphanum + 1

chars = len(str)
percentage = (alphanum/chars)*100.0

print('The number of words are : ',words)
print('The number of characters are : ',chars)
print('The percentage of alphanumeric characters are : ',percentage)

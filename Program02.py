#  Python Programs to print the following patterns
# 54321/ 5432/ 543/ 54/ 5
#  A/BB/CCC/..... N rows
# a/ 12/ bcd/ 3456/.... N rows

def main():
    
    for i in range(5,-1,-1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print()

    n = int(input('Enter the value of N : '))
    k = 65
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(chr(k),end=" ")
        k = k + 1
        print()
    
    n = int(input('Enter the value of N : '))
    k1 = 97
    k2 = 1
    l1 = 1
    l2 = 2
    for i in range(1,n+1):
        if(i % 2 != 0):
            for j in range(1,l1+1):
                print(chr(k1),end=' ')
                k1 = k1 + 1
            print()
            l1 = l1 + 2
        else:
            for j in range(1,l2+1):
                print(k2,end=' ')
                k2 = k2 + 1
            l2 = l2 + 2
            print()
        
main()


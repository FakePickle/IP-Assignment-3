#printing the top half of the diamond using recursion
def top_half(n,count = 0):
    if n==1:
        print('* '*n + ' '*(count*2) + '* '*n)
    else:
        print('* '*n + ' '*(count*2) + '* '*n)
        top_half(n-1,count+2)

#printing the bottom half of the diamond using recursion
def bottom_half(n,count = 2):
    if n == 1:
        pass
    elif n == 2:
        print('* '*count + ' '*((n-2)*4) + '* '*count)
    else:
        print('* '*count + ' '*((n-2)*4) + '* '*count)
        bottom_half(n-1,count+1)

#drivers code
if __name__ == '__main__':
    n = int(input("Enter the size of the diamond : "))
    top_half(n)
    bottom_half(n)
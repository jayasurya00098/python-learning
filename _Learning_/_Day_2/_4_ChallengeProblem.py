# Given a number N, print all the digits from right to left 
# Print the number in Reverse

# if N = 453, then print 3 5 4
# if N = 1918, then print 8 1 9 1

N = int(input('Enter A Number: '))

while N > 0 :
    print ( N % 10 , end = '')
    N = N // 10
# FizzBuzz
# N as input int
# 1. If N is a multiple of 3, print "Fizz"
# 2. If N is a multiple of 5, print "Buzz"
# 3. If N is a multiple of both 3 & 5, print "FizzBuzz"

# ex: 
# input N = 15 
# 15 % 3 = 0 
# 15 % 5 = 0
# then print "FizzBuzz"

# ex: 
# input N = 18 
# 15 % 3 = 0 
# 15 % 5 = 3
# then print "Fizz"

# ex: 
# input N = 20 
# 15 % 3 = 2 
# 15 % 5 = 0
# then print "Buzz"

# ex: 
# input N = 17 
# 15 % 3 = 2 
# 15 % 5 = 2
# then print Nothing

N = int(input('Enter a value for N: '))  
if N % 3 == 0 and N % 5 == 0 :
    print("FizzBuzz")
elif N % 3 == 0 :
    print("Fizz")
elif N % 5 == 0 :
    print("Buzz")
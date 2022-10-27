#for loops in python is different from other languages

#range(5) = 0,1,2,3,4 - parameter (endValue)
#range(1,5) = 1,2,3,4 - parameter (startValue, endValue)
#range(1,5,2) = 1,3 - parameter (startValue, endValue, jump)

print("Print Values in Range")

N = int(input('Enter a Value: '))

for i in range(N) :
    print(i)

print("-------------------------")

print()
print("Print Values in Range with Start and End Values")

S = int(input('Enter Range Start Value: '))
E = int(input('Enter Range End Value: '))

for i in range(S, E) :
    print(i)

print("-------------------------")

print()
print("Print Values of the sum of all even number in the range")

R = int(input('Enter Range Value: '))
sum = 0
for i in range(2, R + 1, 2) :
    sum += i

print(sum)

print("-------------------------")
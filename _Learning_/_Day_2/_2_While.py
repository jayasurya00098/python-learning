#while loop

#print number 1 to 10

print("Print number 1 to 10")

i = 1
while i <= 10:
    print(i)
    i += 1

print("-------------------------")

#print number 1 to 6 in the same line

print("Print number 1 to 6 in the same line")

j = 1
while j <= 6:
    #end with a space to avoid new line
    print(j, end = ' ')
    j += 1

print()
print("-------------------------")

#print all the even numbers from 1 to Q

print("Print all the even numbers from 1 to Q")

Q = 25
k = 1
while k <= Q :
    if k % 2 == 0 :
        print(k)
    k += 1

print("-------------------------")

#print number from R to 1

R = int(input('Enter a Value for R: '))

while R >= 1 :
    print(R)
    R -= 1

print("-------------------------")
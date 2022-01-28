# Find the sum of integers from a to b - 2

print("Find the sum of integers from a to b.")
a = int(input("Enter the integer a : "))
b = int(input("Enter the integer b : "))

if a > b:
    a, b = b, a

sum = 0
for i in range(a,b):
    print(f"{i} + ", end='')
    sum += i

print(f"{b} = ", end='')
sum += b

print(sum)
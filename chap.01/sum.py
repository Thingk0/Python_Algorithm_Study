# Find the sum of integers from a to b - for

print("Find the sum of integers from a to b.")
a = int(input("Enter the integer a : "))
b = int(input("Enter the integer b : "))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b+1):
    sum += i

print(f"\nThe sum of integers from {a} to {b} is {sum}")
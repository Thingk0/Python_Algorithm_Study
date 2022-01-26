# Find the sum of integers from 1 to n - for

print("Find the sum of integers from 1 to n.")
n = int(input("Enter the value n: "))

sum = 0
for i in range(1, n+1):
    sum += i

print(f"\nThe sum of integers from 1 to {n} is {sum}")
# Find the sum of integers from 1 to n - while

print("Find the sum of integers from 1 to n.")
n = int(input("Enter the value n: "))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(f"\nThe sum of integers from 1 to {n} is {sum}")
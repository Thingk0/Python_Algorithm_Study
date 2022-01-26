# Get 3 integers and get the maximum value.

print("Find the maximum value of the three integers.")

num_1 = int(input("Enter the Number 1 : "))
num_2 = int(input("Enter the Number 2 : "))
num_3 = int(input("Enter the Number 3 : "))

num_max = num_1

if num_2 > num_max:
    num_max = num_2

if num_3 > num_max:
    num_max = num_3

print(f"\nThe Maximum value is {num_max}")
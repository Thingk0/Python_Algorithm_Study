# Get the median from the three integers.

def med3(a, b, c):
    # a, b, c : Find the median value and return it.
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b


print("Find the median value of the three integers.")
a = int(input("Enter the Number 1 : "))
b = int(input("Enter the Number 2 : "))
c = int(input("Enter the Number 3 : "))

print(f"The median value is {med3(a,b,c)}")
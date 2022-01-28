# * Print out the shape n times, but change the line for every w (1)
# *를 n개 출력하되 w개마다 줄바굼하기 (1)

print("Print out '*'")
n = int(input("How many should I print out?: "))
w = int(input("How many '*' should I change the line?: "))

for i in range(n):
    print('*', end='')
    if i % w == w - 1:
        print()

if n % w:
    print()
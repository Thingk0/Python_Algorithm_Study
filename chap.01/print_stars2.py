# * Print out the shape n times, but change the line for every w (2)
# * 를 n개 출력하되 w 개마다 줄바굼하기 (2)

print("Print out '*'")
n = int(input("How many should I print out?: "))
w = int(input("How many '*' should I change the line?: "))

for _ in range(n // w):
    print('*' * w)

rest = n % w
if rest:
    print('*' * rest)
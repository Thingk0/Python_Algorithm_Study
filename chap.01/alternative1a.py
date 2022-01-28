# +와 -를 번갈아 출력하기 1 (for)
# Take turns printing + and - (for)

print("Outputting + and - alternately.")
n = int(input("How many should I print out?: "))

for i in range(1, n+1):
    if i % 2:   # odd numbers
        print('-', end='')
    else:       # even numbers
        print('+', end='')

print()
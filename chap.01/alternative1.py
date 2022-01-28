# +와 -를 번갈아 출력하기 1
# Take turns printing + and -

print("Outputting + and - alternately.")
n = int(input("How many should I print out?: "))

for i in range(n):
    if i % 2:   # odd numbers
        print('-', end='')
    else:       # even numbers
        print('+', end='')

print()
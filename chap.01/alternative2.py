# +와 -를 번갈아 출력하기 2
# Take turns printing + and -

print("Outputting + and - alternately.")
n = int(input("How many should I print out?: "))

for _ in range(n // 2):
    print('+-', end='')

if n % 2:
    print('+', end='')

print()
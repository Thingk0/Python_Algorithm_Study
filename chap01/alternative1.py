# Do it! 실습 1-12
# + 와 - 를 번갈아 출력하기 1

# 22.05.08 Check

print("+와 -를 번갈아 출력합니다.")
n = int(input("몇 개를 출력할까요?: "))

for i in range(n):
    if i % 2:   # odd numbers
        print('-', end='')
    else:       # even numbers
        print('+', end='')

print()

# Do it! 실습 1-12
# + 와 - 를 번갈아 출력하기 1 ( for 문 수정 )

# 22.05.08 Check

print("+와 -를 번갈아 출력합니다.")
n = int(input("몇 개를 출력할까요?: "))

for i in range(1, n + 1):
    if i % 2:   # odd numbers
        print('+', end='')
    else:       # even numbers
        print('-', end='')

print()

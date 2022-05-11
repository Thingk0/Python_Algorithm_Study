# Do it! 실습 1-13
# + 와 - 를 번갈아 출력하기 2

# 22.05.08 Check

print("+와 -를 번갈아 출력합니다.")
n = int(input("몇 개를 출력할까요?: "))

for _ in range(n // 2):
    print('+-', end='')     # +- 를 n // 2 개 출력

if n % 2:
    print('+', end='')      # n 이 홀수라면 + 출력

print()

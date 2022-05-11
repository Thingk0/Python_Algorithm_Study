# Do it! 실습 1-15
# * 를 n개 출력하되 w 개마다 줄바꿈하기 2

# 22.05.08 Check

print("*를 출력합니다.")
n = int(input("몇 개를 출력할까요?: "))
w = int(input("몇 개마다 줄바꿈할까요?: "))

for _ in range(n // w):          # n // w 번 반복
    print('*' * w)

rest = n % w
if rest:                         # if 문 판단 -> 1번
    print('*' * rest)
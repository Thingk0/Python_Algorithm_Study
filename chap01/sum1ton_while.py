# Do it! 실습 1-7
# 1부터 n까지 정수의 합 구하기 1 (while)

# 22.05.08 Check

print("1부터 n까지 정수의 합을 구합니다.")
n = int(input("n값을 입력하세요.: "))

sum = 0
i = 1

while i <= n:       # i가 n보다 작거나 같을 동안 반복
    sum += i        # sum 에 i를 더함
    i += 1          # i 에 1을 더함

print(f"1부터 {n}까지 정수의 합은 {sum}입니다.")
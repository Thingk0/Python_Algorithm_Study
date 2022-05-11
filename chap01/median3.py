# Do it! 실습 1C-2
# 세 정수를 입력받아 중앙값 구하기 1

# 22.05.08 Check


def med3(a, b, c):
    if a >= b:
        if b >= c:
            # c <= b <= a
            return b
        elif a <= c:
            # b <= a <= c
            return a
        else:
            # b <= c <= a
            return c
    elif a > c:
        # c < a < b
        return a
    elif b > c:
        # a < c < b
        return c
    else:
        # c < b < a
        # a < b < c
        return b


print("세 정수의 중앙값을 구합니다.")
a = int(input("정수 a의 값을 입력하세요.: "))
b = int(input("정수 b의 값을 입력하세요.: "))
c = int(input("정수 c의 값을 입력하세요.: "))

print(f"중앙값은 {med3(a,b,c)} 입니다.")
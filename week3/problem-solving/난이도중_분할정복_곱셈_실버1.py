# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629
def divide_conquer(x, y, z):
    x %= z
    if y == 0:
        return 1
    half = divide_conquer(x, y // 2, z)

    if y % 2 == 0:
        return (half * half) % z
    else:
        return (half * half * x) % z

x, y, z = map(int, input().split())
print(divide_conquer(x, y, z))
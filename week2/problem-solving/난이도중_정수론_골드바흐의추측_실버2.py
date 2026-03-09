# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020

def is_prime(n):
    if n < 2:
        return False
    if n != 2 and n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

N = int(input())

result = []
for i in range(N):
    num = int(input())
    a = num // 2
    b = num // 2
    while a > 1:
        if is_prime(a) and is_prime(b):
            result.append((a, b))
            break
        a -= 1
        b += 1

for i in result:
    print(*i)
# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

def is_prime(n):
    if n < 2:
        return False
    if n != 2 and n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
nums = list(map(int, input().split()))
cnt = 0

for i in nums:
    if is_prime(i):
        cnt += 1

print(cnt)
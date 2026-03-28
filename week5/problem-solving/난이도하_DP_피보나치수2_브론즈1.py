# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748

n = int(input())

def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}

    if n < 2:
        return n
    
    if n in memo:
        return memo[n]

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    
    return memo[n]

print(fibonacci_memo(n))
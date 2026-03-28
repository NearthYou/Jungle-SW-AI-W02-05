# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904

# dp[1] = 1, dp[2]= 2, dp[3], dp[4] = 5

import sys
input = sys.stdin.readline

def solve():
    n = int(input())

    if n < 4 :
        print(n)
        return

    prev, prevs = 2, 3
    cur = 0
    for _ in range(4, n + 1):
        cur = (prev + prevs) % 15746
        prev = prevs
        prevs = cur

    print(cur)

solve()
# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))

max_diff = 0
for p in permutations(nums):
    cur_diff = sum(abs(p[i] - p[i+1]) for i in range(N - 1))

    if cur_diff > max_diff:
        max_diff = cur_diff

print(max_diff)
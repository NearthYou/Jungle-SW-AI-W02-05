# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = [0] * (n)

for i in range(n):
    nums[i] = int(input())

right = len(nums) - 1
total = 0
for i in range(right, -1, -1):
    count = k // nums[i]
    total += count
    k %= nums[i]
    
print(total)
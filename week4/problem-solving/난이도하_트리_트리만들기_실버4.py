# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

for i in range(1, m + 1):
    print(0, i)
    
last_node = m - 1
for next_node in range(m + 1, n):
    print(last_node, next_node)
    last_node = next_node
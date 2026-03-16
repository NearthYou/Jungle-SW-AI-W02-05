# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493

# 하나의 탑에서 발사된 레이저 신호
# N개의 탑들의 높이가 입력으로 주어짐
# 숫자에서 왼쪽으로

n = int(input())
nums = list(map(int, input().split()))
rs = [0] * n

stack = []
for i in range(n - 1, -1, -1):
    while stack and nums[i] > nums[stack[-1]]:
        idx = stack.pop()
        rs[idx] = i + 1
    stack.append(i)
print(*rs)
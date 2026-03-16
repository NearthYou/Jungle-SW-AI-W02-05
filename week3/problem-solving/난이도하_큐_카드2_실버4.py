# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

# 제일 위에 있는 카드를 버린다.
# 그 다음 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다
# 카드가 한장 남을 때까지 반복

# 1234 -> 234 -> 342
# 제일 먼저 넣은거 pop
# 그 다음 숫자는 pop 한것 다시 append

from collections import deque

n = int(input())
d = deque([x + 1 for x in range(n)])

while len(d) != 1:
    d.popleft()
    pop_item = d.popleft()
    d.append(pop_item)

print(d.pop())


# a = int(input())
# b = 1

# while a > b:
#     b *= 2
    
# print(a * 2 - b)
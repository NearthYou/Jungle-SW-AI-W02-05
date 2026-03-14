# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406

import sys

input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

s = input().strip()
m = int(input())

head = Node(None)
tail = Node(None)
head.next = tail
tail.prev = head

cursor = tail

for char in s:
    new_node = Node(char)
    prev_node = cursor.prev
    
    new_node.prev = prev_node
    new_node.next = cursor
    prev_node.next = new_node
    cursor.prev = new_node

for _ in range(m):
    command = input().split()
    
    if command[0] == 'L':
        if cursor.prev != head:
            cursor = cursor.prev
            
    elif command[0] == 'R':
        if cursor != tail:
            cursor = cursor.next
            
    elif command[0] == 'B':
        if cursor.prev != head:
            delete_node = cursor.prev
            prev_node = delete_node.prev
            
            prev_node.next = cursor
            cursor.prev = prev_node
            
    elif command[0] == 'P':
        new_node = Node(command[1])
        prev_node = cursor.prev
        
        new_node.prev = prev_node
        new_node.next = cursor
        prev_node.next = new_node
        cursor.prev = new_node


res = []
curr = head.next
while curr != tail:
    res.append(curr.data)
    curr = curr.next

print("".join(res))


# import sys

# # 입력을 빠르게 받기 위한 설정
# input = sys.stdin.readline

# left = list(input().strip())  # 커서 왼쪽 문자들
# right = []                    # 커서 오른쪽 문자들

# m = int(input())

# for _ in range(m):
#     cmd = input().split()
    
#     if cmd[0] == 'L':
#         if left:
#             right.append(left.pop())
#     elif cmd[0] == 'R':
#         if right:
#             left.append(right.pop())
#     elif cmd[0] == 'B':
#         if left:
#             left.pop()
#     elif cmd[0] == 'P':
#         left.append(cmd[1])

# # right 스택은 역순으로 쌓여 있으므로 뒤집어서 합침
# print("".join(left + right[::-1]))
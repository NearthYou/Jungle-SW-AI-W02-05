# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828

import sys
input = sys.stdin.readline

n = int(input())
stack = []

def is_empty():
    return len(stack) == 0

for _ in range(n):
    line = input().split()
    command = line[0]
    
    if command == "push":
        stack.append(line[1])
    
    elif command == "pop":
        if is_empty():
            print("-1")
        else:
            print(stack.pop())
    
    elif command == "size":
        print(len(stack))
        
    elif command == "empty":
        print(1 if is_empty() else 0)
        
    elif command == "top":
        if is_empty():
            print("-1")
        else:
            print(stack[-1])
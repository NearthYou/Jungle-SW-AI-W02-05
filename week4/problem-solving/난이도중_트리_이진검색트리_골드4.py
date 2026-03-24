# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639

# import sys
# input = sys.stdin.read
# sys.setrecursionlimit(10**6)
# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

# def insert(node, val):
#     if val < node.val:
#         if node.left is None:
#             node.left = TreeNode(val)
#         else:
#             insert(node.left, val)
#     else:
#         if node.right is None:
#             node.right = TreeNode(val)
#         else:
#             insert(node.right, val)

# def postorder(node):
#     if node is None:
#         return
#     postorder(node.left)
#     postorder(node.right)
#     print(node.val)

# x = list(map(int, input().split()))
# if not x:
#     exit()

# root = TreeNode(x[0])
# for i in range(1, len(x)):
#     insert(root, x[i])

# postorder(root)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.read

nums = list(map(int, input().split()))

def postorder(start, end):
    if start > end:
        return
    
    root = nums[start]
    mid = start + 1
    
    while mid <= end:
        if nums[mid] > root:
            break
        mid += 1
    
    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(root)

if nums:
    postorder(0, len(nums) - 1)
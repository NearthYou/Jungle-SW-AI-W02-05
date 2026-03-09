# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
visited[0] = True
min_cost = float('inf')

def dfs(now, cnt, cost):
    global min_cost
    if(min_cost <= cost):
        return
    if(cnt == N):
        if arr[now][0] != 0:
            min_cost = min(min_cost, cost + arr[now][0])
        return
    
    for next in range(N):
        if not visited[next] and arr[now][next] != 0:
            visited[next] = True
            dfs(next, cnt + 1, cost + arr[now][next])
            visited[next] = False

dfs(0, 1, 0)
print(min_cost)
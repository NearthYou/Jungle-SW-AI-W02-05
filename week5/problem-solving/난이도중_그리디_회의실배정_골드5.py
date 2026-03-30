# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931

# 회의 시작 시간, 끝나는 시간 정해져 있음
# 시작 = 끝. 같을 수 있음. 바로 끝나는거라 가정

# 끝 기준으로 정렬
# 중복 시, 시작 시간이랑 비교해서 더 빨리 시작하는거 채택

import sys
input = sys.stdin.readline

def solve():

    n = int(input())

    if not n:
        return

    meetings = [tuple(map(int, input().split())) for _ in range(n)]
    
    if not meetings:
            return print(0)

    def schedule():
        meetings.sort(key = lambda x: (x[1], x[0]))

        cnt = 0
        prev_end = meetings[0][1]
        for i in range(1, len(meetings)):
            cur_start = meetings[i][0]
            if prev_end <= cur_start:
                cnt += 1
                prev_end = meetings[i][1]
        print(cnt + 1)
    
    schedule()

if __name__ == "__main__":
    solve()
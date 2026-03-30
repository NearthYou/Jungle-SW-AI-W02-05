# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946

# 둘 중 하나가 다른 지원자에 비해 떨어지지 않는다면 합격

# 케이스 T

# T만큼 -> 지원자 숫자 N
# N만큼 -> 서류 심사 성적, 면접 순위 주어짐

# 동석차 없음

# 각 테스트 케이스에 대해서 선발할 수 있는 신입 사원의 최대 인원수를 한줄에 하나씩 출력

# 첫 번째 비교, 같으면 두 번째 비교해서 정렬

# 서류로 정렬한다음 -> 면접만 비교?

# 1위는 그냥 붙임
# 2위부터 검사 -> 1위의 면접 점수랑 검사 -> 이기면 합격
# 3위 -> 2위의 면접 점수랑 검사 -> 이기면 합격
# 4위 -> 3위의 면접 점수랑 검사 -> 이기면 합격

import sys
input = sys.stdin.readline

t = int(input())

rs = []
for _ in range(t):
    n = int(input())
    newbie = [(0, 0)] * n
    
    for i in range(n):
        newbie[i] = tuple(map(int,input().split()))
        
    newbie.sort()
    prev = newbie[0][1]
    cnt = 1
    
    for i in range(1, n):
        if prev > newbie[i][1]:
            cnt += 1
            prev = newbie[i][1]
    
    rs.append(cnt)

for c in rs:
    print(c)


# import sys
# input = sys.stdin.readline

# def solve():
#     try:
#         line = input().split()
#         if not line: return
#         t = int(line[0])
#     except EOFError:
#         return

#     for _ in range(t):
#         n = int(input())
#         # 인덱스가 서류 순위, 값이 면접 순위인 리스트
#         # 0번 인덱스는 사용하지 않으므로 n+1 크기로 생성
#         ranks = [0] * (n + 1)
        
#         for _ in range(n):
#             s_rank, m_rank = map(int, input().split())
#             ranks[s_rank] = m_rank

#         cnt = 0
#         min_m_rank = float('inf')
        
#         # 서류 1등부터 N등까지 차례대로 확인 (이미 정렬된 상태나 다름없음)
#         for i in range(1, n + 1):
#             current_m_rank = ranks[i]
#             if current_m_rank < min_m_rank:
#                 cnt += 1
#                 min_m_rank = current_m_rank
#                 # 만약 면접 1등까지 확인했다면 그 뒤는 볼 필요도 없음 (최적화)
#                 if min_m_rank == 1:
#                     break
        
#         print(cnt)

# if __name__ == "__main__":
#     solve()
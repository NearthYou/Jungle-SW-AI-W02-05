# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

# 한 변의 길이 N과 행렬이 주어질 때 잘라진 하얀색, 파란색 개수를 구해라
# 1이 파란색 0이 흰색
# 전체 종이가 같은 색이 아니면 가로와 세로로 중간 부분을 잘라서 N/2 * N/2로 나눈다.

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

counts = [0, 0]
def divide_conquer(r, c, n):
    color = arr[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if arr[i][j] != color:
                half = n // 2
                divide_conquer(r, c, half)
                divide_conquer(r, c + half, half)
                divide_conquer(r + half, c, half)
                divide_conquer(r + half, c + half, half)
                return
    counts[color] += 1
    return

divide_conquer(0, 0, n)
print(counts[0])
print(counts[1])
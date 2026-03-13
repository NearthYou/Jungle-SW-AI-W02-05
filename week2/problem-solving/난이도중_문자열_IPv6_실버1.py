# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107

ip = input()

# :: 를 기준으로 분리
if "::" in ip:
    left, right = ip.split("::")

    left_parts = left.split(":") if left else []
    right_parts = right.split(":") if right else []
    

    missing_count = 8 - (len(left_parts) + len(right_parts))
    middle_parts = ["0000"] * missing_count
    
    full_parts = left_parts + middle_parts + right_parts
else:

    full_parts = ip.split(":")


restored_parts = []
for part in full_parts:

    restored_parts.append(part.zfill(4))

print(":".join(restored_parts))
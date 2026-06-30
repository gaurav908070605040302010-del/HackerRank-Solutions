#Check Strict Superset
A = set(map(int, input().split()))
n = int(input())

result = True

for _ in range(n):
    B = set(map(int, input().split()))
    if not (A > B):   # A must be a strict superset of B
        result = False

print(result)
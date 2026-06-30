#Piling Up!
from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    cubes = deque(map(int, input().split()))

    last = float('inf')

    while cubes:
        if cubes[0] >= cubes[-1]:
            x = cubes.popleft()
        else:
            x = cubes.pop()

        if x > last:
            print("No")
            break
        last = x
    else:
        print("Yes")
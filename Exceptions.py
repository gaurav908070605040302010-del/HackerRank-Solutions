#Exceptions
t = int(input())

for _ in range(t):
    try:
        a, b = input().split()
        print(int(a) // int(b))
    except Exception as e:
        print("Error Code:", e)
def solve():
    a, b = map(int, input().split())
    if a % b == 0:
        print(0)
        return
    multiplier = a//b+1
    print(multiplier*b-a)

t = int(input())
for i in range(t):
    solve()

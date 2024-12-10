t = int(input())

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[j] - a[i] == j - i:
                count += 1
    return count

for _ in range(t):
    print(solve())
t = int(input())

def split(n, m):
    if n==m:
        return True
    if n % 3 != 0 or n < m:
        return False
    return split(n//3, m) or split(n//3*2, m)

for _ in range(t):
    n, m = map(int, input().split())
    print("YES" if split(n, m) else "NO")
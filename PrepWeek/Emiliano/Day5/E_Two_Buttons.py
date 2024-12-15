n, m = map(int, input().split())

def solve(n, m):
    if m <= n:
        return n - m
    count = 0
    while m > n:
        if not m & 1:
            m //= 2
            count += 1
        else:
            m += 1
            count += 1
    return count + n - m

print(solve(n, m))
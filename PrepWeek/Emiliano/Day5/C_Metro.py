def solve():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if a[0] == 1 and a[s-1] == 1:
        print("YES")
        return
    for i in range(s, n):
        if a[0] == 1 and a[i] == 1 and b[i] == 1 and b[s-1] == 1:
            print("YES")
            return
    print("NO")
solve()
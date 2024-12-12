def solve():
    n = int(input())
    a = list(map(int, input().split()))
    seats = [False] * (n+1)
    seats[a[0]] = True
    for i in range(1,n):
        seats[a[i]] = True
        if a[i] == 1 and seats[2] == False:
            return False
        if a[i] == n and seats[n-1] == False:
            return False
        if a[i] > 1 and a[i] < n and seats[a[i]-1] == False and seats[a[i]+1] == False:
            return False
    return True

t = int(input())
for i in range(t):
    print("YES" if solve() else "NO")

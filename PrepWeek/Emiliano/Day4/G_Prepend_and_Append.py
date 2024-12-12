def solve():
    n = int(input())
    s = input()
    i = 0
    j = n-1
    while i < j and s[i] != s[j]:
        i += 1
        j -= 1
    return j-i+1

t = int(input())
for _ in range(t):
    print(solve())
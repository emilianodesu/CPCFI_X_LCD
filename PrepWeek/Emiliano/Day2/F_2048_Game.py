q = int(input())

def solve():
    _ = int(input())
    s = list(map(int, input().split()))
    if 2048 in s:
        return 'YES'
    s = [i for i in s if i < 2048]
    if sum(s) >= 2048:
        return 'YES'
    return 'NO'


for _ in range(q):
    print(solve())
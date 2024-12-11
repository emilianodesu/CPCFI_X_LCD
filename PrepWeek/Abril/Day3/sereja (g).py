n, m = map(int, input().split())
a = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

distinct_count = [0] * n
seen = set()
for i in range(n - 1, -1, -1):
    seen.add(a[i])
    distinct_count[i] = len(seen)

results = [distinct_count[li - 1] for li in queries]
for result in results:
    print(result)
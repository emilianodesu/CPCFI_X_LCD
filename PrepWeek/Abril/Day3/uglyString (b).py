t = int(input())
results = []

for _ in range(t):
    n = int(input())
    s = input().strip()

    min_deletions = float('inf')

    for i in range(n - 2):
        if s[i:i + 3] == "pie" or s[i:i + 3] == "map":
            min_deletions = min(min_deletions, 2)

    if min_deletions == float('inf'):
        results.append(0)
    else:
        results.append(min_deletions)

for result in results:
    print(result)
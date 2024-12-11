def can_transform(n, m):
    if n == m:
        return True
    if n < m:
        return False
    if n % 3 != 0:
        return False
    return can_transform(n // 3, m) or can_transform(2 * (n // 3), m)


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    results = []

    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        if can_transform(n, m):
            results.append("YES")
        else:
            results.append("NO")

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
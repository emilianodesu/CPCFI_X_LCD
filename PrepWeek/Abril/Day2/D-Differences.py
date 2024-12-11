from collections import defaultdict


def count_pairs(n, a):
    freq = defaultdict(int)
    for i in range(n):
        key = a[i] - i
        freq[key] += 1

    count = 0
    for value in freq.values():
        if value > 1:
            count += value * (value - 1) // 2
    return count


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    results = []

    for _ in range(t):
        n = int(data[index])
        a = list(map(int, data[index + 1:index + 1 + n]))
        index += 1 + n
        results.append(count_pairs(n, a))

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
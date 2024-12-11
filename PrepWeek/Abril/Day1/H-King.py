import math


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def main():
    t = int(input())
    results = []
    for _ in range(t):
        a, b = map(int, input().split())
        results.append(lcm(a, b))

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
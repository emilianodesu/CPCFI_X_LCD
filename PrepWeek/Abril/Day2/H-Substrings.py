def contains_two_substrings(s):
    ab_index = s.find("AB")
    if ab_index != -1 and s.find("BA", ab_index + 2) != -1:
        return "YES"

    ba_index = s.find("BA")
    if ba_index != -1 and s.find("AB", ba_index + 2) != -1:
        return "YES"

    return "NO"


def main():
    import sys
    input = sys.stdin.read
    s = input().strip()
    print(contains_two_substrings(s))


if __name__ == "__main__":
    main()
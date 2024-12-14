def main():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    can_travel = False

    for i in range(s):
        if a[i] == 0:
            can_travel = False
            break
    else:
        can_travel = True

    if can_travel:
        for i in range(s-1, n):
            if b[i] == 0:
                print("NO")
                return
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()

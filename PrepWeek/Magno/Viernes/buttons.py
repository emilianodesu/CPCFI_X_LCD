def main():
    n, m = map(int, input().split())
    pasos = 0
    while m > n:
        if m % 2 == 0:
            m //= 2 
        else:
            m += 1
        pasos += 1
    pasos += n - m
    print(pasos)

if __name__ == "__main__":
    main()

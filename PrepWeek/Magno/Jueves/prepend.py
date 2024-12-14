def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        inicio = 0
        fin = n - 1
        while inicio < fin and s[inicio] != s[fin]:
            inicio += 1
            fin -= 1
        print(fin - inicio + 1)

if __name__ == "__main__":
    main()
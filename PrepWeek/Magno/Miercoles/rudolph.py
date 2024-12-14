def main():
    t = int(input())
    lista = []
    for _ in range(t):
        n = int(input())
        s = input().strip()
        
        c = 0 
        i = 0 
        while i <= n - 3: 
            if s[i:i+3] == 'pie' or s[i:i+3] == 'map':
                c += 1 
                i += 3
            else:
                i += 1
        lista.append(str(c))

    print("\n".join(lista))

if __name__ == "__main__":
    main()

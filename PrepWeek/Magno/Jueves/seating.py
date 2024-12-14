def main():
    t = int(input())
    resultados = []

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        ocupados = set([a[0]])
        resultado = "YES"
        
        for i in range(1, n):
            asiento = a[i]
            if not ((asiento - 1 in ocupados) or (asiento + 1 in ocupados)):
                resultado = "NO"
                break
            ocupados.add(asiento)
        resultados.append(resultado)
    print("\n".join(resultados))

if __name__ == "__main__":
    main()

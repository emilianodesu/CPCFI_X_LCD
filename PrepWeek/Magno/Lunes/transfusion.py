import sys

def main():
    datos = sys.stdin.read().strip().split()
    t = int(datos[0])
    pos = 1

    for _ in range(t):
        n = int(datos[pos])
        pos += 1
        a = list(map(int, datos[pos:pos+n]))
        pos += n
        suma_total = sum(a)

        if suma_total % n != 0:
            print("NO")
            continue

        objetivo = suma_total // n
        suma_impares = 0
        suma_pares = 0

        for i in range(n):
            if (i+1) % 2 == 1:
                suma_impares += a[i]
            else:
                suma_pares += a[i]
        cant_impares = (n+1)//2
        cant_pares = n//2
        
        if suma_impares == objetivo*cant_impares and suma_pares == objetivo*cant_pares:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()

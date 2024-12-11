import sys
import math

def main():
    datos = sys.stdin.read().strip().split()
    t = int(datos[0])
    indice = 1

    for _ in range(t):
        a = int(datos[indice])
        b = int(datos[indice + 1])
        indice += 2
        m = (a * b) // math.gcd(a, b)
        print(m)

if __name__ == "__main__":
    main()
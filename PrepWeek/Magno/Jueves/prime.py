import sys

def factorizacion(n):
    factores = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            if d in factores:
                factores[d] += 1
            else:
                factores[d] = 1
            n //= d
        d += 1
    if n > 1:
        factores[n] = 1
    return factores

def main():
    n = int(input())
    casi_primos = 0
    for i in range(1, n + 1):
        if len(set(factorizacion(i))) == 2:
            casi_primos += 1
    print(casi_primos)

if __name__ == "__main__":
    main()

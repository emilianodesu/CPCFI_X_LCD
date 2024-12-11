import sys

def main():
    datos = sys.stdin.read().strip().split()
    t = int(datos[0])
    pos = 1

    for _ in range(t):
        n = int(datos[pos])
        pos += 1
        camino = datos[pos]
        pos += 1
        dp = [-1]*n
        dp[0] = 0
        for i in range(n):
            if dp[i] == -1:
                continue
            for salto in [1, 2]:
                destino = i+salto
                if destino < n and camino[destino] != '*':
                    suma = dp[i] + (1 if camino[destino] == '@' else 0)
                    if suma > dp[destino]:
                        dp[destino] = suma
        print(max(dp))

if __name__ == "__main__":
    main()

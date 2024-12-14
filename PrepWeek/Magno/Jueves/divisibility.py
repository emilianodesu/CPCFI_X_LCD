import sys

def main():
    datos = sys.stdin.read().split()
    t = int(datos[0])
    indice = 1
    for _ in range(t):
        a, b = int(datos[indice]), int(datos[indice + 1])
        indice += 2
        if a % b == 0:
            print(0)
        else:
            print(b - a % b)

if __name__ == "__main__":
    main()

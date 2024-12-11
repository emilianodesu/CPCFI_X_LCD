import sys

def main():
    datos = sys.stdin.read().strip().split()
    t = int(datos[0])
    indice = 1

    for _ in range(t):
        n = int(datos[indice])
        a = int(datos[indice+1])
        b = int(datos[indice+2])
        indice += 3
        movimientos = datos[indice]
        indice += 1
        x, y = 0, 0

        encontrado = False
        max_pasos = 1000

        for paso in range(max_pasos+1):
            if x == a and y == b:
                encontrado = True
                break
            movimiento = movimientos[paso % n]
            if movimiento == 'N':
                y += 1
            elif movimiento == 'S':
                y -= 1
            elif movimiento == 'E':
                x += 1
            elif movimiento == 'W':
                x -= 1
        print("YES" if encontrado else "NO")

if __name__ == "__main__":
    main()

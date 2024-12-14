import sys

def main():
    datos = sys.stdin.read().split()
    t = int(datos[0])
    indice = 1
    for _ in range(t):
        n = int(datos[indice])
        indice += 1
        digitos_no_usados = list(map(int, datos[indice:indice + n]))
        indice += n
        digitos_posibles = list(set(range(10)) - set(digitos_no_usados))
        
        total = 0
        for i in range(len(digitos_posibles)):
            for j in range(i + 1, len(digitos_posibles)):
                total += 1
        print(total * 6)

if __name__ == "__main__":
    main()

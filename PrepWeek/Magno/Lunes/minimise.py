import sys

def main():
    datos = sys.stdin.read().strip().split()
    t = int(datos[0])
    indice = 1
    
    for _ in range(t):
        n = int(datos[indice])
        indice += 1
        s = '1' + '0'*(n-1)
        print(s)

if __name__ == "__main__":
    main()

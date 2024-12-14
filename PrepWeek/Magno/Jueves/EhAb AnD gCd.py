import sys

def main():
    datos = sys.stdin.read().split()
    t = int(datos[0])
    for i in range(1, t + 1):
        x = int(datos[i])
        a = 1
        b = x - 1
        print(f"{a} {b}")

if __name__ == "__main__":
    main()

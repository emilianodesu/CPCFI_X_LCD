def main():
    datos = int(input())
    x = int(datos)
    c = bin(x).count('1')
    print(c)

if __name__ == "__main__":
    main()

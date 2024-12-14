def main():
    s = input().strip()
    vocales = "aoyeuiAOYEUI"
    resultado = []
    for letra in s:
        if letra not in vocales: 
            resultado.append('.' + letra.lower())
    print(''.join(resultado))


if __name__ == "__main__":
    main()

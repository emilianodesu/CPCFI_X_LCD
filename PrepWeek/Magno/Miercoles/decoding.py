def decodificar_mensaje_sveta(n, s):
    palabra_original = [None] * n
    izquierda = 0
    derecha = n - 1
    
    for i in range(n):
        if i % 2 == 0:
            palabra_original[izquierda] = s[i]
            izquierda += 1
        else:
            palabra_original[derecha] = s[i]
            derecha -= 1
    
    return "".join(palabra_original)

if __name__ == "__main__":
    n = int(input())
    s = input().strip()
    print(decodificar_mensaje_sveta(n, s))

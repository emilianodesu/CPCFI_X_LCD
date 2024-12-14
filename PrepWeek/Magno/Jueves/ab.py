import sys

def main():
    datos = sys.stdin.read().split()
    indice = 0
    t = int(datos[indice])
    indice += 1
    
    for _ in range(t):
        n = int(datos[indice])
        k = int(datos[indice + 1])
        indice += 2
        s = datos[indice]
        indice += 1
        
        negro_actual = s[:k].count('W')
        min_recolorar = negro_actual
        
        for i in range(1, n - k + 1):
            negro_actual += (s[i + k - 1] == 'W') - (s[i - 1] == 'W')
            min_recolorar = min(min_recolorar, negro_actual)
        
        print(min_recolorar)

if __name__ == "__main__":
    main()

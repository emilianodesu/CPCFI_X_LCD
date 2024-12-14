def main():
    t = int(input())
    
    for _ in range(t):
        n, m = map(int, input().split())
        grid= [list(map(int, input().split())) for _ in range(n)]
        visitado = [[False] * m for _ in range(n)]
        volumen_maximo = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0 and not visitado[i][j]:
                    cola = [(i, j)]
                    visitado[i][j] = True
                    volumen = 0
                    
                    while cola:
                        x, y = cola.pop(0)
                        volumen += grid[x][y]
                        
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < m and not visitado[nx][ny] and grid[nx][ny] > 0:
                                visitado[nx][ny] = True
                                cola.append((nx, ny))
                    
                    volumen_maximo = max(volumen_maximo, volumen)
        
        print(volumen_maximo)

if __name__ == "__main__":
    main()

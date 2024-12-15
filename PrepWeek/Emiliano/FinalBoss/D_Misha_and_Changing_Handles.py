n = int(input())
cambios = [tuple(input().split()) for _ in range(n)]
def solve(n, cambios):
    usuarios = {}
    for anterior, nuevo in cambios:
        if anterior not in usuarios:
            usuarios[anterior] = anterior
        usuarios[nuevo] = usuarios[anterior]
        del usuarios[anterior]
    print(len(usuarios))
    for nombre in usuarios:
        print(usuarios[nombre], nombre)
solve(n, cambios)

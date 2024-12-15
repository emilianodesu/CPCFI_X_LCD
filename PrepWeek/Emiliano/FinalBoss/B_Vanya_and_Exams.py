n, r, avg = map(int, input().split())
exams = []
for _ in range(n):
    a, b = map(int, input().split())
    exams.append((a, b))
total = avg*n
actual = sum([x[0] for x in exams])
puntos = total - actual

if puntos <= 0:
    print(0)
    exit()

exams.sort(key=lambda x: x[1])
ens = 0
for a, b in exams:
    tope = r-a
    if tope >= puntos:
        ens += puntos*b
        break
    ens += tope*b
    puntos -= tope
print(ens)
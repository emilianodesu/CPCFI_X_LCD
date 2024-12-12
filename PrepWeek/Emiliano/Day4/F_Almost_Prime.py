n = int(input())
es_primo = [True] * (n+1)
es_primo[0] = es_primo[1] = False
for i in range(2, int(n**0.5) + 1):
    if es_primo[i]:
        for j in range(i*i, n+1, i):
            es_primo[j] = False
divisores = [0] * (n+1)
for i in range(2, n+1):
    if es_primo[i]:
        for j in range(i, n+1, i):
            divisores[j] += 1
print(sum(1 for x in divisores if x==2))

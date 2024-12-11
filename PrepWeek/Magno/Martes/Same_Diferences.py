"""
Problem:
You are given an array a of n integers. Count the number of pairs of indices (i, j) such that i < j and aj - ai = j - i.

Input:
The first line contains one integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first line of each test case contains one integer n (1 ≤ n ≤ 2 * 10^5).

The second line of each test case contains n integers a1, a2, …, an (1 ≤ ai ≤ n) — array a.

It is guaranteed that the sum of n over all test cases does not exceed 2 * 10^5.

Output:
For each test case output the number of pairs of indices (i, j) such that i < j and aj - ai = j - i.
"""

import sys

def main():
    datos = sys.stdin.read().strip().split()
    t = int(datos[0])
    indice = 1

    for _ in range(t):
        n = int(datos[indice])
        indice += 1
        a = list(map(int, datos[indice:indice + n]))
        indice += n

        conteo = 0
        diferencias = {}
        for i in range(n):
            d = a[i] - i
            if d in diferencias:
                conteo += diferencias[d] 
                diferencias[d] += 1 
            else:
                diferencias[d] = 1
                
        print(conteo)

if __name__ == "__main__":
    main()
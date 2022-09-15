import numpy as np

m = int(input("Introduce la dimension de la matriz A: "))**2

matrix = np.zeros(m, dtype=np.uint8)
for i in range(m):
    if i == 0:
        matrix[0] = 2
        continue
    k = matrix[i - 1]
    isprime = 0
    while (not isprime):
        k += 1
        isprime = 1
        for j in range(i):
            if k % matrix[j] == 0:
                isprime = 0
                break

    matrix[i] = k

n = int(np.sqrt(m))
s = ""
for i in range(n):
    for j in range(n):
        s += "{}\t".format(matrix[n * i + j])
    s += "\n"
print("La matriz A de numeros primos consecutivos es:")
print(s)

x=np.reshape(matrix, (n,n))
sumDS = 0
for i in range(n):
  for j in range(i,n):
    sumDS += x[i][j]

print("La suma de los elementos en la matriz diagonal superior es: {}".format(sumDS))
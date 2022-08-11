import numpy as np

i = 0
resultado = 0

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])

for i in range(matriz.shape[0]):
  for j in range(matriz.shape[1]):
    resultado += matriz[i][j]
print(resultado)

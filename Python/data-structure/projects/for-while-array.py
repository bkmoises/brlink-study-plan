n1 = 0
i = 0
j = 0
resultado = 0
lista = []

while i < 5:
  n1 = int(input("Digite um número inteiro: "))
  lista.append(n1)
  i += 1

for j in range (len(lista)):
  resultado += lista[j]


print(resultado)



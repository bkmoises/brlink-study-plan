media = 0
nota = 0

for numero in range (1, 6):
  nota = int(input("Digite o valor da sua nota: "))
  media += nota
print ("Sua média é:", media / 5)

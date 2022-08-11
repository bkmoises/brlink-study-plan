tempo = float(input("Informe o tempo médio da viagem "))
velocidade = float(input("Informe a velocidade média do trajeto "))
distancia = tempo * velocidade
litrosUsados = distancia / 12

print ("A velocidade média no trajeto foi:", velocidade)
print ("O tempo gasto foi:", tempo)
print ("A distância percorrida foi", distancia)
print ("A quantidade de combustivel utilizado foi:", round((litrosUsados))

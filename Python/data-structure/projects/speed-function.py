def trajeto(tempo, velocidade):
    distancia = tempo * velocidade
    return distancia / 12

litros = trajeto(int(input("Informe o tempo médio do trajeto: ")), int(input("Informe a velocidade média do trajeto: ")))

print(litros)

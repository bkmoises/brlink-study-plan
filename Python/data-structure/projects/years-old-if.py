idade = int(input("Digite a sua idade: "))

if (idade >= 0) & (idade <= 12):
  print ("Este usuário é uma criança")
else:
  if (idade >= 13) & (idade <= 17):
    print ("Este usuário é um adolecente")
  else:
    if idade >= 18:
      print ("Este usuário é um adulto")
    else:
      print ("A idade informada é invalida!")

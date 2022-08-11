m1 = float(input("Digite a primeira nota "))
m2 = float(input("Digite a segunda nota "))
m3 = float(input("Digite a tercera nota "))
media = (m1 + m2 + m3) / 3

if (media > 0) & (media <= 4):
  print(f"sua média foi {media}, Reprovado!")
else:
  if (media > 4.1) & (media <= 6):
    print(f"sua média foi {media}, Exame!")
  else:
    print (f"sua média foi {media}, Aprovado!")
